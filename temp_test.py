from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister 
from qiskit.circuit import Parameter, ParameterVector 
from math import pi 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.h(4)
qc.measure(qreg[1], creg[1])
with qc.if_test((creg[1], 1)) as else_1: 
	qc.x(0)
with else_1: 
	qc.rz(0.39269908169872414, 1)

qc.x(4)
import matplotlib as plt 
qc.draw("mpl") 
plt.pyplot.show() 
