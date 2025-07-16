from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_1[0])
subcirc0.u(0.451000,0.730000,-0.395000, qreg_2[1])
subcirc0.s(qreg_2[1])
subcirc0.rz(-0.551000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.749000, qreg_0[3])
subcirc1.z(qreg_0[0])
subcirc1.s(qreg_0[3])
subcirc1.u(0.577000,0.171000,0.240000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.rz(0.583000, qreg_1[1])
subcirc2.rz(0.869000, qreg_1[0])
subcirc2.rz(0.238000, qreg_1[1])
subcirc2.rz(0.494000, qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.z(3)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.z(3)
main_circ.append(subcirc1,[qreg_0[0],0,2,3])
main_circ.z(qreg_0[0])
main_circ.u(param_2,0.981000,0.339000, 2)
main_circ.append(subcirc0,[3,2,1,qreg_1[0]])
main_circ.append(subcirc0,[qreg_0[0],0,2,1])
main_circ.z(qreg_0[0])
main_circ.z(2)
main_circ.rz(-0.914000, 3)
main_circ.u(param_2,0.682000,0.342000, 2)
main_circ.s(1)
main_circ.append(subcirc2,[1,qreg_0[0],qreg_1[0],0])
main_circ.append(subcirc0,[0,qreg_0[0],3,qreg_1[0]])
main_circ.s(1)
main_circ.append(subcirc2,[0,1,3,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],0,3,1])
main_circ.s(qreg_1[0])
main_circ.z(2)
main_circ.z(0)
main_circ.z(3)
main_circ.u(param_1,param_0,-0.368000, qreg_1[0])
bindings = {param_0: 0.069000, param_1: -0.391000, param_2: 0.987000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1917")
