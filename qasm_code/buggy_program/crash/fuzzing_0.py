from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister 
from qiskit_aer import Aer 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.circuit import Parameter, ParameterVector 
from qiskit.circuit.library import XGate 
from qiskit.transpiler.passes import * 
from qiskit.circuit.library import * 
from qiskit.transpiler import PassManager, generate_preset_pass_manager 
from math import pi 
import numpy as np 
np.random.seed(42) 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.swap(2, 1)
qc.ch(2, 0)
qc.y(4)
qc.t(0)
qc.swap(3, 2)

qr_8cf2c4 = QuantumRegister(2)
cr_8cf2c4 = ClassicalRegister(2)
qc.add_register(qr_8cf2c4)
qc.add_register(cr_8cf2c4)
qc.x(qr_8cf2c4[0])
qc.x(qr_8cf2c4[1])
qc.measure(qr_8cf2c4[0], cr_8cf2c4[0]) 
qc.measure(qr_8cf2c4[1], cr_8cf2c4[1]) 
with qc.while_loop((cr_8cf2c4, 0b10)): 
	a = 0
	with qc.for_loop(range(a)) as i_1b1d12:
		qc.cswap(4, 2, 1)
		qc.swap(1, 0)
		qc.rz(0.39269908169872414, 0)
		qc.rx(0.7853981633974483, 1)
		qc.z(3)
	
	qc.measure(qr_8cf2c4[0], cr_8cf2c4[0]) 
	qc.measure(qr_8cf2c4[1], cr_8cf2c4[1]) 
qc.reset(qr_8cf2c4)
qc.cz(0, 3)
qc.ch(2, 0)
qc.rx(1.5707963267948966, 1)
qc.cx(2, 0)
qc.h(4)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


