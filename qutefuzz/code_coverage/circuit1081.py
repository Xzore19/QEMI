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
subcirc0.u(0,0,0.775000, qreg_0[1])
subcirc0.s(qreg_2[1])
subcirc0.u(pi/2,0.489000,0.138000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[2])
subcirc1.u(0,0,-0.275000, qreg_0[1])
subcirc1.u(pi/2,0.895000,0.985000, qreg_0[1])
subcirc1.u(pi/2,0.690000,-0.670000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.h(qreg_0[1])
subcirc2.h(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.s(qreg_2[1])
subcirc3.u(pi/2,-0.472000,0.074000, qreg_0[1])
subcirc3.h(qreg_0[0])
subcirc3.u(0,0,0.301000, qreg_2[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(pi/2,0.552000,0.324000, 2)
main_circ.u(pi/2,param_2,param_2, 2)
main_circ.h(0)
main_circ.s(0)
main_circ.u(param_0,0,param_0, qreg_0[0])
main_circ.s(0)
main_circ.u(param_0,-0.131000,param_0, 1)
main_circ.h(qreg_0[0])
main_circ.append(subcirc2,[0,qreg_0[0],3,1])
main_circ.append(subcirc2,[qreg_0[0],0,2,1])
main_circ.s(1)
main_circ.s(3)
main_circ.u(0,param_1,param_2, 2)
main_circ.h(qreg_0[0])
main_circ.u(param_0,0,param_2, 0)
main_circ.u(pi/2,0.657000,0.229000, 3)
main_circ.append(subcirc2,[3,1,qreg_0[0],0])
main_circ.append(subcirc2,[0,2,3,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],3,2,1])
main_circ.append(subcirc2,[1,2,0,3])
main_circ.u(0,0,param_0, 1)
main_circ.h(2)
main_circ.append(subcirc2,[qreg_0[0],0,2,1])
main_circ.u(0,param_0,0.003000, qreg_0[0])
main_circ.u(0,param_0,0.474000, qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc2,[0,2,qreg_0[0],3])
main_circ.s(1)
main_circ.h(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.h(qreg_0[0])
bindings = {param_0: 0.106000, param_1: -0.111000, param_2: -0.209000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1081")
