from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister 
from qiskit.circuit import Parameter, ParameterVector 
from math import pi 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.cz(1, 4)
qc.measure(qreg[2], creg[2])
with qc.if_test((creg[2], 0)) as else_1: 
	qc.rz(0.39269908169872414, 3)
with else_1: 
	qc.tdg(0)

qc.p(0.39269908169872414, 0)
import matplotlib as plt 
qc.draw("mpl") 
plt.pyplot.show() 
