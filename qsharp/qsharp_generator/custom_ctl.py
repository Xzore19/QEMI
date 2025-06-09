import random
import uuid
from typing import List, Optional, Dict, Any
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent, get_qsharp_modifier, register_random_flag_block

CONTROL_BLOCK_REGISTRY = [
    "APPLY_IF_LE",
    "APPLY_IF_L",
    "FOR_LOOP",
    "IFELSE",
]

CONTROL_BLOCK_REGISTRY_P = [
    "REPEAT_UNTIL",  
    "WHILE_LOOP",  
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

    if random.random() < 0:
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

    modifier = get_qsharp_modifier(call_type)

    # ✅ plain 类型：插入就地量子门 + 测量 + if 条件
    if call_type == "plain" and N >= 3:
        selected = sorted(random.sample(local_indices, 3))
        used_qubits = [f"q[{available_indices[i]}]" for i in selected]

        # 生成量子门
        _, ops, _ = generate_random_gate_block(
            call_type="plain",
            target_indices=list(range(3)),  # 假定局部映射为 q[0], q[1], q[2]
            depth=3,
        )

        import re

        replaced_ops = []
        for line in ops:
            # 匹配所有 q[数字] 并替换为对应的 used_qubits 内容
            def repl(match):
                i = int(match.group(1))
                return used_qubits[i]
            line = re.sub(r"q\[(\d+)\]", repl, line)
            replaced_ops.append(line)

        # 生成测量语句
        meas_results = []
        for i, q in enumerate(used_qubits):
            meas_results.append(f"let r{i} = Measure([PauliZ], [{q}]);")

        # 拼接条件表达式
        condition = " or ".join([f"r{i} == One" for i in range(3)])

        # 生成两个 body
        if depth-3 <= 0: 
            if_body = make_nested_or_fallback_body(local_indices, depth, call_type)
            else_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        else:
            if_body = make_nested_or_fallback_body(local_indices, depth - 3, call_type)
            else_body = make_nested_or_fallback_body(local_indices, depth - 3, call_type)
        if not if_body or not else_body:
            return None

        block_lines = (
            ["// --- RANDOM FLAG BASED IF ---"]
            + replaced_ops
            + meas_results
            + [f"if {condition} {{"]
            + indent(if_body.splitlines(), 1).splitlines()
            + ["} else {"]
            + indent(else_body.splitlines(), 1).splitlines()
            + ["}"]
        )
        block = "\n".join(block_lines)

        return {
            "import": "Std.Intrinsic",
            "call": block,
            "adjoint": False,
            "controlled": False,
        }

    # ✅ 非 plain 情况：继续使用经典布尔 flag
    if_body = make_nested_or_fallback_body(local_indices, depth, call_type)
    else_body = make_nested_or_fallback_body(local_indices, depth, call_type)
    if not if_body or not else_body:
        return None

    if_op = f"__IfBody_{uid}"
    else_op = f"__ElseBody_{uid}"

    def build_inline(name: str, body: str) -> str:
        return f"operation {name}(q : Qubit[]) : Unit{modifier} {{\n" + indent(body.splitlines(), 1) + "\n}"

    if_op_def = build_inline(if_op, if_body)
    else_op_def = build_inline(else_op, else_body)

    if call_type == "adjoint":
        call_if = f"Adjoint {if_op}(q);"
        call_else = f"Adjoint {else_op}(q);"
    else:
        call_if = f"{if_op}(q);"
        call_else = f"{else_op}(q);"

    flag_func, _ = register_random_flag_block()

    block = (
        f"{if_op_def}\n\n"
        f"{else_op_def}\n\n"
        f"if {flag_func}() {{\n    {call_if}\n}} else {{\n    {call_else}\n}}"
    )

    return {
        "import": "Std.Intrinsic",  # 添加 import，确保 Measure/Reset 可用
        "call": block,
        "adjoint": call_type in ("adjoint", "adj+ctl"),
        "controlled": call_type in ("controlled", "adj+ctl"),
    }


def make_repeat_until_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    if not available_indices:
        return None

    N = len(available_indices)
    local_indices = list(range(N))
    inline_op_name = f"__RepeatBody_{uuid.uuid4().hex[:8]}"
    fixup_op_name = f"__FixupBody_{uuid.uuid4().hex[:8]}"

    modifier = get_qsharp_modifier(call_type)
    use_controlled = False

    # 尝试构造 controlled 调用
    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, N // 2)
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        repeat_body = make_nested_or_fallback_body(target, depth, call_type)
        fixup_body = make_nested_or_fallback_body(target, depth, call_type)  # fixup 使用浅层深度

        ctrl_str = ", ".join(f"q[{available_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{available_indices[i]}]" for i in target)

        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        repeat_call = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
        fixup_call = f"{prefix}{fixup_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        # 非受控调用
        repeat_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        fixup_body = make_nested_or_fallback_body(local_indices, depth, call_type)

        prefix = "Adjoint " if call_type == "adjoint" else ""
        repeat_call = f"{prefix}{inline_op_name}(q);"
        fixup_call = f"{prefix}{fixup_op_name}(q);"

    # 构造内联 operation 定义
    inline_repeat_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{repeat_body}\n"
        f"}}"
    )
    inline_fixup_op = (
        f"operation {fixup_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{fixup_body}\n"
        f"}}"
    )

    # ✅ 用一个新的 qubit 控制退出条件
    logic = [
        "use flag = Qubit();",
        "mutable result = One;",
        "repeat {",
        "    X(flag);",                # 改变测量结果
        f"    {repeat_call}",
        "    set result = M(flag);",
        "} until (result == Zero) fixup {",
        f"    {fixup_call}",
        "}"
    ]

    call = (
        f"{inline_repeat_op}\n"
        f"{inline_fixup_op}\n"
        + "\n".join(logic)
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def make_while_loop_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    if not available_indices:
        return None

    import uuid
    from qsharp_generator.functions import get_qsharp_modifier, indent
    from qsharp_generator.custom_ctl import make_nested_or_fallback_body

    N = len(available_indices)
    local_indices = list(range(N))
    inline_op_name = f"__WhileBody_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)

    use_controlled = False

    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, N // 2)
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        loop_body = make_nested_or_fallback_body(target, depth, call_type)
        ctrl_str = ", ".join(f"q[{available_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{available_indices[i]}]" for i in target)
        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        loop_call = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        loop_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        prefix = "Adjoint " if call_type == "adjoint" else ""
        loop_call = f"{prefix}{inline_op_name}(q);"

    # inline body op
    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{loop_body}\n"
        f"}}"
    )

    # condition 逻辑：用一个 fresh flag qubit
    logic = [
        "use flag = Qubit();",
        "mutable result = Zero;",
        "X(flag);",
        "set result = M(flag);",
        "while (result == One) {",
        f"    {loop_call}",
        "    X(flag);",
        "    set result = M(flag);",
        "}"
    ]

    call = (
        f"{inline_op}\n"
        + "\n".join(logic)
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def generate_random_control_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    if call_type == "plain":
        # 仅在 plain 模式下使用 REPEAT_UNTIL
        block = random.choice(CONTROL_BLOCK_REGISTRY + CONTROL_BLOCK_REGISTRY_P)
    else:
        # 在其他模式下仅使用前四种
        block = random.choice(CONTROL_BLOCK_REGISTRY)
    # block = "REPEAT_UNTIL"  # For testing purposes, always use IFELSE
    available_indices = list(range(len(available_indices)))
    # block = "WHILE_LOOP"  # For testing purposes, always use WHILE_LOOP
        
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
    if block == "REPEAT_UNTIL":
        if depth - 3 <= 0:
            return None
        return make_repeat_until_block(available_indices, depth - 3, call_type)
    if block == "WHILE_LOOP":
        if depth - 3 <= 0:
            return None
        return make_while_loop_block(available_indices, depth - 3, call_type)
    return None
