from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from collections import Counter

# Grover 算法 - 量子位数: 6
# Grover 迭代次数（最优）: 6
# 理论单次查询成功率（n=6, r=6）: 0.9966
# 为达到 99.95% 置信度，需重复运行 Grover 电路 2 次（每次 shots=1）

# 目标状态（小端顺序）: '011101'

# 构造 Oracle 子电路
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.x(qreg[0])
    oracle.x(qreg[4])
    oracle.h(qreg[5])
    oracle.mcx([qreg[0], qreg[1], qreg[2], qreg[3], qreg[4]], qreg[5])
    oracle.h(qreg[5])
    oracle.x(qreg[0])
    oracle.x(qreg[4])
    return oracle.to_gate(label='Oracle')

# 构造 Diffuser 子电路
def create_diffuser(qreg):
    diffuser = QuantumCircuit(qreg, name='Diffuser')
    diffuser.h(qreg)
    diffuser.x(qreg)
    diffuser.h(qreg[5])
    diffuser.mcx([qreg[0], qreg[1], qreg[2], qreg[3], qreg[4]], qreg[5])
    diffuser.h(qreg[5])
    diffuser.x(qreg)
    diffuser.h(qreg)
    return diffuser.to_gate(label='Diffuser')

# 模拟执行
backend = Aer.get_backend('aer_simulator')
oracle_gate = create_oracle(QuantumRegister(6))
diffuser_gate = create_diffuser(QuantumRegister(6))
results = []
grdc_qreg = QuantumRegister(6)
grdc_creg = ClassicalRegister(6)
grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
grdc_qc.h(grdc_qreg)
for _ in range(6):
  grdc_qc.append(oracle_gate, qargs=grdc_qreg)
  grdc_qc.append(diffuser_gate, qargs=grdc_qreg)
  grdc_qc.measure(grdc_qreg, grdc_creg)