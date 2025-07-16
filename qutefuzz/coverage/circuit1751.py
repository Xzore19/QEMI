from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(0,0,-0.661000, qreg_1[0])
subcirc0.h(qreg_1[2])
subcirc0.u(0,0,-0.884000, qreg_1[0])
subcirc0.h(qreg_1[1])
subcirc0.u(0,0,-0.946000, qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,0.459000, qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.h(qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_0[2])
subcirc2.u(0,0,-1.000000, qreg_0[1])
subcirc2.u(0,0,-0.015000, qreg_0[1])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.h(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[2])
subcirc3.s(qreg_0[3])
subcirc3.h(qreg_0[1])
subcirc3.u(0,0,-0.205000, qreg_0[0])
subcirc3.cy(qreg_0[3],qreg_0[1])

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

main_circ.u(param_2,param_0,param_1, 2)
main_circ.u(0,param_1,0.902000, 0)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.cy(0,1)
main_circ.u(param_1,0,0.288000, 2)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.u(0,0,param_1, 2)
main_circ.cy(2,1)
main_circ.h(3)
main_circ.cy(3,1)
main_circ.append(subcirc1,[2,3,1,0])
main_circ.u(0,0,param_0, 1)
main_circ.u(param_1,0,param_1, 1)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.h(1)
main_circ.cy(0,3)
main_circ.u(param_2,param_1,0.236000, 0)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.cy(0,3)
main_circ.cy(0,2)
main_circ.cy(2,1)
main_circ.cy(2,1)
main_circ.cy(2,0)
main_circ.cy(3,1)
main_circ.cy(1,0)
main_circ.s(1)
main_circ.append(subcirc1,[2,0,1,3])
main_circ.u(0,0,-0.949000, 2)
bindings = {param_0: -0.563000, param_1: 0.668000, param_2: -0.388000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1751")
