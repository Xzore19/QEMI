def remove_import(filename):
    code = """
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister
from qiskit_aer import Aer
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
from qiskit.circuit.library import *
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from math import pi
import numpy as np
\n
def main():
"""

    with open(filename, "r") as file:
        for line in file:
            if "import" not in line:
                code += "    " + line

    code +="""\n
if __name__ == "__main__":
    from coverage import Coverage

    cov = Coverage(
        source=["qiskit"],
        branch=False,
        data_suffix=True
    )
    cov.start()

    main()

    cov.stop()
    cov.save()
    cov.combine()
    cov.report()
"""

    with open(filename, "w") as file:
        file.write(code)


if __name__ == "__main__":
    filename = "code_coverage/fuzzing_0.py"
    remove_import(filename)

