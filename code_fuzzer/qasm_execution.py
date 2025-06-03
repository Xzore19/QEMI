from qiskit import *
from qiskit.qasm3 import loads
from qiskit_aer import Aer
import ast
import qiskit

class QasmExecution:
    def __init__(self, file, simulator="Qiskit"):
        # 对目标的qasm文件调用不同语言的模拟器
        self.file = file
        if simulator == "Qiskit":
            self.qiskit_simulator()


    def qiskit_simulator(self):
        exec_code = ""
        with open(self.file, "r") as file:
            for line in file:
                exec_code += line

        circuit = loads(exec_code)

        # 选择 Qiskit 后端（例如 Aer 模拟器）
        backend = Aer.get_backend("aer_simulator")

        # 量子电路编译
        compiled_circuit = transpile(circuit, backend)

        # 运行电路
        job = backend.run(compiled_circuit, shots=10000)

        # 获取结果
        result = job.result()
        counts = result.get_counts()

        # 打印测量结果
        return counts


    def extract_qc_from_code(self, qiskit_code):
        tree = ast.parse(qiskit_code)
        namespace = {}
        exec(compile(tree, filename="<ast>", mode="exec"), namespace)
        for var in namespace.values():
            if isinstance(var, QuantumCircuit):
                return var
        return None

    def qasm_run(self, file):
        code = ""
        with open(file, "r") as f:
            for line in f:
                code += line

        qc = self.extract_qc_from_code(code)

        if qc:
            # 转换为 OpenQASM 3.0
            qasm_code = qiskit.qasm3.dumps(qc)
        else:
            raise Exception("QuantumCircuit Objects not exist")

        circuit = loads(qasm_code)
        backend = Aer.get_backend("aer_simulator")

        # 量子电路编译
        compiled_circuit = transpile(circuit, backend)

        # 运行电路
        job = backend.run(compiled_circuit, shots=10000)

        # 获取结果
        result = job.result()
        counts = result.get_counts()

        # 打印测量结果
        return counts


