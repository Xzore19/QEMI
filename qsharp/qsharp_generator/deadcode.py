import uuid
from typing import List, Set, Dict, Any, Callable, Optional
from qsharp_generator.custom_blocks import generate_random_gate_block
from qsharp_generator.functions import indent

def make_fixed_apply_if_equalle_block(
    target_register: str,
    target_indices: List[int],
    depth: int,
    builtin_block_names: List[str],
    register_block: Callable[[], str],
    required_imports: Set[str],
    make_if_block_adapter: Callable[[List[int]], Optional[Dict[str, Any]]],
) -> Dict[str, Any]:
    required_imports.add("Std.Arithmetic")

    # 构造 inline block
    local_indices = list(range(len(target_indices)))
    _, instructions, _ = generate_random_gate_block(
        call_type="adj+ctl",
        target_indices=local_indices,
        depth=depth,
        builtin_block_names=builtin_block_names,
        register_block=register_block,
        required_imports=required_imports,
        make_apply_if_equalle_block=make_if_block_adapter,
    )

    body = indent(instructions, level=2)
    inline_name = f"__InlineApplyIfEqualAction_{uuid.uuid4().hex[:8]}"
    inline_op = (
        f"operation {inline_name}(q : Qubit[]) : Unit is Adj + Ctl {{\n"
        f"{body}\n"
        f"}}"
    )

    lines = [
        f"{inline_op}",
        "use x = Qubit[2];",
        "X(x[0]);",
        "X(x[1]);",
        "use y = Qubit[2];",
        "X(y[0]);",
        f"let target = {target_register};",
        f"ApplyIfEqualLE({inline_name}, x, y, target);",
        "X(x[0]);",
        "X(x[1]);",
        "X(y[0]);"
    ]
    full_code = "// --- DEADCODE START ---\n" + "\n".join(lines) + "\n// --- DEADCODE END ---"

    return {
        "import": "Std.Arithmetic",
        "call": full_code,
        "adjoint": True,
        "controlled": True,
    }