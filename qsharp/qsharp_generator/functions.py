import math
import random
from typing import List, Tuple, Callable, Set, Dict, Any, Optional

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


def generate_single_qubit_block(idx: int) -> Tuple[str, str]:
    """
    Generate a custom single-qubit gate block with a unique index.

    Args:
        idx (int): Index to use in the operation name.

    Returns:
        Tuple[str, str]: (operation name, Q# operation definition string)
    """
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
    name = f"MySingleBlock{idx}"
    return name, f"    operation {name}(q : Qubit) : Unit is Adj + Ctl {{\n{body}\n    }}"

def ensure_single_block(counter: int, existing_names: Set[str], blocks: List[str]) -> Tuple[str, str, int]:
    while True:
        idx = counter
        counter += 1
        block_name, op_text = generate_single_qubit_block(idx)
        if block_name not in existing_names:
            existing_names.add(block_name)
            blocks.append(op_text)
            return block_name, op_text, counter


def add_measure_all(qubit_num: int) -> List[str]:
    return [f"let r{i} = M(q[{i}]);" for i in range(qubit_num)]

