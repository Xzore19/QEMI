import math
import random

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