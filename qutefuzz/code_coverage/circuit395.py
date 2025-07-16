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
subcirc0.u(pi/2,0.314000,-0.397000, qreg_1[1])
subcirc0.h(qreg_0[0])
subcirc0.x(qreg_1[1])
subcirc0.cx(qreg_1[1],qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[2])
subcirc1.u(pi/2,-0.323000,0.379000, qreg_0[3])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.h(qreg_2[0])
subcirc2.cx(qreg_2[1],qreg_0[1])
subcirc2.x(qreg_2[1])
subcirc2.u(pi/2,0.912000,0.362000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.x(qreg_1[0])
main_circ.append(subcirc0,[2,1,3,qreg_0[0]])
main_circ.cx(2,0)
main_circ.append(subcirc2,[3,qreg_1[0],0,2,qreg_0[0],1])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.append(subcirc2,[1,0,qreg_1[0],2,3,qreg_0[0]])
main_circ.x(1)
main_circ.append(subcirc0,[3,qreg_0[0],1,qreg_1[0]])
main_circ.h(2)
main_circ.u(pi/2,0.350000,0.380000, 0)
main_circ.cx(2,qreg_1[0])
main_circ.u(pi/2,param_6,param_6, 2)
main_circ.cx(1,3)
main_circ.u(pi/2,param_0,param_3, 1)
main_circ.append(subcirc1,[1,qreg_0[0],2,3])
main_circ.h(3)
main_circ.x(3)
main_circ.cx(qreg_0[0],2)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.cx(0,qreg_1[0])
main_circ.cx(qreg_1[0],0)
main_circ.cx(0,2)
main_circ.cx(qreg_1[0],3)
main_circ.h(1)
main_circ.cx(3,0)
main_circ.append(subcirc1,[2,qreg_0[0],qreg_1[0],0])
main_circ.x(3)
main_circ.h(3)
main_circ.h(3)
main_circ.x(qreg_1[0])
bindings = {param_0: 0.854000, param_3: 0.294000, param_6: 0.354000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
