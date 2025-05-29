import math
import random
from typing import List, Tuple, Callable, Set, Dict, Any, Optional
import uuid

registered_single_qubit_blocks: List[str] = []

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
        return f"ApplyToEachCA({block_name}, q);"
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


# def generate_single_qubit_block() -> Tuple[str, str]:
#     """
#     Generate a custom single-qubit gate block with a unique UUID-based name.

#     Returns:
#         Tuple[str, str]: (operation name, Q# operation definition string)
#     """
#     gates = ["H", "X", "Y", "Z", "S", "T", "I", "Rx", "Ry", "Rz", "R1"]
#     instructions = []
#     for _ in range(random.randint(2, 4)):
#         gate = random.choice(gates)
#         if gate in ["Rx", "Ry", "Rz", "R1"]:
#             angle = round(random.uniform(0, 2 * math.pi), 6)
#             instructions.append(f"{gate}({angle}, q);")
#         else:
#             instructions.append(f"{gate}(q);")

#     body = indent(instructions, level=2)
#     uid = uuid.uuid4().hex[:8]
#     name = f"MySingleBlock_{uid}"
#     return name, f"    operation {name}(q : Qubit) : Unit is Adj + Ctl {{\n{body}\n    }}"

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

