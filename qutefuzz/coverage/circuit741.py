from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0,0,-0.316000, qreg_0[0])
subcirc0.rz(-0.876000, qreg_2[1])
subcirc0.u(0,0,0.220000, qreg_2[1])
subcirc0.ry(-0.589000, qreg_0[1])
subcirc0.s(qreg_2[0])
subcirc0.s(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.324000, qreg_1[0])
subcirc1.u(0,0,-0.377000, qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1.u(0,0,0.247000, qreg_1[1])
subcirc1.rz(0.671000, qreg_3[0])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.442000, qreg_1[0])
subcirc2.u(0,0,0.831000, qreg_0[0])
subcirc2.ry(0.900000, qreg_1[0])
subcirc2.rz(-0.826000, qreg_2[0])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.ry(0.503000, qreg_2[0])
subcirc3.rz(-0.795000, qreg_0[0])
subcirc3.rz(-0.479000, qreg_2[1])
subcirc3.u(0,0,0.062000, qreg_0[1])
subcirc3.u(0,0,-0.451000, qreg_2[0])
subcirc3.ry(0.017000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(2)
main_circ.s(2)
main_circ.ry(param_2, 2)
main_circ.rz(0.954000, qreg_0[0])
main_circ.rz(param_0, 3)
main_circ.append(subcirc0,[2,qreg_0[0],qreg_1[0],1,3,0])
main_circ.append(subcirc2,[qreg_1[0],0,3,2])
main_circ.append(subcirc1,[2,1,qreg_1[0],qreg_0[0]])
main_circ.u(0,param_0,param_0, 1)
main_circ.append(subcirc0,[3,qreg_0[0],qreg_1[0],0,1,2])
main_circ.ry(param_1, qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],2,1,0,3])
main_circ.s(qreg_1[0])
main_circ.ry(0.796000, qreg_1[0])
main_circ.rz(-0.545000, qreg_1[0])
main_circ.s(2)
main_circ.u(0,0,-0.202000, 2)
main_circ.ry(param_1, 1)
bindings = {param_0: 0.657000, param_1: -0.594000, param_2: -0.301000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "741")
