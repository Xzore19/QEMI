from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.y(qreg_3[0])
subcirc0.z(qreg_3[0])
subcirc0.z(qreg_0[0])
subcirc0.rz(-0.201000, qreg_3[0])
subcirc0.rz(-0.979000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_2[0])
subcirc1.ry(-0.505000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(0.766000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.ry(-0.467000, qreg_2[1])
subcirc2.ry(0.598000, qreg_0[1])
subcirc2.rz(0.787000, qreg_2[0])
subcirc2.y(qreg_0[1])
subcirc2.z(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_0[3])
subcirc3.rz(-0.346000, qreg_0[0])
subcirc3.rz(0.258000, qreg_0[0])
subcirc3.rz(-0.393000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(-0.272000, qreg_3[0])
subcirc4.ry(0.742000, qreg_0[2])
subcirc4.rz(-0.459000, qreg_0[0])
subcirc4.rz(0.116000, qreg_0[2])
subcirc4.y(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[3,1,0,2])
main_circ.rz(param_1, 3)
main_circ.append(subcirc2,[2,0,1,3])
main_circ.append(subcirc0,[1,0,3,2])
main_circ.rz(0.513000, 2)
main_circ.z(0)
main_circ.y(2)
main_circ.append(subcirc1,[2,3,1,0])
main_circ.append(subcirc0,[2,1,3,0])
main_circ.append(subcirc0,[1,3,2,0])
main_circ.y(0)
main_circ.y(0)
main_circ.rz(param_2, 0)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.append(subcirc2,[0,3,2,1])
main_circ.rz(param_1, 0)
main_circ.ry(param_1, 0)
main_circ.rz(-0.779000, 2)
main_circ.y(1)
main_circ.rz(0.171000, 2)
main_circ.y(0)
main_circ.ry(-0.472000, 1)
main_circ.y(0)
main_circ.y(2)
main_circ.z(2)
main_circ.rz(param_3, 1)
main_circ.ry(param_0, 1)
main_circ.ry(param_2, 3)
bindings = {param_0: 0.617000, param_1: -0.478000, param_2: -0.210000, param_3: 0.538000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
