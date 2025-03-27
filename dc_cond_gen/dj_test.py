from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer

qreg = QuantumRegister(5)  # 4 输入 + 1 辅助
creg = ClassicalRegister(4)
qc = QuantumCircuit(qreg, creg)

qc.x(qreg[4])  # 将辅助比特初始化为 |1⟩
qc.h(qreg)  # 所有量子比特 Hadamard
qc.cx(qreg[3], qreg[4])  # 非恒定函数：控制比特 3
qc.cx(qreg[2], qreg[4])  # 非恒定函数：控制比特 2
qc.h([qreg[0], qreg[1], qreg[2], qreg[3]])  # 输入比特再次 Hadamard
qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])

# 执行模拟器并获取测量结果
backend = Aer.get_backend('aer_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
dj_result = job.result().get_counts()

print('Deutsch-Jozsa 测量结果:', dj_result)
if list(dj_result.keys()) == ['0000']:
    print('❌ 错误：被识别为恒定函数')
else:
    print('✅ 正确：该函数是非恒定函数')