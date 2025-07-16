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
subcirc0.u(-0.492000,-0.463000,0.313000, qreg_3[0])
subcirc0.u(0.460000,-0.428000,-0.521000, qreg_0[0])
subcirc0.u(-0.334000,0.546000,0.086000, qreg_0[1])
subcirc0.rz(0.280000, qreg_3[0])
subcirc0.rz(-0.229000, qreg_0[2])
subcirc0.u(0.775000,-0.084000,-0.182000, qreg_0[2])
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
subcirc1.u(-0.187000,0.528000,-0.736000, qreg_1[0])
subcirc1.y(qreg_0[0])
subcirc1.rz(-0.894000, qreg_1[0])
subcirc1.y(qreg_1[1])
subcirc1.u(-0.367000,-0.534000,0.834000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.x(qreg_0[1])
subcirc2.rz(-0.335000, qreg_0[0])
subcirc2.u(0.642000,-0.586000,-0.060000, qreg_0[1])
subcirc2.x(qreg_0[2])
subcirc2.rz(0.298000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.496000, qreg_0[0])
subcirc3.y(qreg_3[0])
subcirc3.rz(0.691000, qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3.rz(-0.826000, qreg_2[0])
subcirc3.x(qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rz(param_1, qreg_0[1])
main_circ.append(subcirc0,[1,qreg_0[3],0,qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.u(param_2,param_0,-0.182000, 0)
main_circ.rz(-0.441000, 0)
main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[1],1,0])
main_circ.rz(param_0, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],1,qreg_0[2],0,qreg_0[1],qreg_0[3]])
main_circ.u(param_1,0.575000,param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],0,1,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.x(0)
main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[1],qreg_0[0],0])
main_circ.x(0)
main_circ.x(0)
main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.x(qreg_0[3])
main_circ.y(qreg_0[2])
main_circ.x(qreg_0[3])
bindings = {param_0: -0.693000, param_1: 0.800000, param_2: 0.510000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "779")
