import uuid
from typing import List, Dict, Any, Optional
import random
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent, get_qsharp_modifier, register_random_flag_block_for_dc
from qsharp_generator.custom_ctl import make_nested_or_fallback_body
from qsharp_generator.illegal_block import make_nested_or_illegal_or_fallback_body

DEADCODE_BLOCK_REGISTRY = [
    "FOR_LOOP_ZERO",
    "IF_FALSE",
    "APPLY_IF"
]

DEADCODE_BLOCK_REGISTRY_P = [
    "REPEAT_UNTIL_DEADCODE",
    "WHILE_FALSE",
    "CTL_ON_CLASSICAL"
]

APPLY_IF_OPS = [
    "ApplyIfEqualL",
    "ApplyIfEqualLE",
    "ApplyIfGreaterL",
    "ApplyIfGreaterLE",
    "ApplyIfGreaterOrEqualL",
    "ApplyIfGreaterOrEqualLE",
    "ApplyIfLessL",
    "ApplyIfLessLE",
    "ApplyIfLessOrEqualL",
    "ApplyIfLessOrEqualLE",
]

def make_fixed_apply_if_relation_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Dict[str, Any]:    

    call_type = "adj+ctl"
    modifier = get_qsharp_modifier(call_type)
    N = len(target_indices)
    local_indices = list(range(N))
    prefix = None
    lines = []
    use_controlled = False

    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, min(2, N // 2))
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        body = make_nested_or_fallback_body(target, depth, call_type)

        ctrl_str = ", ".join(f"q[{local_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{local_indices[i]}]" for i in target)

        lines += [f"let target = [{tgt_str}]; "]

        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        # loop_body = f"{prefix}{control_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        body = make_nested_or_fallback_body(local_indices, depth, call_type)
        lines += [f"let target = q; "]
        prefix = "Adjoint " if call_type == "adjoint" else ""
        # loop_body = f"{'Adjoint ' if call_type == 'adjoint' else ''}{control_op_name}(q);"

    # call_type = "adj+ctl"
    # local_indices = list(range(len(target_indices)))
    # body = make_nested_or_fallback_body(local_indices, depth, call_type)    
    inline_name = f"__InlineApplyIfRelation_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    lines += [inline_op]
    control_op_name = random.choice(APPLY_IF_OPS)

    # 具体构造控制输入以确保 "deadcode 条件永远不满足"
    if control_op_name == "ApplyIfEqualLE":
        # 11 != 10
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",  # x = 3
            "use y = Qubit[2];", "X(y[0]);", ]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, x, y, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, x, y, target);",]
        lines += ["X(x[0]);", "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfGreaterLE":
        # 3 > 2 → true → 为了构造 deadcode 要反过来
        lines += [
            "use x = Qubit[2];",              # x = 1 (01)
            "X(x[0]);",                       
            "use y = Qubit[2];",              # y = 2 (10)
            "X(y[1]);",]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, x, y, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, x, y, target);",]
        lines += [
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualLE":
        # 1 >= 2 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);",             # x = 1
            "use y = Qubit[2];", "X(y[1]);",]             # y = 2]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, x, y, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, x, y, target);",]
        lines += [
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfLessLE":
        # 2 < 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",]             # y = 1]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, x, y, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, x, y, target);",]
        lines += ["X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfLessOrEqualLE":
        # 2 <= 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, x, y, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, x, y, target);",]
        lines += ["X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfEqualL":
        # 0 != 3
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",  ]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, 0L, x, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, 0L, x, target);",]
        lines += ["X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterL":
        # 0 > 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, 0L, x, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, 0L, x, target);",]
        lines += ["X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualL":
        # 0 >= 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, 0L, x, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, 0L, x, target);",]
        lines += ["X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfLessL":
        # 0 < 0 → false
        lines += [
            "use x = Qubit[2];",]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, 0L, x, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, 0L, x, target);",]

    elif control_op_name == "ApplyIfLessOrEqualL":
        # 0 <= -1 → false
        lines += [
            "use x = Qubit[2];", ]
        if use_controlled:
            lines += [f"{prefix}{control_op_name}([{ctrl_str}], ({inline_name}, -1L, x, target));"]
        else:
            lines += [f"{prefix}{control_op_name}({inline_name}, -1L, x, target);",]

    else:
        raise ValueError(f"Unsupported control op: {control_op_name}")

    full_code = "// --- DEADCODE START ---\n" + "\n".join(lines) + "\n// --- DEADCODE END ---"

    return {
        "import": "Std.Arithmetic",
        "call": full_code,
        "adjoint": True,
        "controlled": True,
    }


def make_fixed_if_else_deadcode_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Dict[str, Any]:
    local_indices = list(range(len(target_indices)))

    # 主逻辑（else 分支）
    else_body = make_nested_or_fallback_body(local_indices, depth, call_type)

    inline_name = f"__InlineIfElseDeadcode_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)

    if random.random() < 0.5:
        dead_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        if not dead_body:
            return None

        else_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        if not else_body:
            return None

        flag_func_name, value, _ = register_random_flag_block_for_dc()  # 返回 Bool 的经典表达式函数

        modifier = get_qsharp_modifier(call_type)

        if value:
            # ✅ flag_func 返回 True：deadcode 放在 else
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{",
                f"    if {flag_func_name}() {{"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    } else {",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    }",
                "}"
            ]
        else:
            # ✅ flag_func 返回 False：deadcode 放在 if
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{",
                f"    if {flag_func_name}() {{",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    } else {"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    }",
                "}"
            ]          

        full_code = (
            "\n".join(inline_op_lines) +
            f"\n\n{inline_name}(q);"
        )

        return {
            "import": None,
            "call": full_code,
            "adjoint": call_type in ("adjoint", "adj+ctl"),
            "controlled": call_type in ("controlled", "adj+ctl"),
        }

    if call_type == "plain":
        # ✅ plain：用 Measure + if 判断
        dead_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        if random.random() < 0.5:
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit {{",
                "    use flag = Qubit();",
                "    let r = Measure([PauliZ], [flag]);",
                "    if r == One {",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    } else {"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    }",
                "}"
            ]
            full_code = (
                "\n".join(inline_op_lines) +
                f"\n\n{inline_name}(q);"  # ✅ 添加调用
            )
        else:
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit {{",
                "    use flag = Qubit();",
                "    let r = Measure([PauliZ], [flag]);",
                "    if r == Zero {"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    } else {",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    }",
                "}"
            ]
            full_code = (
                "\n".join(inline_op_lines) +
                f"\n\n{inline_name}(q);"  # ✅ 添加调用
            )            

    elif call_type in ("controlled", "adj+ctl"):
        # ✅ 非 plain：用 Controlled __DeadBlock(...) 包裹，避免测量
        dead_inline_name = f"__DeadBlock_{uuid.uuid4().hex[:8]}"
        dead_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        dead_inline_op = (
            f"operation {dead_inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
            f"{indent(dead_body.splitlines(), level=1)}\n"
            f"}}"
        )

        inline_op_lines = [
            f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{",
            "    use ctrl = Qubit();",
            "    within { } apply {",
            "        // --- DEADCODE START ---",
            f"        Controlled {dead_inline_name}([ctrl], q);",
            "        // --- DEADCODE END ---",
            "    }",
        ] + indent(else_body.splitlines(), level=1).splitlines() + [
            "}"
        ]

        full_code = (
            dead_inline_op + "\n\n" +
            "\n".join(inline_op_lines) +
            f"\n\n{inline_name}(q);"
        )
    
    else:
        # ✅ 新增：使用经典布尔表达式控制 deadcode 的分支
        dead_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        if not dead_body:
            return None

        else_body = make_nested_or_fallback_body(local_indices, depth, call_type)
        if not else_body:
            return None

        flag_func_name, value, _ = register_random_flag_block_for_dc()  # 返回 Bool 的经典表达式函数

        modifier = get_qsharp_modifier(call_type)

        if value:
            # ✅ flag_func 返回 True：deadcode 放在 else
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{",
                f"    if {flag_func_name}() {{"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    } else {",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    }",
                "}"
            ]
        else:
            # ✅ flag_func 返回 False：deadcode 放在 if
            inline_op_lines = [
                f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{",
                f"    if {flag_func_name}() {{",
                "        // --- DEADCODE START ---"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    } else {"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "    }",
                "}"
            ]     

        full_code = (
            "\n".join(inline_op_lines) +
            f"\n\n{inline_name}(q);"
        )

    return {
        "import": None,
        "call": full_code,
        "adjoint": call_type in ("adjoint", "adj+ctl"),
        "controlled": call_type in ("controlled", "adj+ctl"),
    }

def make_fixed_for_loop_zero_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Dict[str, Any]:
    import uuid
    from qsharp_generator.functions import get_qsharp_modifier, indent
    from qsharp_generator.custom_ctl import make_nested_or_fallback_body

    if not target_indices:
        return None

    N = len(target_indices)
    local_indices = list(range(N))
    inline_op_name = f"__ForLoopZeroBody_{uuid.uuid4().hex[:8]}"

    modifier = get_qsharp_modifier(call_type)

    use_controlled = False
    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, min(2, N // 2))
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        body = make_nested_or_fallback_body(target, depth, call_type)

        ctrl_str = ", ".join(f"q[{target_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{target_indices[i]}]" for i in target)

        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        loop_body = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        body = make_nested_or_fallback_body(local_indices, depth, call_type)
        loop_body = f"{'Adjoint ' if call_type == 'adjoint' else ''}{inline_op_name}(q);"

    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    # ✅ 构造 0 次迭代的 for 循环（不会执行 loop_body）
    call = (
        f"{inline_op}\n"
        f"// --- DEADCODE START ---\n"
        f"for i in 1..0 {{\n"  # Q# 1.16 合法，但不会进入循环体
        f"    {loop_body}\n"
        f"}}\n"
        f"// --- DEADCODE END ---"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def make_fixed_repeat_until_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Dict[str, Any]:
    import uuid
    from qsharp_generator.functions import get_qsharp_modifier, indent
    from qsharp_generator.custom_ctl import make_nested_or_fallback_body
    from qsharp_generator.functions import register_random_flag_block_for_dc

    if not target_indices:
        return None

    N = len(target_indices)
    local_indices = list(range(N))
    inline_op_name = f"__RepeatBody_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)

    use_controlled = False
    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, min(2, N // 2))
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        body = make_nested_or_fallback_body(target, depth, call_type)
        ctrl_str = ", ".join(f"q[{target_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{target_indices[i]}]" for i in target)
        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        repeat_call = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
        fixup_body = make_nested_or_fallback_body(target, depth, call_type)
    else:
        body = make_nested_or_fallback_body(local_indices, depth, call_type)
        repeat_call = f"{'Adjoint ' if call_type == 'adjoint' else ''}{inline_op_name}(q);"
        fixup_body = make_nested_or_fallback_body(local_indices, depth, call_type)

    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    # ✅ 注册 flag 函数，直到其返回值为 True ⇒ fixup 永远不会执行
    while True:
        flag_func_name, flag_value, _ = register_random_flag_block_for_dc()
        if flag_value:
            break

    fixup_body = indent(fixup_body.splitlines(), 1)
    fixup_block = (
        "    // --- DEADCODE START ---\n"
        + fixup_body +
        "\n    // --- DEADCODE END ---"
    )

    # ✅ 拼接完整 repeat-until-fixup 结构（fixup 是 deadcode）
    call = (
        f"{inline_op}\n"
        f"repeat {{\n"
        f"    {repeat_call}\n"
        f"}} until ({flag_func_name}()) fixup {{\n"
        f"{fixup_block}\n"
        f"}}"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def make_fixed_while_false_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl",
) -> Dict[str, Any]:
    import uuid
    from qsharp_generator.functions import get_qsharp_modifier, indent
    from qsharp_generator.custom_ctl import make_nested_or_fallback_body
    from qsharp_generator.functions import register_random_flag_block_for_dc

    if not target_indices:
        return None

    N = len(target_indices)
    local_indices = list(range(N))
    inline_op_name = f"__WhileBody_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)

    use_controlled = False
    if call_type in ("controlled", "adj+ctl") and N >= 2 and random.random() < 0.5:
        use_controlled = True
        num_ctrl = random.randint(1, min(2, N // 2))
        ctrl = sorted(random.sample(local_indices, num_ctrl))
        target = sorted([i for i in local_indices if i not in ctrl])
        if not target:
            return None

        body = make_nested_or_fallback_body(target, depth, call_type)
        ctrl_str = ", ".join(f"q[{target_indices[i]}]" for i in ctrl)
        tgt_str = ", ".join(f"q[{target_indices[i]}]" for i in target)
        prefix = "Controlled Adjoint " if call_type == "adj+ctl" else "Controlled "
        loop_body = f"{prefix}{inline_op_name}([{ctrl_str}], [{tgt_str}]);"
    else:
        body = make_nested_or_fallback_body(local_indices, depth, call_type)
        loop_body = f"{'Adjoint ' if call_type == 'adjoint' else ''}{inline_op_name}(q);"

    inline_op = (
        f"operation {inline_op_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    # ✅ 注册一个总返回 False 的布尔函数作为 while 条件
    while True:
        flag_func_name, flag_value, _ = register_random_flag_block_for_dc()
        if not flag_value:
            break  # 只接受返回 False 的函数

    # ✅ 构造 while 条件永远不满足的死循环结构
    call = (
        f"{inline_op}\n"
        f"// --- DEADCODE START ---\n"
        f"while ({flag_func_name}()) {{\n"
        f"    {loop_body}\n"
        f"}}\n"
        f"// --- DEADCODE END ---"
    )

    return {
        "import": None,
        "call": call,
        "adjoint": call_type in ("adjoint", "adj", "adj+ctl"),
        "controlled": use_controlled,
    }

def make_bitstring_deadcode_block(
    target_indices: List[int],
    depth: int,
    call_type: str = "adj+ctl"
) -> Optional[Dict[str, Any]]:
    local_indices = list(range(len(target_indices)))
    dead_inline_name = f"__DeadBlock_{uuid.uuid4().hex[:8]}"
    wrapper_inline_name = f"__InlineBitstringDeadcode_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)

    call_type = "adj+ctl"
    dead_body = make_nested_or_fallback_body(local_indices, depth, call_type)
    if not dead_body:
        return None

    dead_inline_op = (
        f"operation {dead_inline_name}(q : Qubit[]) : Unit is Adj + Ctl {{\n"
        f"{indent(dead_body.splitlines(), level=1)}\n"
        f"}}"
    )

    use_bitstring = random.random() < 0.5
    ctrl_bits = [random.choice([False, True]) for _ in range(3)]
    ctrl_init = [f"        X(ctrl[{i}]);" for i, b in enumerate(ctrl_bits) if b]
    actual_value = "".join("1" if b else "0" for b in ctrl_bits)

    if use_bitstring:
        # 设置一个永远不匹配的目标位串
        mismatch_bits = ["true" if not b else "false" for b in ctrl_bits]
        bit_str = "[" + ", ".join(mismatch_bits) + "]"

        call_stmt = [
            *ctrl_init,
            f"        ApplyControlledOnBitString({bit_str}, {dead_inline_name}, ctrl, q);"
        ]
    else:
        # 控制值为实际状态 + 偏移，确保不匹配
        actual_int = sum(2**i for i, b in enumerate(ctrl_bits) if b)
        mismatched_int = (actual_int + random.randint(1, 7)) % 8
        call_stmt = [
            f"        // ctrl actual = |{actual_value}⟩ (int {actual_int}), condition = {mismatched_int}",
            *ctrl_init,
            f"        ApplyControlledOnInt({mismatched_int}, {dead_inline_name}, ctrl, q);"
        ]

    wrapper_inline_op_lines = [
        f"operation {wrapper_inline_name}(q : Qubit[]) : Unit {{",
        "    use ctrl = Qubit[3];",
        "    within { } apply {",
        "        // --- DEADCODE START ---",
        *call_stmt,
        "        // --- DEADCODE END ---",
        "    }",
        "    ResetAll(ctrl);",
        "}"
    ]

    full_code = (
        dead_inline_op + "\n\n" +
        "\n".join(wrapper_inline_op_lines) +
        f"\n\n{wrapper_inline_name}(q);"
    )

    return {
        "import": None,
        "call": full_code,
        "adjoint": False,
        "controlled": False,
    }


def generate_fixed_deadcode_block(
    available_indices: List[int],
    depth: int,
    call_type: str,
) -> Optional[Dict[str, Any]]:
    # 可选的 deadcode 控制结构类型
    if call_type == "plain":
        block = random.choice(DEADCODE_BLOCK_REGISTRY+ DEADCODE_BLOCK_REGISTRY_P)
    else:
        block = random.choice(DEADCODE_BLOCK_REGISTRY)

    available_indices = list(range(len(available_indices)))

    if block == "FOR_LOOP_ZERO":
        if len(available_indices) < 1 or depth <= 0:
            return None
        return make_fixed_for_loop_zero_block(available_indices, depth, call_type)

    if block == "REPEAT_UNTIL_DEADCODE":
        if len(available_indices) < 1 or depth <= 2:
            return None
        return make_fixed_repeat_until_block(available_indices, depth, call_type)

    if block == "IF_FALSE":
        if len(available_indices) < 1 or depth <= 0:
            return None
        return make_fixed_if_else_deadcode_block(available_indices, depth, call_type)
    
    if block == "APPLY_IF":
        if len(available_indices) < 1 or depth <= 0:
            return None
        return make_fixed_apply_if_relation_block(available_indices, depth, call_type)
    
    if block == "WHILE_FALSE":
        if len(available_indices) < 1 or depth <= 0:
            return None
        return make_fixed_while_false_block(available_indices, depth, call_type)
    
    if block == "CTL_ON_CLASSICAL":
        if len(available_indices) < 1 or depth <= 0:
            return None
        return make_bitstring_deadcode_block(available_indices, depth, call_type)

    return None