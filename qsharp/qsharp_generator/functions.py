import math
import random
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
import uuid

registered_single_qubit_blocks: List[str] = []
registered_random_flag_blocks: List[str] = []
registered_oracle_blocks: List[str] = []

def register_single_qubit_block() -> str:
    import uuid
    from qsharp_generator.functions import indent

    gates = ["H", "X", "Y", "Z", "S", "T", "I", "Rx", "Ry", "Rz", "R1"]
    instructions = []
    for _ in range(random.randint(2, 4)):
        gate = random.choice(gates)
        if gate in ["Rx", "Ry", "Rz", "R1"]:
            angle = round(random.uniform(0, 2 * math.pi), 6)
            instructions.append(f"{gate}({angle}, q);")
        else:
            instructions.append(f"{gate}(q);")

    body = indent(instructions, level=2)
    name = f"MySingleBlock_{uuid.uuid4().hex[:8]}"
    op_text = f"    operation {name}(q : Qubit) : Unit is Adj + Ctl {{\n{body}\n    }}"
    registered_single_qubit_blocks.append(op_text)
    return name

def generate_random_complexpolar_vector(num_qubits):
    """
    Generates a normalized list of ComplexPolar values in Q# syntax.

    Args:
        num_qubits (int): Number of qubits, determines output vector size.

    Returns:
        List[str]: A list of strings representing ComplexPolar(r, phi) in Q#.
    """
    dim = 2 ** num_qubits
    squares = [random.uniform(0, 1) for _ in range(dim)]
    total = sum(squares)
    normed = [math.sqrt(x / total) for x in squares]
    phases = [random.uniform(0, 2 * math.pi) for _ in range(dim)]
    return [f"ComplexPolar({round(r, 6)}, {round(phi, 6)})" for r, phi in zip(normed, phases)]

def get_apply_to_each_call(block_name: str, call_type: str) -> str:
    """
    Returns the appropriate Q# ApplyToEach call based on the call type.

    Args:
        block_name (str): The name of the Q# block/operation.
        call_type (str): One of 'plain', 'adjoint', 'controlled'.

    Returns:
        str: The formatted ApplyToEachX call.
    """
    if call_type == "controlled":
        return f"ApplyToEachC({block_name}, q);"
    elif call_type == "adjoint":
        return f"ApplyToEachA({block_name}, q);"
    elif call_type == "plain":
        return f"ApplyToEach({block_name}, q);"
    else:
        return f"ApplyToEachCA({block_name}, q);"
    

def indent(lines, level=1, spaces_per_level=4):
    """
    Indents each line of the given list by a specified level.

    Args:
        lines (List[str]): The lines to indent.
        level (int): The indentation level.
        spaces_per_level (int): Number of spaces per level.

    Returns:
        str: The indented block of lines joined with newlines.
    """
    indent_str = " " * (level * spaces_per_level)
    return "\n".join(f"{indent_str}{line}" for line in lines)

def add_measure_all(qubit_num: int) -> List[str]:
    return [f"let r{i} = M(q[{i}]);" for i in range(qubit_num)]


def get_qsharp_modifier(call_type: str) -> str:
    normalized = call_type.lower()
    if normalized in ["adjoint", "adj"]:
        return " is Adj"
    elif normalized in ["controlled", "ctl"]:
        return " is Ctl"
    elif normalized in ["adj+ctl", "adjoint+controlled", "controlled+adjoint", "ctl+adj"]:
        return " is Adj + Ctl"
    else:
        return ""

def register_random_flag_block_type_1() -> Tuple[str, bool]:
    uid = uuid.uuid4().hex[:8]
    func_name = f"__RandomFlag_{uid}"

    expr_pool = [
        ("ResultAsBool(Zero)", False),
        ("ResultAsBool(One)", True),
        ("not ResultAsBool(Zero)", True),
        ("not ResultAsBool(One)", False),
    ]

    var_defs = []
    var_names = []
    values = []
    for i in range(4):
        var = f"b{i}"
        expr, val = random.choice(expr_pool)
        var_defs.append(f"    let {var} = {expr};")
        var_names.append(var)
        values.append(val)

    if random.random() < 0.5:
        expr = f"({var_names[0]} and {var_names[1]}) or ({var_names[2]} and not {var_names[3]})"
        value = (values[0] and values[1]) or (values[2] and not values[3])
    else:
        expr = f"Xor(Xor({var_names[0]}, {var_names[1]}), Xor({var_names[2]}, {var_names[3]}))"
        value = values[0] ^ values[1] ^ values[2] ^ values[3]

    func_def = (
        f"function {func_name}() : Bool {{\n"
        + "\n".join(var_defs) + "\n"
        + f"    return {expr};\n"
        + "}"
    )

    registered_random_flag_blocks.append(func_def)
    return func_name, value, 0


def register_random_flag_block_type_2() -> Tuple[str, bool]:
    uid = uuid.uuid4().hex[:8]
    func_name = f"__RandomFlag_{uid}"

    expr_pool = [
        ("false", False),
        ("true", True),
        ("not false", True),
        ("not true", False),
    ]

    var_defs = []
    var_names = []
    values = []
    for i in range(4):
        var = f"b{i}"
        expr, val = random.choice(expr_pool)
        var_defs.append(f"    let {var} = {expr};")
        var_names.append(var)
        values.append(val)

    if random.random() < 0.5:
        expr = f"({var_names[0]} and {var_names[1]}) or ({var_names[2]} and not {var_names[3]})"
        value = (values[0] and values[1]) or (values[2] and not values[3])
    else:
        expr = f"Xor(Xor({var_names[0]}, {var_names[1]}), Xor({var_names[2]}, {var_names[3]}))"
        value = values[0] ^ values[1] ^ values[2] ^ values[3]

    func_def = (
        f"function {func_name}() : Bool {{\n"
        + "\n".join(var_defs) + "\n"
        + f"    return {expr};\n"
        + "}"
    )

    registered_random_flag_blocks.append(func_def)
    return func_name, value, 0

def register_random_flag_block_type_3(available_indices: List[int]) -> Tuple[str, bool]:
    uid = uuid.uuid4().hex[:8]
    func_name = f"__RandomFlag_{uid}"

    if not available_indices:
        raise ValueError("没有可用 qubit，无法生成 CheckZero/CheckAllZero flag block")

    if random.random() < 0.5:
        qid = random.choice(available_indices)
        expr = f"CheckZero(q[{qid}])"
        value = True
    else:
        n = random.randint(1, len(available_indices))
        selected = sorted(random.sample(available_indices, k=n))
        qlist = "[" + ", ".join(f"q[{i}]" for i in selected) + "]"
        expr = f"CheckAllZero({qlist})"
        value = True

    func_def = (
        f"operation {func_name}(q : Qubit[]) : Bool {{\n"
        f"    return {expr};\n"
        f"}}"
    )

    registered_random_flag_blocks.append(func_def)
    return func_name, value, 1

def register_random_flag_block_for_dc() -> Tuple[str, bool]:
    if random.random() < 0.5:
        return register_random_flag_block_type_1()
    else:
        return register_random_flag_block_type_2()

def register_random_flag_block(call_type: Optional[str], available_indices: Optional[List[int]] = None) -> Tuple[str, bool]:
    if available_indices is None:
        available_indices = list(range(10))  

    r = random.random()
    if call_type=="plain":
        return register_random_flag_block_type_3(available_indices)
    elif r < 1/2:
        return register_random_flag_block_type_1()
    else:
        return register_random_flag_block_type_2()