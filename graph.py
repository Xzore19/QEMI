from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')

# 量子传态电路：3个量子比特和3个经典比特
qc = QuantumCircuit(3, 3)

# 量子态准备：将第一个量子比特置于任意态（例如：Hadamard）
qc.h(0)
qc.barrier()

# 创建纠缠对
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Bell测量
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# 测量前两个比特
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()

# 根据测量结果执行经典控制操作
qc.cx(1, 2)
qc.cz(0, 2)

# 测量最终量子比特
qc.measure(2, 2)
#
# qc.draw("mpl")
#
# plt.show()

# # 绘制高清电路图
image = qc.draw('latex')

image.show()

# plt.savefig('quantum_circuit.png')