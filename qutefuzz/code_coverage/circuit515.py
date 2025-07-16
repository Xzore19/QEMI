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
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.726000,0.517000, qreg_1[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.u(pi/2,-0.155000,-0.505000, qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.111000,0.417000, qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc1,[3,1,2,qreg_0[0],0])
main_circ.x(2)
main_circ.append(subcirc0,[3,1,2,0])
main_circ.append(subcirc0,[3,0,2,qreg_0[0]])
main_circ.x(3)
main_circ.append(subcirc0,[2,3,qreg_0[0],1])
main_circ.u(pi/2,-0.790000,0.817000, 3)
main_circ.append(subcirc1,[1,0,qreg_0[0],2,3])
main_circ.h(0)
main_circ.cz(1,0)
main_circ.x(0)
main_circ.cz(qreg_0[0],1)
main_circ.append(subcirc1,[3,qreg_0[0],0,1,2])
main_circ.h(1)
main_circ.u(pi/2,param_1,0.264000, 0)
main_circ.x(qreg_0[0])
main_circ.cz(1,0)
main_circ.cz(2,qreg_0[0])
main_circ.cz(3,1)
main_circ.append(subcirc0,[3,1,qreg_0[0],2])
main_circ.append(subcirc1,[3,qreg_0[0],1,0,2])
main_circ.cz(qreg_0[0],0)
main_circ.h(qreg_0[0])
main_circ.u(param_3,0.826000,param_4, 0)
bindings = {param_1: 0.833000, param_3: -0.955000, param_4: 0.227000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
