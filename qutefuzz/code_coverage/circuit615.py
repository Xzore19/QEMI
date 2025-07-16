from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rz(0.663000, qreg_0[0])
subcirc0.ry(-0.029000, qreg_2[0])
subcirc0.z(qreg_3[0])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.981000, qreg_3[0])
subcirc1.ry(0.417000, qreg_3[0])
subcirc1.ry(0.170000, qreg_2[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(0.519000, qreg_3[0])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.951000, qreg_0[0])
subcirc2.rx(0.814000, qreg_0[0])
subcirc2.rx(0.501000, qreg_0[0])
subcirc2.rx(-0.328000, qreg_1[1])
subcirc2.ry(-0.926000, qreg_1[1])
subcirc2.rz(-0.237000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.rx(0.582000, qreg_2[0])
subcirc3.rx(-0.895000, qreg_2[0])
subcirc3.z(qreg_0[0])
subcirc3.rx(-0.999000, qreg_0[1])
subcirc3.z(qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(-0.317000, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.ry(0.640000, qreg_0[2])
main_circ.z(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.rz(param_0, qreg_0[0])
main_circ.rz(param_1, qreg_0[2])
main_circ.ry(param_0, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.ry(0.278000, qreg_0[2])
main_circ.ry(param_2, qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.rz(param_2, qreg_0[0])
bindings = {param_0: -0.311000, param_1: -0.836000, param_2: -0.398000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "615")
