import random
import uuid
from typing import List, Optional, Dict, Any
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent, get_qsharp_modifier

CONTROL_BLOCK_REGISTRY = [
    "APPLY_IF_LE",
    "APPLY_IF_L",
    "FOR_LOOP",
    "IFELSE",
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

    # ✅ 用局部 index list 替代全局 target_indices 传下去
    local_indices = list(range(len(target_indices)))

    if random.random() < 1:
        maybe_nested = generate_random_control_block(local_indices, depth, call_type)
        if maybe_nested is not None:
            return indent(maybe_nested["call"].splitlines(), level=1)

    _, instructions, _ = generate_random_gate_block(
        call_type=call_type,
        target_indices=local_indices,
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
    x_local = sorted(local_indices[:cmp_len])
    y_local = sorted(local_indices[cmp_len:2 * cmp_len])
    remaining = local_indices[2 * cmp_len:]
    if not remaining:
        return None
    target_local = sorted(random.sample(remaining, random.randint(1, len(remaining))))

    call_type = "adj+ctl"
    body = make_nested_or_fallback_body(target_local, depth, call_type)
    uuid_tag = uuid.uuid4().hex[:8]
    inline_name = f"__InlineApplyIfRelationLE_{uuid_tag}"
    modifier = get_qsharp_modifier(call_type)

    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    def arr(name, indices):
        return f"let {name} = [" + ", ".join(f"q[{i}]" for i in indices) + "];"

    x_decl = arr("x", x_local)
    y_decl = arr("y", y_local)
    t_decl = arr("target", target_local)

    op_name = random.choice(APPLY_IF_LE_REGISTRY)
    call = (
        f"{inline_op}\n"
        f"{x_decl}\n{y_decl}\n{t_decl}\n"
        f"{op_name}({inline_name}, x, y, target);"
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
    cmp_len = random.randint(1, min(3, N - 1))

    x_local = sorted(local_indices[:cmp_len])
    remaining = local_indices[cmp_len:]
    if not remaining:
        return None

    target_local = sorted(random.sample(remaining, random.randint(1, len(remaining))))

    call_type = "adj+ctl"
    body = make_nested_or_fallback_body(target_local, depth, call_type)
    uuid_tag = uuid.uuid4().hex[:8]
    inline_name = f"__InlineApplyIfRelationL_{uuid_tag}"
    modifier = get_qsharp_modifier(call_type)

    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    bit_string = [random.choice([0, 1]) for _ in range(cmp_len)]
    const_val = int("".join(str(b) for b in reversed(bit_string)), 2)

    def arr(name, indices):
        return f"let {name} = [" + ", ".join(f"q[{i}]" for i in indices) + "];"

    x_decl = arr("x", x_local)
    t_decl = arr("target", target_local)

    op_name = random.choice(APPLY_IF_L_REGISTRY)
    call = (
        f"{inline_op}\n"
        f"{x_decl}\n{t_decl}\n"
        f"{op_name}({inline_name}, {const_val}L, x, target);"
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

    N = len(available_indices)
    local_indices = list(range(N))
    inline_op_name = f"__ForLoopBody_{uuid.uuid4().hex[:8]}"

    # 默认修饰符
    modifier = get_qsharp_modifier(call_type)

    use_controlled = False
    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, N // 2)
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        # ✅ 只将“目标 qubit”传进去生成嵌套体
        body = make_nested_or_fallback_body(target, depth, call_type)

        ctrl_str = ", ".join(f"q[{available_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{available_indices[i]}]" for i in target)

        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        loop_body = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        # 降级为普通/Adjoint 调用
        body = make_nested_or_fallback_body(local_indices, depth, call_type)
        loop_body = f"{'Adjoint ' if call_type == 'adjoint' else ''}{inline_op_name}(q);"

    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    call = (
        f"{inline_op}\n"
        f"for i in 1..3 {{\n"
        f"    {loop_body}\n"
        f"}}"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def make_if_else_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    if not available_indices:
        return None

    N = len(available_indices)
    local_indices = list(range(N))
    uid = uuid.uuid4().hex[:8]

    # 准备修饰符
    modifier = get_qsharp_modifier(call_type)

    use_controlled = False
    if call_type in ("controlled", "adj+ctl") and N >= 2:
        use_controlled = True
        num_ctrl = random.randint(1, N // 2)
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        # 构造两个分支的嵌套体（只针对 target）
        if_body = make_nested_or_fallback_body(target, depth, call_type)
        else_body = make_nested_or_fallback_body(target, depth, call_type)
    else:
        target = local_indices
        ctrl = []
        if_body = make_nested_or_fallback_body(target, depth, call_type)
        else_body = make_nested_or_fallback_body(target, depth, call_type)

    if not if_body or not else_body:
        return None

    # operation 名称
    if_op = f"__IfBody_{uid}"
    else_op = f"__ElseBody_{uid}"

    # 生成两个子 operation（只接受 target qubit）
    def build_inline(name: str, body: str) -> str:
        return f"operation {name}(q : Qubit[]) : Unit{modifier} {{\n{indent(body.splitlines(), 1)}\n}}"

    if_op_def = build_inline(if_op, if_body)
    else_op_def = build_inline(else_op, else_body)

    # 生成调用
    if use_controlled:
        ctrl_str = ", ".join(f"q[{available_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{available_indices[i]}]" for i in target)
        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        call_if = f"{prefix}{if_op}([{ctrl_str}], [{tgt_str}]);"
        call_else = f"{prefix}{else_op}([{ctrl_str}], [{tgt_str}]);"
    else:
        if call_type == "adjoint":
            call_if = f"Adjoint {if_op}(q);"
            call_else = f"Adjoint {else_op}(q);"
        else:
            call_if = f"{if_op}(q);"
            call_else = f"{else_op}(q);"

    # 生成 if 结构（注意 mutable flag = true 是经典控制流）
    full_block = (
        f"{if_op_def}\n\n"
        f"{else_op_def}\n\n"
        f"mutable flag = true;\n"
        f"if flag {{\n"
        f"    {call_if}\n"
        f"}} else {{\n"
        f"    {call_else}\n"
        f"}}"
    )

    return {
        "import": None,
        "call": full_block,
        "adjoint": call_type in ("adjoint", "adj+ctl"),
        "controlled": use_controlled,
    }

def generate_random_control_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    block = random.choice(CONTROL_BLOCK_REGISTRY)
    # block = "IFELSE"  # For testing purposes, always use IFELSE
    # print(f"Generating control block: {block} with depth {depth} and call type {call_type}")
    available_indices = list(range(len(available_indices)))

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
    if block == "IFELSE":
        if depth - 1 <= 0:
            return None
        return make_if_else_block(available_indices, depth - 1, call_type)
    return None
