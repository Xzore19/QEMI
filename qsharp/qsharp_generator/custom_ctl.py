import random
import uuid
from typing import List, Optional, Dict, Any
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent, get_qsharp_modifier

CONTROL_BLOCK_REGISTRY = [
    "APPLY_IF_LE",
    "APPLY_IF_L",
    "FOR_LOOP",
]

APPLY_IF_LE_REGISTRY = [
    "ApplyIfEqualLE",
    "ApplyIfGreaterLE",
    "ApplyIfGreaterOrEqualLE",
    "ApplyIfLessLE",
    "ApplyIfLessOrEqualLE",
]

APPLY_IF_L_REGISTRY = [
    "ApplyIfEqualL",
    "ApplyIfGreaterL",
    "ApplyIfGreaterOrEqualL",
    "ApplyIfLessL",
    "ApplyIfLessOrEqualL",
]

def make_nested_or_fallback_body(
    target_indices: List[int],
    depth: int,
    call_type: str,
) -> str:
    from qsharp_generator.custom_ctl import generate_random_control_block
    from qsharp_generator.custom_blocks import generate_random_gate_block
    from qsharp_generator.functions import indent

    if random.random() < 1:
        # print(f"[DEBUG] calling nested block with call_type: {call_type}")
        maybe_nested = generate_random_control_block(target_indices, depth, call_type)
        if maybe_nested is not None:
            return indent(maybe_nested["call"].splitlines(), level=1)

    _, instructions, _ = generate_random_gate_block(
        call_type=call_type,
        target_indices=list(range(len(target_indices))),
        depth=depth,
    )
    return indent(instructions, level=2)

def make_apply_if_relation_le_block(
    available_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Optional[Dict[str, Any]]:
    N = len(available_indices)
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

    call_type = "adj+ctl"

    body = make_nested_or_fallback_body(target_indices, depth, call_type)

    uuid_tag = uuid.uuid4().hex[:8]
    inline_name = f"__InlineApplyIfRelationLE_{uuid_tag}"
    modifier = get_qsharp_modifier(call_type)
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    def to_array_str(name, indices):
        return f"let {name} = [" + ", ".join(f"q[{i}]" for i in indices) + "];"

    x_decl = to_array_str("x", x_indices)
    y_decl = to_array_str("y", y_indices)
    target_decl = to_array_str("target", target_indices)

    control_op_name = random.choice(APPLY_IF_LE_REGISTRY)

    call = (
        f"{inline_op}\n"
        f"{x_decl}\n{y_decl}\n{target_decl}\n"
        f"{control_op_name}({inline_name}, x, y, target);"
    )

    return {
        "import": "Std.Arithmetic",
        "call": call,
        "adjoint": True,
        "controlled": True,
    }

def make_apply_if_relation_l_block(
    available_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Optional[Dict[str, Any]]:
    N = len(available_indices)
    if N < 2:
        return None

    local_indices = list(range(N))
    random.shuffle(local_indices)

    max_cmp_len = min(3, N - 1)
    cmp_len = random.randint(1, max_cmp_len)

    x_indices = sorted(local_indices[:cmp_len])
    remaining = local_indices[cmp_len:]
    if not remaining:
        return None

    target_len = random.randint(1, len(remaining))
    target_indices = sorted(random.sample(remaining, target_len))

    call_type = "adj+ctl"

    body = make_nested_or_fallback_body(target_indices, depth, call_type)

    uuid_tag = uuid.uuid4().hex[:8]
    inline_name = f"__InlineApplyIfRelationL_{uuid_tag}"
    modifier = get_qsharp_modifier(call_type)
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    def to_array_str(name, indices):
        return f"let {name} = [" + ", ".join(f"q[{i}]" for i in indices) + "];"

    x_decl = to_array_str("x", x_indices)
    bit_string = [random.choice([0, 1]) for _ in range(cmp_len)]
    c_value = int("".join(str(b) for b in reversed(bit_string)), 2)
    target_decl = to_array_str("target", target_indices)

    control_op_name = random.choice(APPLY_IF_L_REGISTRY)

    call = (
        f"{inline_op}\n"
        f"{x_decl}\n{target_decl}\n"
        f"{control_op_name}({inline_name}, {c_value}L, x, target);"
    )

    return {
        "import": "Std.Arithmetic",
        "call": call,
        "adjoint": True,
        "controlled": True,
    }

def make_for_loop_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    if not available_indices:
        return None

    local_indices = list(range(len(available_indices)))
    # print(f"[DEBUG] calling nested block with call_type: {call_type}")
    body = make_nested_or_fallback_body(local_indices, depth, call_type)

    uuid_tag = uuid.uuid4().hex[:8]
    inline_op_name = f"__ForLoopBody_{uuid_tag}"
    modifier = get_qsharp_modifier(call_type)
    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    call = (
        f"{inline_op}\n"
        f"for i in 1..3 {{\n"
        f"    {inline_op_name}(q);\n"
        f"}}"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adj", "adj+ctl"),
        "controlled": call_type in ("ctl", "adj+ctl"),
    }

def generate_random_control_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    block = random.choice(CONTROL_BLOCK_REGISTRY)
    
    # print(f"Generating control block: {block} with depth {depth} and call type {call_type}")

    if block == "APPLY_IF_LE":
        if len(available_indices) < 3:
            return None
        return make_apply_if_relation_le_block(available_indices, depth, call_type)
    if block == "APPLY_IF_L":
        if len(available_indices) < 2:
            return None
        return make_apply_if_relation_l_block(available_indices, depth, call_type)
    if block == "FOR_LOOP":
        if depth - 1 <= 0:
            return None
        return make_for_loop_block(available_indices, depth - 1, call_type)
    return None
