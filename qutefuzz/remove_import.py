def remove_import(filename, savefile):
    code = """
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi
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

    with open(savefile, "w") as file:
        file.write(code)


if __name__ == "__main__":
    filename = "code_coverage/circuit2.py"
    savefile = "coverage/circuit2.py"
    remove_import(filename, savefile)

