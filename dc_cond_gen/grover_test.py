from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from collections import Counter

# Grover 算法 - 量子位数: 6
# Grover 迭代次数（最优）: 6
# 理论单次查询成功率（n=6, r=6）: 0.9966
# 为达到 99.95% 置信度，需重复运行 Grover 电路 2 次（每次 shots=1）

# 目标状态（小端顺序）: '110000'

# 构造 Oracle 子电路
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.x(qreg[2])
    oracle.x(qreg[3])
    oracle.x(qreg[4])
    oracle.x(qreg[5])
    oracle.h(qreg[5])
    oracle.mcx([qreg[0], qreg[1], qreg[2], qreg[3], qreg[4]], qreg[5])
    oracle.h(qreg[5])
    oracle.x(qreg[2])
    oracle.x(qreg[3])
    oracle.x(qreg[4])
    oracle.x(qreg[5])
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
for _ in range(2):
    qreg = QuantumRegister(6)
    creg = ClassicalRegister(6)
    qc = QuantumCircuit(qreg, creg)
    qc.h(qreg)
    for _ in range(6):
        qc.append(oracle_gate, qargs=qreg)
        qc.append(diffuser_gate, qargs=qreg)
    qc.measure(qreg, creg)
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1)
    result = job.result().get_counts()
    results.append(list(result.keys())[0])

# 统计出现最多的测量结果
freq = Counter(results)
most_common = freq.most_common(1)[0]
human_target = '000011'
print('测量结果统计:', freq)
print(f'出现次数最多的测量结果: {most_common[0]}，共出现 {most_common[1]} 次')
print(f'目标状态: {human_target}')
print(f'是否命中目标: {most_common[0] == human_target}')