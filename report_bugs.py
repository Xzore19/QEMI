from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

# 创建主寄存器
qreg = QuantumRegister(5)
creg = ClassicalRegister(5)  # 用于最终输出
cond_creg = ClassicalRegister(2)  # 专门用于 if_test 条件判断
qc = QuantumCircuit(qreg, creg, cond_creg)

# 初始化两个量子比特为 1
qc.x(qreg[0])
qc.x(qreg[1])

# 测量写入 cond_creg（作为判断用）
qc.measure(qreg[0], cond_creg[0])
qc.measure(qreg[1], cond_creg[1])

# 根据 cond_creg 是否为 0b11 决定是否对 qreg[2] 施加 H 门
with qc.if_test((cond_creg, 0b11)):
    qc.h(qreg[2])

# 最后测量所有 qreg 写入 creg，用于输出
qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])
qc.measure(qreg[4], creg[4])
#
# simulator = Aer.get_backend("aer_simulator")
#
# p = PassManager(Optimize1qGates())
# qc = p.run(qc)
#
# compiled_circuit = transpile(qc, backend=simulator, optimization_level=3)
# job = simulator.run(compiled_circuit, shots=100000)
# result = job.result().get_counts()
# print(result)

import matplotlib as plt

qc.draw("mpl")

plt.pyplot.show()