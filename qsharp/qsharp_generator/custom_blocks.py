import random
import math
import uuid
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
from qsharp_generator.functions import indent, generate_random_complexpolar_vector, get_apply_to_each_call, register_single_qubit_block
 
SUPPORTED_GATES = {
    "H":     {"arity": 1, "adjoint": True,  "controlled": True},
    "X":     {"arity": 1, "adjoint": True,  "controlled": True},
    "Y":     {"arity": 1, "adjoint": True,  "controlled": True},
    "Z":     {"arity": 1, "adjoint": True,  "controlled": True},
    "S":     {"arity": 1, "adjoint": True,  "controlled": True},
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
}

BUILTIN_QUANTUM_OPERATIONS = [
    "ApplyQFT",
    "ApproximatelyPreparePureStateCP",
    "ApplyToEach"
]

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

def make_apply_qft_props(call_type: str) -> dict:
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

def generate_unique_inline_name() -> str:
    uid = uuid.uuid4().hex[:8]
    return f"__InlineApplyIfEqualAction_{uid}"

def generate_random_gate_block(
    call_type: str,
    target_indices: List[int],
    depth: int,
) -> Tuple[Set[int], List[str], List[str]]:

    print(f"[DBG] call_type={call_type}")

    instructions = []
    used_indices = set()
    extra_ops = []

    for _ in range(depth):
        if random.random() < 0.2:
            name = random.choice(BUILTIN_QUANTUM_OPERATIONS)

            if name == "ApplyQFT":
                props = make_apply_qft_props(call_type)
            elif name == "ApproximatelyPreparePureStateCP":
                props = make_random_stateprep_block(len(target_indices), call_type)
            elif name == "ApplyToEach":
                block_name = register_single_qubit_block()
                props = make_apply_to_each_props(block_name, call_type)
                extra_ops.append(block_name)
            else:
                continue

            if "controlled" in call_type and not props.get("controlled", False):
                continue
            if "adjoint" in call_type and not props.get("adjoint", False):
                continue

            instructions.append(props["call"])
            used_indices.update(range(len(target_indices)))
            continue

        gate_type = random.choice(list(SUPPORTED_GATES.keys()))
        props = SUPPORTED_GATES[gate_type]
        print(f"[DBG] trying gate: {gate_type}, call_type: {call_type}, supports_ctl: {props['controlled']}, supports_adj: {props['adjoint']}")

        # 类型不支持则跳过
        if call_type == "adj+ctl":
            if not (props["adjoint"] and props["controlled"]):
                print(f"[SKIP] {gate_type} does not support both Adjoint + Controlled, skipping")
                continue
        elif call_type in ("controlled", "ctl"):
            if not props["controlled"]:
                print(f"[SKIP] {gate_type} does not support Controlled, skipping")
                continue
        elif call_type in ("adjoint", "adj"):
            if not props["adjoint"]:
                print(f"[SKIP] {gate_type} does not support Adjoint, skipping")
                continue

        arity = props["arity"]
        if len(target_indices) < arity:
            continue

        qubits = random.sample(range(len(target_indices)), arity)
        used_indices.update(qubits)

        qubit_args = ", ".join(f"q[{i}]" for i in qubits)

        if gate_type in ["Rx", "Ry", "Rz", "R1", "Rxx", "Ryy", "Rzz"]:
            angle = round(random.uniform(0, 2 * math.pi), 6)
            instructions.append(f"{gate_type}({angle}, {qubit_args});")
        else:
            instructions.append(f"{gate_type}({qubit_args});")

    return used_indices, instructions, extra_ops
