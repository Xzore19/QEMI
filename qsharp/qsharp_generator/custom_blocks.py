import random
import math
import uuid
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
from qsharp_generator.functions import generate_random_complexpolar_vector, get_apply_to_each_call, register_single_qubit_block
 
SUPPORTED_GATES = {
    "H":     {"arity": 1, "adjoint": True,  "controlled": True},
    "X":     {"arity": 1, "adjoint": True,  "controlled": True},
    "Y":     {"arity": 1, "adjoint": True,  "controlled": True},
    "Z":     {"arity": 1, "adjoint": True,  "controlled": True},
    "S":     {"arity": 1, "adjoint": True,  "controlled": True},
    "SX":    {"arity": 1, "adjoint": True,  "controlled": True},
    "T":     {"arity": 1, "adjoint": True,  "controlled": True},
    "I":     {"arity": 1, "adjoint": True,  "controlled": True},
    "Rx":    {"arity": 1, "adjoint": True,  "controlled": True},
    "Ry":    {"arity": 1, "adjoint": True,  "controlled": True},
    "Rz":    {"arity": 1, "adjoint": True,  "controlled": True},
    "R1":    {"arity": 1, "adjoint": True,  "controlled": True},
    "CNOT":  {"arity": 2, "adjoint": True,  "controlled": True},
    "SWAP":  {"arity": 2, "adjoint": True,  "controlled": True},
    "CX":    {"arity": 2, "adjoint": True,  "controlled": True},
    "CY":    {"arity": 2, "adjoint": True,  "controlled": True},
    "CZ":    {"arity": 2, "adjoint": True,  "controlled": True},
    "Rxx":   {"arity": 2, "adjoint": True,  "controlled": True},
    "Ryy":   {"arity": 2, "adjoint": True,  "controlled": True},
    "Rzz":   {"arity": 2, "adjoint": True,  "controlled": True},
    "CCNOT": {"arity": 3, "adjoint": True,  "controlled": True},
    "AND":   {"arity": 3, "adjoint": True,  "controlled": False},  # 新增支持
    "Exp": {"arity": "var", "adjoint": True, "controlled": True},
    "R1Frac": {"arity": 1, "adjoint": True, "controlled": True},
    "RFrac": {"arity": 1, "adjoint": True, "controlled": True},
    "Reset": {"arity": 1, "adjoint": False, "controlled": False},
    "ResetAll": {"arity": "var", "adjoint": False, "controlled": False},
    "ApplyP": {"arity": 1, "adjoint": True, "controlled": True},
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

def make_add_block_by_type(op_name: str, call_type: str = "plain", num_qubits: int = 9) -> Dict[str, Any]:
    import random

    if call_type != "plain":
        raise ValueError(f"{op_name} 仅允许在 plain 模式中生成（因使用 ResetAll）")

    if num_qubits < 3:
        raise ValueError(f"{op_name} 至少需要 3 个 qubit")

    indices = list(range(num_qubits))
    random.shuffle(indices)

    max_n = num_qubits // 3
    n = random.randint(1, max_n)

    if len(indices) < 3 * n:
        raise ValueError("qubit 数不足，无法分配非重叠的三组寄存器")

    xs_indices = sorted(indices[:n])
    ys_indices = sorted(indices[n:2*n])
    zs_indices = sorted(indices[2*n:3*n])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]
    zs = [f"q[{i}]" for i in zs_indices]

    reset_stmt = f"ResetAll([{', '.join(zs[1:])}]);" if len(zs) > 1 else ""
    call_stmt = f"{op_name}([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

    return {
        "import": "Std.Arithmetic",
        "call": (reset_stmt + "\n" if reset_stmt else "") + call_stmt,
        "adjoint": False,
        "controlled": False,
    }

def make_ripple_carry_cg_incbyle_props(call_type: str = "plain", num_qubits: int = 9) -> Dict[str, Any]:
    import random

    if num_qubits < 2:
        raise ValueError("RippleCarryCGIncByLE 至少需要 2 个 qubit")

    indices = list(range(num_qubits))
    random.shuffle(indices)

    # 为保证 xs ≤ ys，预留最少长度
    max_ys_len = num_qubits // 2
    ys_len = random.randint(1, max_ys_len)
    xs_len = random.randint(1, ys_len)

    total_needed = xs_len + ys_len
    if len(indices) < total_needed:
        raise ValueError("可用 qubit 数不足以生成 RippleCarryCGIncByLE")

    xs_indices = sorted(indices[:xs_len])
    ys_indices = sorted(indices[xs_len:xs_len + ys_len])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]

    return {
        "import": "Std.Arithmetic",
        "call": f"RippleCarryCGIncByLE([{', '.join(xs)}], [{', '.join(ys)}]);",
        "adjoint": True,
        "controlled": True,
    }

# def make_add_le_props(call_type: str = "adjoint", max_qubits: int = 6) -> Dict[str, Any]:
#     import random

#     indices = list(range(max_qubits))
#     random.shuffle(indices)

#     max_n = max_qubits // 3
#     n = random.randint(1, max_n)

#     if len(indices) < 3 * n:
#         raise ValueError("qubit 数不足，无法生成非重叠的三组寄存器。")

#     xs_indices = sorted(indices[:n])
#     ys_indices = sorted(indices[n:2*n])
#     zs_indices = sorted(indices[2*n:3*n])

#     xs = [f"q[{i}]" for i in xs_indices]
#     ys = [f"q[{i}]" for i in ys_indices]
#     zs = [f"q[{i}]" for i in zs_indices]

#     reset_stmt = f"ResetAll([{', '.join(zs)}]);"
#     add_stmt = f"AddLE([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

#     return {
#         "import": "Std.Arithmetic",
#         "call": f"{reset_stmt}\n{add_stmt}",
#         "adjoint": False,
#         "controlled": False,
#     }

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

# def make_lookahead_dkrs_addle_props(call_type: str = "plain", max_qubits: int = 9) -> Dict[str, Any]:
#     import random

#     if call_type != "plain":
#         raise ValueError("LookAheadDKRSAddLE 仅允许在 plain 模式中生成（因含 Reset）。")

#     if max_qubits < 3:
#         raise ValueError("LookAheadDKRSAddLE 至少需要 3 个 qubit。")

#     indices = list(range(max_qubits))
#     random.shuffle(indices)

#     max_n = max_qubits // 3
#     n = random.randint(1, max_n)

#     if len(indices) < 3 * n:
#         raise ValueError("qubit 数不足，无法生成非重叠的三组寄存器。")

#     xs_indices = sorted(indices[:n])
#     ys_indices = sorted(indices[n:2*n])
#     zs_indices = sorted(indices[2*n:3*n])

#     xs = [f"q[{i}]" for i in xs_indices]
#     ys = [f"q[{i}]" for i in ys_indices]
#     zs = [f"q[{i}]" for i in zs_indices]

#     # ResetAll zs[1:]（除了 carry-in 位 zs[0]）
#     reset_stmt = f"ResetAll([{', '.join(zs[1:])}]);" if len(zs) > 1 else ""
#     call_stmt = f"LookAheadDKRSAddLE([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

#     return {
#         "import": "Std.Arithmetic",
#         "call": (reset_stmt + "\n" if reset_stmt else "") + call_stmt,
#         "adjoint": False,
#         "controlled": False,
#     }

# def make_ripple_carry_cg_addle_props(call_type: str = "plain", num_qubits: int = 9) -> Dict[str, Any]:
#     import random

#     if call_type != "plain":
#         raise ValueError("RippleCarryCGAddLE 仅允许在 plain 模式中生成（因使用 ResetAll）")

#     if num_qubits < 3:
#         raise ValueError("RippleCarryCGAddLE 至少需要 3 个 qubit")

#     indices = list(range(num_qubits))
#     random.shuffle(indices)

#     max_n = num_qubits // 3
#     n = random.randint(1, max_n)

#     if len(indices) < 3 * n:
#         raise ValueError("无法为 xs, ys, zs 分配非重叠的 qubit 子集")

#     xs_indices = sorted(indices[:n])
#     ys_indices = sorted(indices[n:2*n])
#     zs_indices = sorted(indices[2*n:3*n])

#     xs = [f"q[{i}]" for i in xs_indices]
#     ys = [f"q[{i}]" for i in ys_indices]
#     zs = [f"q[{i}]" for i in zs_indices]

#     # Reset zs[1:] 保留 zs[0] 可为 carry-in
#     reset_stmt = f"ResetAll([{', '.join(zs[1:])}]);" if len(zs) > 1 else ""
#     call_stmt = f"RippleCarryCGAddLE([{', '.join(xs)}], [{', '.join(ys)}], [{', '.join(zs)}]);"

#     return {
#         "import": "Std.Arithmetic",
#         "call": (reset_stmt + "\n" if reset_stmt else "") + call_stmt,
#         "adjoint": False,
#         "controlled": False,
#     }

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

def make_ripple_carry_ttk_incbyle_props(call_type: str = "plain", num_qubits: int = 9) -> Dict[str, Any]:
    import random

    if num_qubits < 2:
        raise ValueError("RippleCarryTTKIncByLE 至少需要 2 个 qubit")

    indices = list(range(num_qubits))
    random.shuffle(indices)

    max_ys_len = num_qubits // 2
    ys_len = random.randint(1, max_ys_len)
    xs_len = random.randint(1, min(ys_len, max_ys_len))

    if xs_len + ys_len > num_qubits:
        raise ValueError("可用 qubit 数不足以生成 RippleCarryTTKIncByLE")

    xs_indices = sorted(indices[:xs_len])
    ys_indices = sorted(indices[xs_len:xs_len + ys_len])

    xs = [f"q[{i}]" for i in xs_indices]
    ys = [f"q[{i}]" for i in ys_indices]

    return {
        "import": "Std.Arithmetic",
        "call": f"RippleCarryTTKIncByLE([{', '.join(xs)}], [{', '.join(ys)}]);",
        "adjoint": True,
        "controlled": True,
    }

def make_incby_block(op_type: str, call_type: str, num_qubits: int = 5) -> Dict[str, Any]:
    import random

    if num_qubits < 1:
        raise ValueError(f"{op_type} 需要至少 1 个 qubit")

    SAFE_INCBY_ADDERS = {
        "plain": "RippleCarryCGIncByLE",
        "adjoint": "RippleCarryCGIncByLE",
        "controlled": "RippleCarryTTKIncByLE",  # CG 不支持 controlled
        "adj+ctl": "RippleCarryTTKIncByLE",     # CG 不支持 controlled+adjoint
    }

    import_stmt = "Std.Arithmetic"
    extra_import = ""

    # 通用 ys 构造
    def random_qubit_list(n):
        return sorted(random.sample(range(num_qubits), n))

    if op_type in ("IncByI", "IncByL", "IncByIUsingIncByLE", "IncByLUsingIncByLE"):
        max_len = num_qubits
        n = random.randint(1, max_len)
        ys_indices = random_qubit_list(n)
        ys_str = "[" + ", ".join(f"q[{i}]" for i in ys_indices) + "]"
        max_val = 2 ** n - 1
        c = random.randint(0, max_val)

        if op_type == "IncByI":
            call = f"IncByI({c}, {ys_str});"

        elif op_type == "IncByL":
            extra_import = "Microsoft.Quantum.Math"
            call = f"IncByL(IntAsBigInt({c}), {ys_str});"

        elif op_type == "IncByIUsingIncByLE":
            adder = SAFE_INCBY_ADDERS[call_type]
            call = f"IncByIUsingIncByLE({adder}, {c}, {ys_str});"

        elif op_type == "IncByLUsingIncByLE":
            adder = SAFE_INCBY_ADDERS[call_type]
            extra_import = "Microsoft.Quantum.Math"
            call = f"IncByLUsingIncByLE({adder}, IntAsBigInt({c}), {ys_str});"

    elif op_type == "IncByLE":
        max_len = num_qubits // 2
        ys_len = random.randint(1, max_len)
        xs_len = random.randint(1, ys_len)

        total = xs_len + ys_len
        if total > num_qubits:
            raise ValueError("qubit 不足以分配 xs 和 ys")

        indices = random.sample(range(num_qubits), total)
        xs_indices = sorted(indices[:xs_len])
        ys_indices = sorted(indices[xs_len:])

        xs_str = "[" + ", ".join(f"q[{i}]" for i in xs_indices) + "]"
        ys_str = "[" + ", ".join(f"q[{i}]" for i in ys_indices) + "]"
        call = f"IncByLE({xs_str}, {ys_str});"

    elif op_type == "IncByLEUsingAddLE":
        max_len = num_qubits // 2
        n = random.randint(1, max_len)

        if 2 * n > num_qubits:
            raise ValueError("qubit 不足以分配等长 xs 与 ys")

        indices = random.sample(range(num_qubits), 2 * n)
        xs_indices = sorted(indices[:n])
        ys_indices = sorted(indices[n:])

        xs_str = "[" + ", ".join(f"q[{i}]" for i in xs_indices) + "]"
        ys_str = "[" + ", ".join(f"q[{i}]" for i in ys_indices) + "]"

        call = f"IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, {xs_str}, {ys_str});"

    else:
        raise ValueError(f"未知 IncBy 操作类型: {op_type}")

    all_imports = [import_stmt]
    if extra_import:
        all_imports.append(extra_import)

    return {
        "import": "\n".join(all_imports),
        "call": call,
        "adjoint": True,
        "controlled": True,
    }

BUILTIN_QUANTUM_OPERATIONS = {
    "ApplyQFT": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_qft_props,
    },
    "ApproximatelyPreparePureStateCP": {
        "adjoint": False,
        "controlled": False,
        "generator": make_random_stateprep_block,
    },
    "PreparePureStateD": {
        "adjoint": False,
        "controlled": False,
        "generator": make_prepare_pure_state_d_props,
    },
    "PrepareUniformSuperposition": {
        "adjoint": False,  
        "controlled": False,
        "generator": make_prepare_uniform_superposition_props,
    },
    "ApplyToEach": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_to_each_props,
    },
    "ApplyOperationPowerA": {
        "adjoint": True,
        "controlled": False,
        "generator": make_apply_op_power_a_props, 
    },
    "ApplyPauliFromBitString": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_pauli_from_bitstring_props,
    },
    "ApplyPauliFromInt": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_pauli_from_int_props,
    },
    "AddLE": {
        "adjoint": False,
        "controlled": False,
        "generator": lambda ct, nq: make_add_block_by_type("AddLE", ct, nq),
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
        "generator": lambda ct, nq: make_add_block_by_type("LookAheadDKRSAddLE", ct, nq),
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
    "RippleCarryCGAddLE": {
        "adjoint": False,
        "controlled": False,
        "generator": lambda ct, nq: make_add_block_by_type("RippleCarryCGAddLE", ct, nq),
    },
    "RippleCarryCGIncByLE": {
        "adjoint": True,
        "controlled": False,
        "generator": make_ripple_carry_cg_incbyle_props,
    },
    "RippleCarryTTKIncByLE": {
        "adjoint": True,
        "controlled": True,
        "generator": make_ripple_carry_ttk_incbyle_props,
    },
    "IncByI": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByI", call_type, num_qubits),
    },
    "IncByL": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByL", call_type, num_qubits),
    },
    "IncByLE": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByLE", call_type, num_qubits),
    },
    "IncByIUsingIncByLE": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByIUsingIncByLE", call_type, num_qubits),
    },
    "IncByLUsingIncByLE": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByLUsingIncByLE", call_type, num_qubits),
    },
    "IncByLEUsingAddLE": {
        "adjoint": True,
        "controlled": True,
        "generator": lambda call_type, num_qubits: make_incby_block("IncByLEUsingAddLE", call_type, num_qubits),
    },
}

MIN_QUBITS_REQUIRED = {
    # 三寄存器
    "AddLE": 3,
    "MAJ": 3,
    "LookAheadDKRSAddLE": 3,
    "RippleCarryCGAddLE": 3,

    # 双寄存器
    "FourierTDIncByLE": 2,
    "SwapReverseRegister": 2,
    "Relabel": 2,
    "RippleCarryCGIncByLE": 2,
    "RippleCarryTTKIncByLE": 2,
    "IncByLE": 2,
    "IncByLEUsingAddLE": 3,
}

def generate_random_gate_block(
    call_type: str,
    target_indices: List[int],
    depth: int,
) -> Tuple[Set[int], List[str], List[str]]:

    # print(f"[DBG] call_type={call_type}")

    instructions = []
    used_indices = set()
    extra_ops = []

    MAX_RETRIES = 100
    attempts = 0

    available_indices = list(range(len(target_indices)))

    # 提前决定是否加前缀修饰符
    use_prefix = random.random() < 0.5
    control_indices = []
    data_indices = available_indices  # 默认全部 qubit 都参与

    if use_prefix and call_type in ("controlled", "ctl", "adj+ctl") and len(available_indices) >= 2:
        num_controls = random.randint(1, len(available_indices) // 2)
        control_indices = sorted(random.sample(available_indices, num_controls))
        data_indices = list(range(len(target_indices)-num_controls))
        new_target_indices = [i for i in available_indices if i not in control_indices]

        if not data_indices:
            # fallback，无法拆分控制位/受控位
            use_prefix = False
            control_indices = []
            data_indices = available_indices

    i = 0
    while i < depth and attempts < MAX_RETRIES:
        attempts += 1

        if random.random() < 0.3:
            name = random.choice(list(BUILTIN_QUANTUM_OPERATIONS.keys()))
            props = BUILTIN_QUANTUM_OPERATIONS[name]

            if call_type == "adj+ctl" and not (props.get("adjoint") and props.get("controlled")):
                continue
            if call_type in ("adjoint", "adj") and not props.get("adjoint"):
                continue
            if call_type in ("controlled", "ctl") and not props.get("controlled"):
                continue

            if len(data_indices) < MIN_QUBITS_REQUIRED.get(name, 1):
                continue

            if name == "ApplyToEach":
                block_name = register_single_qubit_block()
                op_props = props["generator"](block_name, call_type)
                extra_ops.append(block_name)
            else:
                op_props = props["generator"](call_type, len(data_indices))

            instructions.append(op_props["call"])
            used_indices.update([target_indices[i] for i in data_indices])
            i += 1
            continue

        gate_type = random.choice(list(SUPPORTED_GATES.keys()))
        props = SUPPORTED_GATES[gate_type]
        arity = props["arity"]

        if call_type == "adj+ctl" and not (props["adjoint"] and props["controlled"]):
            continue
        if call_type in ("controlled", "ctl") and not props["controlled"]:
            continue
        if call_type in ("adjoint", "adj") and not props["adjoint"]:
            continue

        if arity != "var" and len(data_indices) < arity:
            continue

        def qstr(indices):
            return ", ".join(f"q[{i}]" for i in indices)

        if gate_type == "Exp":
            qubit_count = random.randint(1, min(3, len(data_indices)))
            selected = random.sample(data_indices, qubit_count)
            pauli_labels = [random.choice(["PauliX", "PauliY", "PauliZ"]) for _ in selected]
            theta = round(random.uniform(0, 2 * math.pi), 6)
            instructions.append(f"Exp([{', '.join(pauli_labels)}], {theta}, [{qstr(selected)}]);")
            used_indices.update([target_indices[i] for i in selected])
            i += 1
            continue

        elif gate_type == "ApplyPauli":
            qubit_count = random.randint(1, min(3, len(data_indices)))
            selected = random.sample(data_indices, qubit_count)
            paulis = [random.choice(["PauliX", "PauliY", "PauliZ"]) for _ in selected]
            instructions.append(f"ApplyPauli([{', '.join(paulis)}], [{qstr(selected)}]);")
            used_indices.update([target_indices[i] for i in selected])
            i += 1
            continue

        elif gate_type == "ResetAll":
            qubit_count = random.randint(1, len(data_indices))
            selected = random.sample(data_indices, qubit_count)
            instructions.append(f"ResetAll([{qstr(selected)}]);")
            used_indices.update([target_indices[i] for i in selected])
            i += 1
            continue

        elif gate_type == "ApplyCNOTChain":
            qubit_count = random.randint(1, len(data_indices))
            selected = random.sample(data_indices, qubit_count)
            instructions.append(f"ApplyCNOTChain([{qstr(selected)}]);")
            used_indices.update([target_indices[i] for i in selected])
            i += 1
            continue

        if arity == "var":
            selected = random.sample(data_indices, 1)
        else:
            selected = random.sample(data_indices, arity)

        qubit_args = qstr(selected)
        used_indices.update([target_indices[i] for i in selected])

        if gate_type in ["Rx", "Ry", "Rz", "R1", "Rxx", "Ryy", "Rzz"]:
            angle = round(random.uniform(0, 2 * math.pi), 6)
            instructions.append(f"{gate_type}({angle}, {qubit_args});")
        elif gate_type == "R1Frac":
            numerator = random.randint(1, 15)
            power = random.randint(1, 10)
            instructions.append(f"R1Frac({numerator}, {power}, q[{selected[0]}]);")
        elif gate_type == "RFrac":
            pauli = random.choice(["PauliX", "PauliY", "PauliZ"])
            numerator = random.randint(1, 15)
            power = random.randint(1, 10)
            instructions.append(f"RFrac({pauli}, {numerator}, {power}, q[{selected[0]}]);")
        elif gate_type == "ApplyP":
            pauli = random.choice(["PauliX", "PauliY", "PauliZ"])
            instructions.append(f"ApplyP({pauli}, q[{selected[0]}]);")
        else:
            instructions.append(f"{gate_type}({qubit_args});")

        i += 1

    uid = uuid.uuid4().hex[:8]
    op_name = f"__GenBlock_{uid}"
    body = "\n    " + "\n    ".join(instructions)

    if call_type == "adjoint":
        sig = ": Unit is Adj"
    elif call_type in ("controlled", "ctl"):
        sig = ": Unit is Ctl"
    elif call_type == "adj+ctl":
        sig = ": Unit is Adj + Ctl"
    else:
        sig = ": Unit"

    inline_op = f"operation {op_name}(q : Qubit[]) {sig} {{\n{body}\n}}"

    if use_prefix and control_indices:
        controls_str = "[" + ", ".join(f"q[{i}]" for i in control_indices) + "]"
        targets_str = "[" + ", ".join(f"q[{i}]" for i in new_target_indices) + "]"

        if call_type in ("controlled", "ctl"):
            call_stmt = f"Controlled {op_name}({controls_str}, {targets_str});"
        else:
            call_stmt = f"Controlled Adjoint {op_name}({controls_str}, {targets_str});"
    else:
        call_stmt = f"{op_name}(q);"

    instructions = [inline_op, call_stmt]
    extra_ops = []

    return used_indices, instructions, extra_ops

