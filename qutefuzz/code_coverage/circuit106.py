from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_3[0],qreg_1[1])
subcirc0.ry(0.670000, qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.cy(qreg_1[1],qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_2[0],qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_2[0])
subcirc1.ry(-0.636000, qreg_0[1])

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

main_circ.u(param_0,param_0,param_0, 1)
main_circ.append(subcirc1,[2,qreg_1[0],1,0])
main_circ.y(qreg_1[0])
main_circ.u(0,param_1,0.971000, 0)
main_circ.u(param_0,0,-0.582000, qreg_1[0])
main_circ.y(qreg_0[0])
main_circ.u(0,0,param_0, 0)
main_circ.y(qreg_1[0])
main_circ.cy(2,1)
main_circ.y(qreg_1[0])
main_circ.u(param_2,param_1,-0.580000, 3)
main_circ.append(subcirc1,[0,qreg_0[0],qreg_1[0],2])
main_circ.append(subcirc1,[1,3,0,2])
main_circ.append(subcirc0,[0,qreg_1[0],1,2,qreg_0[0]])
main_circ.cy(qreg_1[0],3)
main_circ.u(0,param_0,param_1, qreg_1[0])
main_circ.y(3)
main_circ.append(subcirc0,[3,2,qreg_1[0],0,qreg_0[0]])
main_circ.cy(0,3)
main_circ.append(subcirc0,[qreg_0[0],0,1,2,3])
main_circ.ry(param_2, 1)
main_circ.y(0)
main_circ.y(0)
main_circ.append(subcirc1,[qreg_0[0],2,0,qreg_1[0]])
main_circ.cy(qreg_1[0],3)
main_circ.cy(0,2)
main_circ.cy(2,qreg_1[0])
main_circ.cy(qreg_0[0],3)
main_circ.cy(1,qreg_0[0])
main_circ.ry(param_1, 2)
main_circ.y(qreg_0[0])
main_circ.y(2)
main_circ.cy(3,2)
main_circ.append(subcirc1,[0,qreg_0[0],3,1])
main_circ.u(param_1,0,0.434000, 2)
main_circ.ry(-0.187000, 0)
bindings = {param_0: 0.738000, param_1: 0.523000, param_2: 0.461000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
