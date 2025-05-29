import uuid
import random
from typing import List, Optional, Dict, Any
from qsharp_generator.functions import indent, get_qsharp_modifier
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.custom_ctl import make_nested_or_fallback_body

def make_nested_or_illegal_or_fallback_body(
    target_indices: List[int],
    depth: int,
    call_type: str,
) -> str:
    """
    随机选择插入嵌套控制流、无限循环或普通量子代码块。

    返回：已缩进的代码块字符串。
    """
    from qsharp_generator.custom_ctl import generate_random_control_block
    from qsharp_generator.custom_blocks import generate_random_gate_block
    from qsharp_generator.illegal_block import make_infinite_loop_block
    from qsharp_generator.functions import indent

    r = random.random()

    # 尝试插入嵌套控制流 block（60%）
    if r < 0:
        maybe_nested = generate_random_control_block(target_indices, depth, call_type)
        if maybe_nested is not None:
            return indent(maybe_nested["call"].splitlines(), level=1)

    # 尝试插入无限循环 block（20%）
    if r < 1:
        maybe_illegal = make_infinite_loop_block(target_indices, depth)
        if maybe_illegal is not None:
            return indent(maybe_illegal["call"].splitlines(), level=1)

    # fallback 到普通 quantum block（20%）
    _, instructions, _ = generate_random_gate_block(
        call_type,
        target_indices=list(range(len(target_indices))),
        depth=depth,
    )
    return indent(instructions, level=2)

def make_infinite_loop_block(
    available_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Optional[Dict[str, Any]]:
    if not available_indices:
        return None

    local_indices = list(range(len(available_indices)))
    body = make_nested_or_fallback_body(local_indices, depth, call_type)

    uuid_tag = uuid.uuid4().hex[:8]
    inline_op_name = f"__InfiniteLoopBody_{uuid_tag}"

    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit is Adj + Ctl {{\n"
        f"{body}\n"
        f"}}"
    )

    loop_type = random.choice(["while", "repeat"])

    if loop_type == "while":
        loop_block = (
            f"while (true) {{\n"
            f"    {inline_op_name}(q);\n"
            f"}}"
        )
    else:  # repeat-until false fixup loop
        loop_block = (
            f"repeat {{\n"
            f"    {inline_op_name}(q);\n"
            f"}} until (false)\n"
            f"fixup {{ }};"
        )

    call = (
        f"{inline_op}\n"
        f"{loop_block}"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": False,
        "controlled": True,
    }