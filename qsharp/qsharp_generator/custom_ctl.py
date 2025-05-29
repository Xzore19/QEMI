import random
import uuid
from typing import List, Optional, Dict, Any
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent

CONTROL_BLOCK_REGISTRY = [
    "ApplyIfEqualLE",
]

def make_nested_or_fallback_body(
    target_indices: List[int],
    depth: int,
) -> str:
    """
    尝试在 target_indices 上生成嵌套控制流 block。
    若失败，则退化为普通 quantum block。

    返回：已缩进的代码块字符串。
    """
    from qsharp_generator.custom_ctl import generate_random_control_block
    from qsharp_generator.custom_blocks import generate_random_gate_block
    from qsharp_generator.functions import indent

    if random.random() < 1:
        maybe_nested = generate_random_control_block(target_indices, depth)
        if maybe_nested is not None:
            return indent(maybe_nested["call"].splitlines(), level=1)

    # fallback 到正常 block
    _, instructions, _ = generate_random_gate_block(
        call_type="adj+ctl",
        target_indices=list(range(len(target_indices))),
        depth=depth,
    )
    return indent(instructions, level=2)

def make_apply_if_equalle_block(
    available_indices: List[int],
    depth: int,
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

    # ✅ 嵌套调用（有概率），否则降级为普通 block
    body= make_nested_or_fallback_body(
        target_indices=target_indices,
        depth=depth,
    )

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

def generate_random_control_block(
    available_indices: List[int],
    depth: int,
) -> Optional[Dict[str, Any]]:
    block = random.choice(CONTROL_BLOCK_REGISTRY)

    if block == "ApplyIfEqualLE":
        if len(available_indices) < 3:
            return None
        return make_apply_if_equalle_block(available_indices, depth)
    return None
