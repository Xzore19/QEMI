import random
import math
import uuid
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
from qsharp_generator.functions import indent, generate_random_complexpolar_vector, get_apply_to_each_call

BUILTIN_BLOCK_NAMES = [
    "ApplyQFT",
    "ApproximatelyPreparePureStateCP",
    "ApplyIfEqualLE",
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

def generate_unique_inline_name() -> str:
    uid = uuid.uuid4().hex[:8]
    return f"__InlineApplyIfEqualAction_{uid}"

def generate_random_gate_block(
    call_type: str,
    target_indices: List[int],
    depth: int,
    register_block: Callable[[], str],
) -> Tuple[Set[int], List[str], List[str]]:
    single_no_param = ["H", "X", "Y", "Z", "S", "T", "I"]
    single_with_param = ["Rx", "Ry", "Rz", "R1"]
    two_no_param = ["CNOT", "SWAP"]
    two_with_param = ["Rxx", "Ryy", "Rzz"]
    three_qubit = ["CCNOT"]

    all_gates = single_no_param + single_with_param + two_no_param + two_with_param + three_qubit
    control_safe = set(single_no_param + single_with_param + two_no_param)

    instructions = []
    used_indices = set()
    extra_ops = []

    for _ in range(depth):
        if random.random() < 0.2:
            name = random.choice(BUILTIN_BLOCK_NAMES)

            if name == "ApplyQFT":
                props = make_apply_qft_props(call_type)
            elif name == "ApproximatelyPreparePureStateCP":
                props = make_random_stateprep_block(len(target_indices), call_type)
            elif name == "ApplyIfEqualLE":
                props = make_apply_if_equalle_block(
                    available_indices=target_indices,
                    depth=depth,
                    register_block=register_block
                )
                if props is None:
                    instructions.append("I(q[0]);")
                    continue
            else:
                continue

            if call_type == "controlled" and not props.get("controlled", False):
                continue
            if call_type == "adjoint" and not props.get("adjoint", False):
                continue

            instructions.append(props["call"])
            used_indices.update(range(len(target_indices)))
            continue

        if random.random() < 0.2:
            block_name = register_block()
            instructions.append(get_apply_to_each_call(block_name, call_type))
            used_indices.update(range(len(target_indices)))
            extra_ops.append(block_name)
            continue

        gate_type = random.choice(all_gates)
        if call_type == "controlled" and gate_type not in control_safe:
            continue

        max_index = len(target_indices) - 1
        if gate_type in single_no_param:
            q = random.randint(0, max_index)
            used_indices.add(q)
            instructions.append(f"{gate_type}(q[{q}]);")

        elif gate_type in single_with_param:
            q = random.randint(0, max_index)
            angle = round(random.uniform(0, 2 * math.pi), 6)
            used_indices.add(q)
            instructions.append(f"{gate_type}({angle}, q[{q}]);")

        elif gate_type in two_no_param and len(target_indices) >= 2:
            q1, q2 = random.sample(range(len(target_indices)), 2)
            used_indices.update([q1, q2])
            instructions.append(f"{gate_type}(q[{q1}], q[{q2}]);")

        elif gate_type in two_with_param and len(target_indices) >= 2:
            q1, q2 = random.sample(range(len(target_indices)), 2)
            angle = round(random.uniform(0, 2 * math.pi), 6)
            used_indices.update([q1, q2])
            instructions.append(f"{gate_type}({angle}, q[{q1}], q[{q2}]);")

        elif gate_type in three_qubit and len(target_indices) >= 3:
            q0, q1, q2 = random.sample(range(len(target_indices)), 3)
            used_indices.update([q0, q1, q2])
            instructions.append(f"{gate_type}(q[{q0}], q[{q1}], q[{q2}]);")

    return used_indices, instructions, extra_ops

def make_apply_if_equalle_block(
    available_indices: List[int],
    depth: int,
    register_block: Callable[[], str],
) -> Optional[Dict[str, Any]]:
    from qsharp_generator.custom_blocks import generate_random_gate_block
    from qsharp_generator.functions import indent

    N = len(available_indices)
    if N < 3:
        return None

    local_indices = list(range(N))
    random.shuffle(local_indices)

    max_cmp_len = min(N // 2, 3)
    while max_cmp_len > 0:
        if N >= 2 * max_cmp_len + 1:
            break
        max_cmp_len -= 1
    if max_cmp_len < 1:
        return None

    cmp_len = random.randint(1, max_cmp_len)
    x_indices = sorted(local_indices[:cmp_len])
    y_indices = sorted(local_indices[cmp_len:2 * cmp_len])
    remaining = local_indices[2 * cmp_len:]
    if not remaining:
        return None

    target_len = random.randint(1, len(remaining))
    target_indices = sorted(random.sample(remaining, target_len))

    # ✅ 这里不再传入 adapter，不能递归嵌套
    _, instructions, _ = generate_random_gate_block(
        call_type="adj+ctl",
        target_indices=list(range(len(target_indices))),
        depth=depth,
        register_block=register_block,
    )

    body = indent(instructions, level=2)
    uuid_tag = uuid.uuid4().hex[:8]
    inline_op = (
        f"operation __InlineApplyIfEqualAction_{uuid_tag}(q : Qubit[]) : Unit is Adj + Ctl {{\n"
        f"{body}\n"
        f"}}"
    )

    def to_array_str(name, indices):
        return f"let {name} = [" + ", ".join(f"q[{i}]" for i in indices) + "];"

    x_decl = to_array_str("x", x_indices)
    y_decl = to_array_str("y", y_indices)
    target_decl = to_array_str("target", target_indices)

    call = (
        f"{inline_op}\n"
        f"{x_decl}\n{y_decl}\n{target_decl}\n"
        f"ApplyIfEqualLE(__InlineApplyIfEqualAction_{uuid_tag}, x, y, target);"
    )

    return {
        "import": "Std.Arithmetic",
        "call": call,
        "adjoint": True,
        "controlled": True,
    }
