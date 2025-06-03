
from qiskit import *
from qiskit.qasm3 import loads
from qiskit_aer import Aer
import ast
import qiskit

qasm_truth = "qasm_code/code.qasm3"
qasm_fuzzing = "qasm_code/fuzzing_code.qasm3"


crash_index = 0
crash_truth = f"qasm_code/buggy_program/crash/truth_{crash_index}.py"
crash_fuzzing = f"qasm_code/buggy_program/crash/fuzzing_{crash_index}.py"


def extract_qc_from_code(qiskit_code):
    tree = ast.parse(qiskit_code)
    namespace = {}
    exec(compile(tree, filename="<ast>", mode="exec"), namespace)
    for var in namespace.values():
        if isinstance(var, QuantumCircuit):
            return var
    return None

def qasm_run(file, fuzzing):
    code = ""
    fuzzing_code = ""
    with open(file, "r") as f:
        for line in f:
            code += line

    qc = extract_qc_from_code(code)

    if qc:
        # 转换为 OpenQASM 3.0
        qasm_code = qiskit.qasm3.dumps(qc)
    else:
        raise Exception("QuantumCircuit Objects not exist")

    with open(qasm_truth, "w") as f1:
        f1.write(qasm_code)

    circuit = loads(qasm_code)
    backend = Aer.get_backend("aer_simulator")

    # 量子电路编译
    compiled_circuit = transpile(circuit, backend)

    # 运行电路
    job = backend.run(compiled_circuit, shots=10000)

    # 获取结果
    result = job.result()
    counts_1 = result.get_counts()

    print(counts_1)
 ################################################################
    with open(fuzzing, "r") as f:
        for line in f:
            fuzzing_code += line

    qc = extract_qc_from_code(fuzzing_code)

    if qc:
        # 转换为 OpenQASM 3.0
        fuzzing_qasm_code = qiskit.qasm3.dumps(qc)
    else:
        raise Exception("QuantumCircuit Objects not exist")

    with open(qasm_fuzzing, "w") as f1:
        f1.write(fuzzing_qasm_code)

    circuit = loads(fuzzing_qasm_code)
    backend = Aer.get_backend("aer_simulator")

    # 量子电路编译
    compiled_circuit = transpile(circuit, backend)

    # 运行电路
    job = backend.run(compiled_circuit, shots=10000)

    # 获取结果
    result = job.result()
    counts_2 = result.get_counts()
    print(counts_2)
    # 打印测量结果
    return counts_1, counts_2

if __name__ == "__main__":
    a, b = qasm_run(crash_truth, crash_fuzzing)

