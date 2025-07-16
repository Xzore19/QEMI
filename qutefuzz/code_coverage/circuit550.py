from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cy(qreg_0[1],qreg_0[3])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.772000, qreg_3[0])
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.u(0,0,-0.480000, qreg_0[1])
subcirc1.h(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

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
subcirc2.cy(qreg_0[0],qreg_3[0])
subcirc2.h(qreg_2[0])
subcirc2.cz(qreg_2[0],qreg_0[0])
subcirc2.cz(qreg_1[0],qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.h(qreg_0[1])
subcirc3.u(0,0,-0.192000, qreg_2[0])
subcirc3.cz(qreg_0[0],qreg_2[1])
subcirc3.h(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_2[0],qreg_1[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc2,[0,qreg_2[1],qreg_0[0],qreg_1[0]])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.cy(qreg_1[0],1)
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.append(subcirc1,[0,1,qreg_2[0],qreg_0[0],qreg_2[1],qreg_1[0]])
main_circ.append(subcirc1,[0,qreg_2[1],1,qreg_2[0],qreg_1[0],qreg_0[0]])
main_circ.cy(qreg_2[0],0)
main_circ.append(subcirc2,[1,0,qreg_2[0],qreg_1[0]])
main_circ.u(0,param_1,param_1, qreg_2[0])
main_circ.append(subcirc2,[qreg_2[0],0,qreg_0[0],qreg_1[0]])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.append(subcirc1,[0,qreg_2[1],qreg_0[0],qreg_2[0],1,qreg_1[0]])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.h(0)
main_circ.append(subcirc1,[qreg_1[0],0,qreg_0[0],qreg_2[1],qreg_2[0],1])
main_circ.u(0,param_1,-0.457000, 0)
main_circ.u(param_4,param_1,-0.347000, qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_2[0],qreg_1[0],qreg_2[1],1])
main_circ.append(subcirc2,[0,qreg_1[0],1,qreg_2[1]])
main_circ.cz(qreg_2[1],qreg_1[0])
main_circ.cy(qreg_1[0],1)
main_circ.cy(qreg_2[0],0)
main_circ.cz(qreg_2[0],qreg_2[1])
bindings = {param_1: -0.032000, param_4: 0.374000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
