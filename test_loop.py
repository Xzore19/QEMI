from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

qreg = QuantumRegister(7)
creg = ClassicalRegister(5)
temp_creg = ClassicalRegister(2)
qc = QuantumCircuit(qreg, creg, temp_creg)
qc.x(5)
qc.x(6)
qc.measure(qreg[5], temp_creg[0])
qc.measure(qreg[6], temp_creg[1])

#########################################################################
with qc.while_loop((temp_creg, 0b00)):
    qc.x(0)
#########################################################################

simulator = Aer.get_backend("aer_simulator")
p = PassManager(RemoveFinalMeasurements())
qc = p.run(qc)

qc.measure_all()

compiled_circuit = transpile(qc, backend=simulator, optimization_level=3, routing_method="sabre",
                             layout_method="noise_adaptive", approximation_degree=1)
job = simulator.run(compiled_circuit, shots=10000)
# result = job.result().get_counts()
# print(result)