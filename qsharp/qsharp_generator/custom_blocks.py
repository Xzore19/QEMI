import random
import math
import uuid
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
from qsharp_generator.functions import generate_random_complexpolar_vector, get_apply_to_each_call, register_single_qubit_block
 
SUPPORTED_GATES = {
    # "H":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "X":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "Y":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "Z":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "S":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "SX":    {"arity": 1, "adjoint": True,  "controlled": True},
    # "T":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "I":     {"arity": 1, "adjoint": True,  "controlled": True},
    # "Rx":    {"arity": 1, "adjoint": True,  "controlled": True},
    # "Ry":    {"arity": 1, "adjoint": True,  "controlled": True},
    # "Rz":    {"arity": 1, "adjoint": True,  "controlled": True},
    # "R1":    {"arity": 1, "adjoint": True,  "controlled": True},
    # "CNOT":  {"arity": 2, "adjoint": True,  "controlled": True},
    # "SWAP":  {"arity": 2, "adjoint": True,  "controlled": True},
    # "CX":    {"arity": 2, "adjoint": True,  "controlled": True},
    # "CY":    {"arity": 2, "adjoint": True,  "controlled": True},
    # "CZ":    {"arity": 2, "adjoint": True,  "controlled": True},
    # "Rxx":   {"arity": 2, "adjoint": True,  "controlled": True},
    # "Ryy":   {"arity": 2, "adjoint": True,  "controlled": True},
    # "Rzz":   {"arity": 2, "adjoint": True,  "controlled": True},
    # "CCNOT": {"arity": 3, "adjoint": True,  "controlled": True},
    # "AND":   {"arity": 3, "adjoint": True,  "controlled": False},  # 新增支持
    # "Exp": {"arity": "var", "adjoint": True, "controlled": True},
    "R1Frac": {"arity": 1, "adjoint": True, "controlled": True},
    "RFrac": {"arity": 1, "adjoint": True, "controlled": True},
    "Reset": {"arity": 1, "adjoint": False, "controlled": False},
    "ResetAll": {"arity": "var", "adjoint": False, "controlled": False},
    # "ApplyP": {"arity": 1, "adjoint": True, "controlled": True},
    "ApplyPauli": {"arity": "var", "adjoint": True, "controlled": True},
    "ApplyCNOTChain": {"arity": "var", "adjoint": True, "controlled": True},
}


def make_random_stateprep_block(call_type: str = "plain", num_qubits: int = 5) -> dict:
    import random

    if call_type != "plain":
        raise ValueError("ApproximatelyPreparePureStateCP 仅允许在 plain 模式中使用（因含 ResetAll）")

    MAX_QUBIT_FOR_STATEPREP = 5

    if num_qubits < 1:
        raise ValueError("num_qubits must be ≥ 1")

    actual_qubit_count = random.randint(1, min(num_qubits, MAX_QUBIT_FOR_STATEPREP))
    selected_indices = sorted(random.sample(range(num_qubits), k=actual_qubit_count))

    vec = generate_random_complexpolar_vector(actual_qubit_count)
    coeff_str = "[\n        " + ",\n        ".join(vec) + "\n    ]"
    qubit_str = "[" + ", ".join(f"q[{i}]" for i in selected_indices) + "]"
    reset_stmt = f"ResetAll([{', '.join(f'q[{i}]' for i in selected_indices)}]);"

    return {
        "import": "Std.StatePreparation",
        "call": (
            f"{reset_stmt}\n"
            "ApproximatelyPreparePureStateCP(\n"
            "    1e-6,\n"
            f"    {coeff_str},\n"
            f"    {qubit_str}\n"
            ");"
        ),
        "adjoint": False,
        "controlled": False
    }

def make_prepare_pure_state_d_props(call_type: str = "plain", num_qubits: int = 5) -> Dict[str, Any]:
    import random
    import math

    if call_type != "plain":
        raise ValueError("PreparePureStateD 仅允许在 plain 模式中生成（因含 ResetAll）")

    MAX_QUBIT_FOR_STATEPREPD = 5
    if num_qubits < 1:
        raise ValueError("num_qubits must be ≥ 1")

    # 随机选用的 qubit 数量：1 ~ min(num_qubits, MAX_QUBIT_FOR_STATEPREPD)
    actual_qubit_count = random.randint(1, min(num_qubits, MAX_QUBIT_FOR_STATEPREPD))
    selected_indices = sorted(random.sample(range(num_qubits), k=actual_qubit_count))

    dim = 2**actual_qubit_count
    raw = [random.random() for _ in range(dim)]
    norm = math.sqrt(sum(x * x for x in raw))
    coeffs = [x / norm for x in raw]

    coeff_str = "[\n        " + ",\n        ".join(f"{x:.6f}" for x in coeffs) + "\n    ]"
    qubit_str = "[" + ", ".join(f"q[{i}]" for i in selected_indices) + "]"
    reset_stmt = f"ResetAll([{', '.join(f'q[{i}]' for i in selected_indices)}]);"

    return {
        "import": "Std.StatePreparation",
        "call": (
            f"{reset_stmt}\n"
            f"PreparePureStateD(\n"
            f"    {coeff_str},\n"
            f"    {qubit_str}\n"
            f");"
        ),
        "adjoint": False,
        "controlled": False,
    }

def make_prepare_uniform_superposition_props(call_type: str = "plain", num_qubits: int = 5) -> Dict[str, Any]:
    import random

    if call_type != "plain":
        raise ValueError("PrepareUniformSuperposition 仅允许在 plain 模式中使用（因含 ResetAll）")

    if num_qubits < 1:
        raise ValueError("num_qubits 必须 ≥ 1")

    MAX_QUBIT_FOR_UNIFORM = 5
    actual_qubit_count = random.randint(1, min(num_qubits, MAX_QUBIT_FOR_UNIFORM))
    selected_indices = sorted(random.sample(range(num_qubits), k=actual_qubit_count))
    nStates = random.randint(1, 2**actual_qubit_count)

    qubit_str = "[" + ", ".join(f"q[{i}]" for i in selected_indices) + "]"
    reset_stmt = f"ResetAll([{', '.join(f'q[{i}]' for i in selected_indices)}]);"

    return {
        "import": "Std.StatePreparation",
        "call": (
            f"{reset_stmt}\n"
            f"PrepareUniformSuperposition({nStates}, {qubit_str});"
        ),
        "adjoint": False,
        "controlled": False,
    }

def make_apply_qft_props(call_type: str, max_qubits) -> dict:
    return {
        "import": "Std.Canon",
        "call": "ApplyQFT(q);",
        "adjoint": True,
        "controlled": True
    }

def make_apply_to_each_props(block_name: str, call_type: str) -> Dict[str, Any]:
    return {
        "import": "Std.Canon",
        "call": get_apply_to_each_call(block_name, call_type),
        "adjoint": call_type in ("adj", "adj+ctl"),
        "controlled": call_type in ("ctl", "adj+ctl"),
    }

def make_apply_op_power_a_props(call_type: str = "adjoint", max_qubits: int = 5) -> Dict[str, Any]:
    import uuid
    import random
    from qsharp_generator.functions import get_qsharp_modifier, registered_oracle_blocks
    from qsharp_generator.custom_ctl import make_nested_or_fallback_body

    max_qubits = min(max_qubits, 5)  # 保证不会超过5个

    if max_qubits < 1:
        raise ValueError("ApplyOperationPowerA 至少需要 1 个 qubit")

    num_qubits = random.randint(1, max_qubits)
    local_indices = list(range(num_qubits))

    uid = uuid.uuid4().hex[:8]
    op_name = f"__PowerOp_{uid}"
    modifier = get_qsharp_modifier("adjoint")
    depth = 5

    body = make_nested_or_fallback_body(local_indices, depth, "adjoint")

    op_def = (
        f"operation {op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )
    registered_oracle_blocks.append(op_def)

    power = random.choice([-3, -2, -1, 0, 1, 2, 3])
    call_stmt = f"ApplyOperationPowerA({power}, {op_name}, q);"

    return {
        "import": "Std.Canon",
        "call": call_stmt,
        "adjoint": True,
        "controlled": False,
    }

def make_apply_pauli_from_bitstring_props(call_type: str, max_qubits: int) -> Dict[str, Any]:
    import random

    # if max_qubits < 1:
    #     max_qubits = 1

    num_qubits = random.randint(1, max_qubits)  # 至少1个 qubit
    bits = [False] * num_qubits

    # 至少设置一个为 True，剩下的可为 False（避免全 False 全 True）
    true_count = random.randint(1, num_qubits)
    true_indices = random.sample(range(num_qubits), k=true_count)
    for i in true_indices:
        bits[i] = True

    bits_str = "[" + ", ".join("true" if b else "false" for b in bits) + "]"
    qubits_str = "[" + ", ".join(f"q[{i}]" for i in range(num_qubits)) + "]"

    paulis = random.sample(["PauliX", "PauliY", "PauliZ"], k=2)
    pauli1, pauli2 = paulis

    call_lines = [
        f"let bits = {bits_str};",
        f"ApplyPauliFromBitString({pauli1}, true, bits, {qubits_str});",
        f"ApplyPauliFromBitString({pauli2}, false, bits, {qubits_str});"
    ]

    return {
        "import": "Std.Canon",
        "call": "\n".join(call_lines),
        "adjoint": True,
        "controlled": True,
    }

def make_apply_pauli_from_int_props(call_type: str, max_qubits: int = 5) -> Dict[str, Any]:
    import random

    assert max_qubits >= 1
    num_qubits = random.randint(1, max_qubits)

    # 随机生成一个 integer，位宽不超过 num_qubits
    max_int = 2**num_qubits - 1
    number_state = random.randint(1, max_int)  # 至少一个 bit 是 1
    qubits_str = "[" + ", ".join(f"q[{i}]" for i in range(num_qubits)) + "]"

    paulis = random.sample(["PauliX", "PauliY", "PauliZ"], k=2)
    pauli1, pauli2 = paulis

    call_lines = [
        f"let n = {number_state};",
        f"ApplyPauliFromInt({pauli1}, true, n, {qubits_str});",
        f"ApplyPauliFromInt({pauli2}, false, n, {qubits_str});"
    ]

    return {
        "import": "Std.Canon",
        "call": "\n".join(call_lines),
        "adjoint": True,
        "controlled": True,
    }

def make_add_le_props(call_type: str = "adjoint", max_qubits: int = 6) -> Dict[str, Any]:
    import random

    indices = list(range(max_qubits))
    random.shuffle(indices)

    max_n = max_qubits // 3
    n = random.randint(1, max_n)

    if len(indices) < 3 * n:
        raise ValueError("qubit 数不足，无法生成非重叠的三组寄存器。")

    xs_indices = sorted(indices[:n])
    ys_indices = sorted(indices[n:2*n])
    zs_indices = sorted(indices[2*n:3*n])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]
    zs = [f"q[{i}]" for i in zs_indices]

    reset_stmt = f"ResetAll([{', '.join(zs)}]);"
    add_stmt = f"AddLE([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

    return {
        "import": "Std.Arithmetic",
        "call": f"{reset_stmt}\n{add_stmt}",
        "adjoint": False,
        "controlled": False,
    }

def make_fourier_tdinc_by_le_props(call_type: str = "plain", max_qubits: int = 6) -> Dict[str, Any]:
    import random

    if max_qubits < 2:
        raise ValueError("FourierTDIncByLE 至少需要 2 个 qubit")

    # 尝试从 target_indices 中随机划分两个非重叠子集
    indices = list(range(max_qubits))
    random.shuffle(indices)

    max_n = max_qubits // 2
    n = random.randint(1, max_n)

    if len(indices) < 2 * n:
        raise ValueError("qubit 数不足，无法分配给 xs 和 ys")

    xs_indices = sorted(indices[:n])
    ys_indices = sorted(indices[n:2*n])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]

    call_stmt = f"FourierTDIncByLE([{', '.join(xs)}], [{', '.join(ys)}]);"

    return {
        "import": "Std.Arithmetic",
        "call": call_stmt,
        "adjoint": True,
        "controlled": True,
    }

def make_maj_props(call_type: str = "plain", max_qubits: int = 3) -> Dict[str, Any]:
    import random

    if max_qubits < 3:
        raise ValueError("MAJ gate requires at least 3 qubits.")

    # 从 qubit 池中随机选 3 个不重复的 qubit
    indices = random.sample(range(max_qubits), 3)
    x, y, z = indices

    call_stmt = f"MAJ(q[{x}], q[{y}], q[{z}]);"

    return {
        "import": "Std.Arithmetic",
        "call": call_stmt,
        "adjoint": True,
        "controlled": True,
    }

def make_lookahead_dkrs_addle_props(call_type: str = "plain", max_qubits: int = 9) -> Dict[str, Any]:
    import random

    if call_type != "plain":
        raise ValueError("LookAheadDKRSAddLE 仅允许在 plain 模式中生成（因含 Reset）。")

    if max_qubits < 3:
        raise ValueError("LookAheadDKRSAddLE 至少需要 3 个 qubit。")

    indices = list(range(max_qubits))
    random.shuffle(indices)

    max_n = max_qubits // 3
    n = random.randint(1, max_n)

    if len(indices) < 3 * n:
        raise ValueError("qubit 数不足，无法生成非重叠的三组寄存器。")

    xs_indices = sorted(indices[:n])
    ys_indices = sorted(indices[n:2*n])
    zs_indices = sorted(indices[2*n:3*n])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]
    zs = [f"q[{i}]" for i in zs_indices]

    # ResetAll zs[1:]（除了 carry-in 位 zs[0]）
    reset_stmt = f"ResetAll([{', '.join(zs[1:])}]);" if len(zs) > 1 else ""
    call_stmt = f"LookAheadDKRSAddLE([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

    return {
        "import": "Std.Arithmetic",
        "call": (reset_stmt + "\n" if reset_stmt else "") + call_stmt,
        "adjoint": False,
        "controlled": False,
    }

def make_reflect_about_integer_props(call_type: str = "plain", max_qubits: int = 5) -> Dict[str, Any]:
    import random

    if max_qubits < 1:
        raise ValueError("ReflectAboutInteger 至少需要 1 个 qubit")

    n = random.randint(1, max_qubits)
    reg_indices = sorted(random.sample(range(max_qubits), n))

    reg_str = "[" + ", ".join(f"q[{i}]" for i in reg_indices) + "]"
    max_index = 2**n - 1
    reflect_index = random.randint(0, max_index)

    call_stmt = f"ReflectAboutInteger({reflect_index}, {reg_str});"

    return {
        "import": "Std.Arithmetic",
        "call": call_stmt,
        "adjoint": True,
        "controlled": True,
    }

def make_swap_reverse_register_props(call_type: str = "plain", num_qubits: int = 5) -> Dict[str, Any]:
    import random

    if num_qubits < 2:
        raise ValueError("SwapReverseRegister 需要至少 2 个 qubit")

    actual_qubit_count = random.randint(2, num_qubits)
    selected_indices = sorted(random.sample(range(num_qubits), k=actual_qubit_count))

    qubit_str = "[" + ", ".join(f"q[{i}]" for i in selected_indices) + "]"

    return {
        "import": "Std.Canon",
        "call": f"SwapReverseRegister({qubit_str});",
        "adjoint": True,
        "controlled": True,
    }

def make_relabel_props(call_type: str = "plain", num_qubits: int = 5) -> Dict[str, Any]:
    import random

    if call_type in ("controlled", "ctl", "adj+ctl"):
        raise ValueError("Relabel 不支持 Controlled 调用。")

    if num_qubits < 2:
        raise ValueError("Relabel 至少需要 2 个 qubit")

    count = random.randint(2, num_qubits)
    current_indices = sorted(random.sample(range(num_qubits), count))
    updated_indices = current_indices.copy()
    while True:
        random.shuffle(updated_indices)
        if updated_indices != current_indices:
            break  # 确保不是恒等映射

    current_str = "[" + ", ".join(f"q[{i}]" for i in current_indices) + "]"
    updated_str = "[" + ", ".join(f"q[{i}]" for i in updated_indices) + "]"

    return {
        "import": "Std.Canon",
        "call": f"Relabel({current_str}, {updated_str});",
        "adjoint": True,
        "controlled": False,
    }

BUILTIN_QUANTUM_OPERATIONS = {
    # "ApplyQFT": {
    #     "adjoint": True,
    #     "controlled": True,
    #     "generator": make_apply_qft_props,
    # },
    # "ApproximatelyPreparePureStateCP": {
    #     "adjoint": False,
    #     "controlled": False,
    #     "generator": make_random_stateprep_block,
    # },
    # "PreparePureStateD": {
    #     "adjoint": False,
    #     "controlled": False,
    #     "generator": make_prepare_pure_state_d_props,
    # },
    # "PrepareUniformSuperposition": {
    #     "adjoint": False,  
    #     "controlled": False,
    #     "generator": make_prepare_uniform_superposition_props,
    # },
    # "ApplyToEach": {
    #     "adjoint": True,
    #     "controlled": True,
    #     "generator": make_apply_to_each_props,
    # },
    # "ApplyOperationPowerA": {
    #     "adjoint": True,
    #     "controlled": False,
    #     "generator": make_apply_op_power_a_props, 
    # },
    # "ApplyPauliFromBitString": {
    #     "adjoint": True,
    #     "controlled": True,
    #     "generator": make_apply_pauli_from_bitstring_props,
    # },
    # "ApplyPauliFromInt": {
    #     "adjoint": True,
    #     "controlled": True,
    #     "generator": make_apply_pauli_from_int_props,
    # },
    "AddLE": {
        "adjoint": False,
        "controlled": False,
        "generator": make_add_le_props,
    },
    "FourierTDIncByLE": {
        "adjoint": True,
        "controlled": True,
        "generator": make_fourier_tdinc_by_le_props,
    },
    "MAJ": {
        "adjoint": True,
        "controlled": True,
        "generator": make_maj_props,
    },
    "LookAheadDKRSAddLE": {
        "adjoint": False,
        "controlled": False,
        "generator": make_lookahead_dkrs_addle_props,
    },
    "ReflectAboutInteger": {
        "adjoint": True,
        "controlled": True,
        "generator": make_reflect_about_integer_props,
    },
    "SwapReverseRegister": {
        "adjoint": True,
        "controlled": True,
        "generator": make_swap_reverse_register_props,
    },
    "Relabel": {
        "adjoint": True,
        "controlled": False,
        "generator": make_relabel_props,
    },
}

def generate_random_gate_block(
    call_type: str,
    target_indices: List[int],
    depth: int,
) -> Tuple[Set[int], List[str], List[str]]:

    print(f"[DBG] call_type={call_type}")

    instructions = []
    used_indices = set()
    extra_ops = []

    MAX_RETRIES = 100
    i = 0
    attempts = 0

    while i < depth and attempts < MAX_RETRIES:
        attempts += 1

        # 20% 概率使用内建模块
        if random.random() < 1:
            name = random.choice(list(BUILTIN_QUANTUM_OPERATIONS.keys()))
            props = BUILTIN_QUANTUM_OPERATIONS[name]

            if call_type == "adj+ctl" and not (props.get("adjoint") and props.get("controlled")):
                continue
            if call_type in ("adjoint", "adj") and not props.get("adjoint"):
                continue
            if call_type in ("controlled", "ctl") and not props.get("controlled"):
                continue

            if name in ("AddLE", "MAJ", "LookAheadDKRSAddLE") and len(target_indices) < 3:
                continue
            if name in ("FourierTDIncByLE", "SwapReverseRegister", "Relabel") and len(target_indices) < 2:
                continue

            # ✅ 统一调用内建模块的生成器
            if name == "ApplyToEach":
                block_name = register_single_qubit_block()
                op_props = props["generator"](block_name, call_type)
                extra_ops.append(block_name)
            # elif name == "ApproximatelyPreparePureStateCP":
            #     op_props = props["generator"](len(target_indices), call_type)
            else:
                op_props = props["generator"](call_type, len(target_indices))  # 例如 ApplyQFT, ApplyOperationPowerA

            instructions.append(op_props["call"])
            used_indices.update(range(len(target_indices)))
            i += 1
            continue

        gate_type = random.choice(list(SUPPORTED_GATES.keys()))
        props = SUPPORTED_GATES[gate_type]
        arity = props["arity"]

        # 类型检查
        if call_type == "adj+ctl" and not (props["adjoint"] and props["controlled"]):
            continue
        if call_type in ("controlled", "ctl") and not props["controlled"]:
            continue
        if call_type in ("adjoint", "adj") and not props["adjoint"]:
            continue

        # ---------- 特殊门 ----------
        if gate_type == "Exp":
            qubit_count = random.randint(1, min(3, len(target_indices)))
            if len(target_indices) < qubit_count:
                continue
            selected = random.sample(range(len(target_indices)), qubit_count)
            used_indices.update(selected)
            pauli_labels = [random.choice(["PauliX", "PauliY", "PauliZ"]) for _ in range(qubit_count)]
            theta = round(random.uniform(0, 2 * math.pi), 6)
            paulis_str = "[" + ", ".join(pauli_labels) + "]"
            qubits_str = "[" + ", ".join(f"q[{i}]" for i in selected) + "]"
            instructions.append(f"Exp({paulis_str}, {theta}, {qubits_str});")
            i += 1
            continue

        elif gate_type == "ApplyPauli":
            qubit_count = random.randint(1, min(3, len(target_indices)))
            if len(target_indices) < qubit_count:
                continue
            selected = random.sample(range(len(target_indices)), qubit_count)
            used_indices.update(selected)
            paulis = [random.choice(["PauliX", "PauliY", "PauliZ"]) for _ in range(qubit_count)]
            paulis_str = "[" + ", ".join(paulis) + "]"
            qubits_str = "[" + ", ".join(f"q[{i}]" for i in selected) + "]"
            instructions.append(f"ApplyPauli({paulis_str}, {qubits_str});")
            i += 1
            continue

        elif gate_type == "ResetAll":
            qubit_count = random.randint(1, len(target_indices))
            selected = random.sample(range(len(target_indices)), qubit_count)
            used_indices.update(selected)
            qargs = "[" + ", ".join(f"q[{i}]" for i in selected) + "]"
            instructions.append(f"ResetAll({qargs});")
            i += 1
            continue

        elif gate_type == "ApplyCNOTChain":
            qubit_count = random.randint(1, len(target_indices))  # ✅ 允许单 qubit
            selected = random.sample(range(len(target_indices)), qubit_count)
            used_indices.update(selected)
            qargs = "[" + ", ".join(f"q[{i}]" for i in selected) + "]"
            instructions.append(f"ApplyCNOTChain({qargs});")
            i += 1
            continue
        # ---------- END 特殊门 ----------

        if arity != "var" and len(target_indices) < arity:
            continue

        qubits = random.sample(range(len(target_indices)), arity if arity != "var" else 1)
        used_indices.update(qubits)
        qubit_args = ", ".join(f"q[{i}]" for i in qubits)

        if gate_type in ["Rx", "Ry", "Rz", "R1", "Rxx", "Ryy", "Rzz"]:
            angle = round(random.uniform(0, 2 * math.pi), 6)
            instructions.append(f"{gate_type}({angle}, {qubit_args});")

        elif gate_type == "R1Frac":
            q = qubits[0]
            numerator = random.randint(1, 15)
            power = random.randint(1, 10)
            instructions.append(f"R1Frac({numerator}, {power}, q[{q}]);")

        elif gate_type == "RFrac":
            q = qubits[0]
            pauli = random.choice(["PauliX", "PauliY", "PauliZ"])
            numerator = random.randint(1, 15)
            power = random.randint(1, 10)
            instructions.append(f"RFrac({pauli}, {numerator}, {power}, q[{q}]);")
        elif gate_type == "ApplyP":
            q = qubits[0]
            pauli = random.choice(["PauliX", "PauliY", "PauliZ"])
            instructions.append(f"ApplyP({pauli}, q[{q}]);")

        else:
            instructions.append(f"{gate_type}({qubit_args});")

        i += 1

    return used_indices, instructions, extra_ops
