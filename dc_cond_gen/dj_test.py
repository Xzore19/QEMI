from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer

dj_qreg = QuantumRegister(9)
dj_creg = ClassicalRegister(4)
qc = QuantumCircuit(dj_qreg, dj_creg)

qc.x(dj_qreg[8])
qc.h([dj_qreg[0], dj_qreg[1], dj_qreg[2], dj_qreg[3], dj_qreg[4], dj_qreg[5], dj_qreg[6], dj_qreg[7], dj_qreg[8]])
# === Oracle 主体部分（平衡函数：dot_product） ===
qc.cx(dj_qreg[2], dj_qreg[8])  # 平衡函数：x[2] ⊕ ...
# === Oracle 增强部分（不影响 DJ 区） ===
qc.iswap(dj_qreg[6], dj_qreg[4])
qc.crz(1.3888, dj_qreg[5], dj_qreg[7])
qc.iswap(dj_qreg[5], dj_qreg[6])
qc.h(dj_qreg[7])
qc.h(dj_qreg[5])
qc.rz(2.6028, dj_qreg[5])
qc.rz(1.2263, dj_qreg[6])
qc.h(dj_qreg[7])
qc.h([dj_qreg[0], dj_qreg[1], dj_qreg[2], dj_qreg[3]])
qc.measure(dj_qreg[0], dj_creg[0])
qc.measure(dj_qreg[1], dj_creg[1])
qc.measure(dj_qreg[2], dj_creg[2])
qc.measure(dj_qreg[3], dj_creg[3])

# 执行模拟器并获取测量结果
backend = Aer.get_backend('aer_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
dj_result = job.result().get_counts()

# 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据
dj_only_result = {k[:4]: v for k, v in dj_result.items()}
print('Deutsch-Jozsa 结果 (前 dj_bits 位):', dj_only_result)
if sorted(dj_only_result.keys()) == ['0000']:
    print('❌ 被识别为恒定函数')
else:
    print('✅ 被识别为非恒定函数')