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
subcirc0.cy(qreg_0[0],qreg_3[0])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.u(pi/2,0.322000,0.831000, qreg_3[0])
subcirc0.u(pi/2,0.873000,0.176000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_3[0],qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_2[0],qreg_0[1])
subcirc1.u(pi/2,0.673000,0.440000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.h(qreg_0[0])
subcirc2.cy(qreg_0[1],qreg_3[0])
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.u(pi/2,-0.199000,0.162000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[2])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.z(qreg_0[2])
subcirc3.h(qreg_0[3])
subcirc3.cy(qreg_0[1],qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cy(0,3)
main_circ.append(subcirc0,[qreg_0[1],2,0,qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],3,0,1,2])
main_circ.h(2)
main_circ.append(subcirc2,[1,0,3,qreg_0[1]])
main_circ.u(pi/2,-0.635000,param_2, qreg_0[0])
main_circ.u(param_0,param_1,0.418000, 3)
main_circ.cy(3,qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.cy(0,2)
main_circ.cy(2,1)
main_circ.append(subcirc0,[3,qreg_0[1],qreg_0[0],2])
main_circ.append(subcirc2,[qreg_0[0],3,1,2])
main_circ.cy(1,3)
main_circ.cy(3,1)
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],1,2])
main_circ.cy(1,2)
main_circ.append(subcirc0,[2,3,1,qreg_0[0]])
main_circ.u(param_3,0.891000,0.829000, 0)
main_circ.u(param_0,param_1,param_0, qreg_0[1])
bindings = {param_0: -0.837000, param_1: -0.770000, param_2: 0.784000, param_3: -0.840000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
