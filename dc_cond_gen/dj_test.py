from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer

dj_qreg = QuantumRegister(9)  # 8 输入 + 1 辅助
dj_creg = ClassicalRegister(2)
qc = QuantumCircuit(dj_qreg, dj_creg)

qc.x(dj_qreg[8])  # 将辅助比特初始化为 |1⟩
qc.h([dj_qreg[0], dj_qreg[1], dj_qreg[2], dj_qreg[3], dj_qreg[4], dj_qreg[5], dj_qreg[6], dj_qreg[7], dj_qreg[8]])  # 所有量子比特 Hadamard
# === Oracle 主体部分 ===
qc.cx(dj_qreg[0], dj_qreg[8])  # 非恒定函数：控制比特 0
# === Oracle 增强部分（不影响 DJ 区） ===
qc.crx(1.0025, dj_qreg[4], dj_qreg[2])
qc.iswap(dj_qreg[5], dj_qreg[6])
qc.crx(2.6075, dj_qreg[6], dj_qreg[5])
qc.iswap(dj_qreg[3], dj_qreg[6])
qc.cx(dj_qreg[4], dj_qreg[5])
qc.crx(0.2105, dj_qreg[6], dj_qreg[5])
qc.cx(dj_qreg[5], dj_qreg[2])
qc.cx(dj_qreg[6], dj_qreg[4])
qc.h([dj_qreg[0], dj_qreg[1]])  # 输入比特再次 Hadamard
qc.cx(dj_qreg[0], dj_qreg[3])
qc.cx(dj_qreg[1], dj_qreg[4])
qc.measure(dj_qreg[3], dj_creg[0])
qc.measure(dj_qreg[4], dj_creg[1])

# 执行模拟器并获取测量结果
backend = Aer.get_backend('aer_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
dj_result = job.result().get_counts()

# 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据
dj_only_result = {k[:2]: v for k, v in dj_result.items()}
print('Deutsch-Jozsa 结果 (前 dj_bits 位):', dj_only_result)
if sorted(dj_only_result.keys()) == ['00']:
    print('❌ 被识别为恒定函数')
else:
    print('✅ 被识别为非恒定函数')