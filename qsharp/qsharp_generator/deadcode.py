import uuid
from typing import List, Dict, Any
import random
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent, get_qsharp_modifier
from qsharp_generator.custom_ctl import make_nested_or_fallback_body
from qsharp_generator.illegal_block import make_nested_or_illegal_or_fallback_body

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
    local_indices = list(range(len(target_indices)))
    body = make_nested_or_fallback_body(local_indices, depth, call_type)
    
    inline_name = f"__InlineApplyIfRelation_{uuid.uuid4().hex[:8]}"
    modifier = get_qsharp_modifier(call_type)
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit{modifier} {{\n"
        f"{body}\n"
        f"}}"
    )

    lines = [inline_op]
    control_op_name = random.choice(APPLY_IF_OPS)

    # 具体构造控制输入以确保 "deadcode 条件永远不满足"
    if control_op_name == "ApplyIfEqualLE":
        # 11 != 10
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",  # x = 3
            "use y = Qubit[2];", "X(y[0]);",              # y = 2
            f"let target = q;",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[0]);", "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfGreaterLE":
        # 3 > 2 → true → 为了构造 deadcode 要反过来
        lines += [
            "use x = Qubit[2];",              # x = 1 (01)
            "X(x[0]);",                       
            "use y = Qubit[2];",              # y = 2 (10)
            "X(y[1]);",
            f"let target = q;",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualLE":
        # 1 >= 2 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);",             # x = 1
            "use y = Qubit[2];", "X(y[1]);",             # y = 2
            f"let target = q;",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfLessLE":
        # 2 < 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",             # y = 1
            f"let target = q;",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfLessOrEqualLE":
        # 2 <= 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",             # y = 1
            f"let target = q;",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfEqualL":
        # 0 != 3
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",  # x = 3
            f"let target = q;",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterL":
        # 0 > 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",
            f"let target = q;",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualL":
        # 0 >= 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",
            f"let target = q;",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfLessL":
        # 0 < 0 → false
        lines += [
            "use x = Qubit[2];",                        # x = 0
            f"let target = q;",
            f"{control_op_name}({inline_name}, 0L, x, target);"
        ]

    elif control_op_name == "ApplyIfLessOrEqualL":
        # 0 <= -1 → false
        lines += [
            "use x = Qubit[2];",                        # x = 0
            f"let target = q;",
            f"{control_op_name}({inline_name}, -1L, x, target);"
        ]

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
                "    if r == Zero {",
                "        // --- DEADCODE START ---"
            ] + indent(else_body.splitlines(), level=2).splitlines() + [
                "        // --- DEADCODE END ---",
                "    } else {"
            ] + indent(dead_body.splitlines(), level=2).splitlines() + [
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
            "// --- DEADCODE IF-ELSE START ---\n" +
            dead_inline_op + "\n\n" +
            "\n".join(inline_op_lines) +
            f"\n\n{inline_name}(q);" +  # ✅ 加上调用
            "\n// --- DEADCODE IF-ELSE END ---"
        )
    
    else:
        return make_fixed_apply_if_relation_block(
            target_indices=target_indices,
            depth=depth,
            call_type=call_type,
        )

    return {
        "import": None,
        "call": full_code,
        "adjoint": call_type in ("adjoint", "adj+ctl"),
        "controlled": call_type in ("controlled", "adj+ctl"),
    }