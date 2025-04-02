from qiskit import transpile
from qiskit.qasm3 import loads
from qiskit_aer import Aer

class QasmExecution:
    def __init__(self, file, simulator):
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
        print("Measurement Results:", counts)
