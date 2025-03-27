from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer

dj_qreg = QuantumRegister(9)  # 8 输入 + 1 辅助
dj_creg = ClassicalRegister(8)
qc = QuantumCircuit(dj_qreg, dj_creg)

qc.x(dj_qreg[8])  # 将辅助比特初始化为 |1⟩
qc.h(dj_qreg)  # 所有量子比特 Hadamard
qc.cx(dj_qreg[5], dj_qreg[7])  # 非恒定函数：控制比特 5
qc.cx(dj_qreg[4], dj_qreg[7])  # 非恒定函数：控制比特 4
qc.cx(dj_qreg[2], dj_qreg[7])  # 非恒定函数：控制比特 2
qc.cx(dj_qreg[6], dj_qreg[7])  # 非恒定函数：控制比特 6
qc.cx(dj_qreg[3], dj_qreg[7])  # 非恒定函数：控制比特 3
qc.ccx(dj_qreg[6], dj_qreg[2], dj_qreg[5])
qc.ccx(dj_qreg[0], dj_qreg[2], dj_qreg[5])
qc.cx(dj_qreg[6], dj_qreg[5])
qc.ccx(dj_qreg[2], dj_qreg[5], dj_qreg[6])
qc.rz(0.2728, dj_qreg[4])
qc.rz(1.2355, dj_qreg[6])
qc.crx(0.6357, dj_qreg[1], dj_qreg[3])
qc.iswap(dj_qreg[5], dj_qreg[4])
qc.h([dj_qreg[0], dj_qreg[1], dj_qreg[2], dj_qreg[3], dj_qreg[4], dj_qreg[5], dj_qreg[6], dj_qreg[7]])  # 输入比特再次 Hadamard
qc.measure(dj_qreg[0], dj_creg[0])
qc.measure(dj_qreg[1], dj_creg[1])
qc.measure(dj_qreg[2], dj_creg[2])
qc.measure(dj_qreg[3], dj_creg[3])
qc.measure(dj_qreg[4], dj_creg[4])
qc.measure(dj_qreg[5], dj_creg[5])
qc.measure(dj_qreg[6], dj_creg[6])
qc.measure(dj_qreg[7], dj_creg[7])

# 执行模拟器并获取测量结果
backend = Aer.get_backend('aer_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
dj_result = job.result().get_counts()

# 提取前 4 位作为 Deutsch-Jozsa 判定依据
dj_only_result = {k[:4]: v for k, v in dj_result.items()}
print('Deutsch-Jozsa 结果 (前4位):', dj_only_result)
if list(dj_only_result.keys()) == ['0000']:
    print('❌ 被识别为恒定函数')
else:
    print('✅ 被识别为非恒定函数')