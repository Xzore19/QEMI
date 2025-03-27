from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(5, 4)  # 4 输入比特 + 1 辅助比特
qc.x(4)  # 将辅助比特初始化为 |1⟩
qc.h(range(5))  # 所有比特做 Hadamard

qc.cx(3, 4)  # 非恒定函数：f(x) XOR 控制比特 3

qc.h(range(4))  # 再次 Hadamard（输入比特）
qc.measure(range(4), range(4))

# 编译并运行
backend = Aer.get_backend('aer_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
result = job.result().get_counts()
print('Deutsch-Jozsa 测量结果:', result)

# 判定是否为非恒定函数
if list(result.keys()) == ['0000']:
    print('❌ 错误：被识别为恒定函数')
else:
    print('✅ 正确：该函数是非恒定函数')