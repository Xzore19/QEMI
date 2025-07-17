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

    code += """\n
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
    total_stmts = 0
    total_miss = 0

    for file in cov.get_data().measured_files():
        _, stmts, _, miss, _ = cov.analysis2(file)
        total_stmts += len(stmts)
        total_miss += len(miss)

    coverage_percent = 100.0 * (total_stmts - total_miss) / total_stmts
    print(f"TTTT: {coverage_percent:.2f}%")
"""

    with open(savefile, "w") as file:
        file.write(code)


if __name__ == "__main__":
    filename = "code_coverage/circuit3.py"
    savefile = "temp_coverage/circuit3.py"
    remove_import(filename, savefile)

