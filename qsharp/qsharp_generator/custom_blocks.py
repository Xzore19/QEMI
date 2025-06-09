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


def make_random_stateprep_block(num_qubits: int, call_type: str = "plain") -> dict:
    MAX_QUBIT_FOR_STATEPREP = 6
    if num_qubits < 1 or num_qubits > MAX_QUBIT_FOR_STATEPREP:
        apply_stmt = get_apply_to_each_call("H", call_type)
        return {
            "import": "Std.Canon",
            "call": apply_stmt,
            "adjoint": True,
            "controlled": call_type in ("controlled", "adj+ctl")
        }

    vec = generate_random_complexpolar_vector(num_qubits)
    coeff_str = "[\n        " + ",\n        ".join(vec) + "\n    ]"
    return {
        "import": "Std.StatePreparation",
        "call": (
            "ApproximatelyPreparePureStateCP(\n"
            "    1e-6,\n"
            f"    {coeff_str},\n"
            "    q\n"
            ");"
        ),
        "adjoint": True,
        "controlled": True
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


BUILTIN_QUANTUM_OPERATIONS = {
    "ApplyQFT": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_qft_props,
    },
    "ApproximatelyPreparePureStateCP": {
        "adjoint": True,
        "controlled": True,
        "generator": make_random_stateprep_block,
    },
    "ApplyToEach": {
        "adjoint": True,
        "controlled": True,
        "generator": make_apply_to_each_props,
    },
    "ApplyOperationPowerA": {
        "adjoint": True,
        "controlled": False,
        "generator": make_apply_op_power_a_props,  # ✅ 你刚定义的函数
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
        if random.random() < 0.2:
            name = random.choice(list(BUILTIN_QUANTUM_OPERATIONS.keys()))
            props = BUILTIN_QUANTUM_OPERATIONS[name]

            if call_type == "adj+ctl" and not (props.get("adjoint") and props.get("controlled")):
                continue
            if call_type in ("adjoint", "adj") and not props.get("adjoint"):
                continue
            if call_type in ("controlled", "ctl") and not props.get("controlled"):
                continue

            # ✅ 统一调用内建模块的生成器
            if name == "ApplyToEach":
                block_name = register_single_qubit_block()
                op_props = props["generator"](block_name, call_type)
                extra_ops.append(block_name)
            elif name == "ApproximatelyPreparePureStateCP":
                op_props = props["generator"](len(target_indices), call_type)
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
