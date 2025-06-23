from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.circuit.library import *
from qiskit.transpiler import PassManager
import numpy as np

np.random.seed(42)

qreg = QuantumRegister(4)
creg = ClassicalRegister(4)
qc = QuantumCircuit(qreg, creg)

qc.ch(2, 1) # this line
qc.z(2) # this line
qc.rx(0.39269908169872414, 0) # this line
qc.ch(3, 0) # this line
qc.crx(0.7853981633974483, 0, 3) # this line

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc.add_register(qr)
qc.add_register(cr)
qc.h(qr[0]) 
qc.cx(qr[0], qr[1]) 
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])

simulator = Aer.get_backend("aer_simulator")

p = PassManager([Collect2qBlocks(), TemplateOptimization(), ConsolidateBlocks()])
qc = p.run(qc)

compiled_circuit = transpile(qc, backend=simulator)


job = simulator.run(compiled_circuit, shots=500)
result = job.result().get_counts()
print(result)
