import uuid
from typing import List, Dict, Any
import random
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent
from qsharp_generator.custom_ctl import make_nested_or_fallback_body

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
    target_register: str,
    target_indices: List[int],
    depth: int,
) -> Dict[str, Any]:

    local_indices = list(range(len(target_indices)))
    body = make_nested_or_fallback_body(local_indices, depth)

    inline_name = f"__InlineApplyIfRelation_{uuid.uuid4().hex[:8]}"
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit is Adj + Ctl {{\n"
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
            f"let target = {target_register};",
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
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualLE":
        # 1 >= 2 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);",             # x = 1
            "use y = Qubit[2];", "X(y[1]);",             # y = 2
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[0]);", "X(y[1]);"
        ]

    elif control_op_name == "ApplyIfLessLE":
        # 2 < 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",             # y = 1
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfLessOrEqualLE":
        # 2 <= 1 → false
        lines += [
            "use x = Qubit[2];", "X(x[1]);",             # x = 2
            "use y = Qubit[2];", "X(y[0]);",             # y = 1
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, x, y, target);",
            "X(x[1]);", "X(y[0]);"
        ]

    elif control_op_name == "ApplyIfEqualL":
        # 0 != 3
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",  # x = 3
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterL":
        # 0 > 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfGreaterOrEqualL":
        # 0 >= 3 → false
        lines += [
            "use x = Qubit[2];", "X(x[0]);", "X(x[1]);",
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, 0L, x, target);",
            "X(x[0]);", "X(x[1]);"
        ]

    elif control_op_name == "ApplyIfLessL":
        # 0 < 0 → false
        lines += [
            "use x = Qubit[2];",                        # x = 0
            f"let target = {target_register};",
            f"{control_op_name}({inline_name}, 0L, x, target);"
        ]

    elif control_op_name == "ApplyIfLessOrEqualL":
        # 0 <= -1 → false
        lines += [
            "use x = Qubit[2];",                        # x = 0
            f"let target = {target_register};",
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
