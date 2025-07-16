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
subcirc0.cy(qreg_1[0],qreg_1[1])
subcirc0.z(qreg_0[0])
subcirc0.ry(-0.129000, qreg_1[0])
subcirc0.ry(0.305000, qreg_1[1])
subcirc0.z(qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.162000, qreg_0[0])
subcirc1.u(0,0,-0.070000, qreg_2[0])
subcirc1.z(qreg_1[0])
subcirc1.ry(-0.566000, qreg_2[0])
subcirc1.z(qreg_2[0])

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
subcirc2.cy(qreg_0[0],qreg_1[0])
subcirc2.u(0,0,-0.858000, qreg_1[0])
subcirc2.ry(0.455000, qreg_2[0])
subcirc2.cy(qreg_2[0],qreg_0[0])
subcirc2.u(0,0,0.558000, qreg_0[0])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[2,1,qreg_0[0],0])
main_circ.append(subcirc2,[3,0,1,2])
main_circ.append(subcirc0,[2,1,3,0])
main_circ.append(subcirc1,[3,1,0,qreg_0[0]])
main_circ.z(0)
main_circ.ry(-0.019000, qreg_0[0])
main_circ.append(subcirc1,[3,2,0,qreg_0[0]])
main_circ.z(qreg_0[0])
main_circ.ry(-0.184000, 2)
main_circ.append(subcirc0,[qreg_0[0],3,2,0])
main_circ.append(subcirc2,[2,1,3,0])
main_circ.append(subcirc1,[qreg_0[0],2,3,0])
main_circ.cy(1,0)
main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[0],1)
main_circ.cy(3,0)
main_circ.cy(2,1)
main_circ.cy(1,0)
main_circ.cy(3,0)
main_circ.cy(qreg_0[0],3)
main_circ.cy(1,qreg_0[0])
main_circ.cy(2,0)
main_circ.u(param_2,param_4,param_2, 0)
main_circ.u(0,param_2,param_4, 1)
main_circ.z(3)
main_circ.u(0,param_4,param_0, 1)
main_circ.ry(param_2, 2)
bindings = {param_0: -0.114000, param_2: -0.433000, param_4: 0.761000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "667")
