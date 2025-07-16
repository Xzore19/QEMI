from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_2[0])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.rx(-0.471000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cy(qreg_1[2],qreg_1[0])
subcirc1.cy(qreg_1[1],qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.z(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.317000, qreg_0[0])
subcirc2.rx(-0.707000, qreg_3[0])
subcirc2.cx(qreg_3[0],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.append(subcirc2,[qreg_0[0],0,2,3,qreg_1[0]])
main_circ.append(subcirc2,[qreg_1[0],3,0,qreg_0[0],1])
main_circ.append(subcirc1,[1,2,3,0])
main_circ.z(2)
main_circ.append(subcirc1,[2,0,qreg_0[0],1])
main_circ.append(subcirc2,[qreg_0[0],1,qreg_1[0],0,3])
main_circ.append(subcirc2,[1,qreg_0[0],3,0,qreg_1[0]])
main_circ.rx(param_1, 1)
main_circ.append(subcirc2,[qreg_0[0],0,1,qreg_1[0],3])
main_circ.z(1)
main_circ.rx(param_2, 1)
main_circ.z(qreg_1[0])
main_circ.append(subcirc1,[0,qreg_1[0],3,1])
main_circ.cy(qreg_1[0],2)
main_circ.append(subcirc1,[1,3,0,2])
main_circ.z(qreg_1[0])
main_circ.append(subcirc1,[0,qreg_0[0],2,3])
main_circ.rx(param_2, 2)
main_circ.z(qreg_0[0])
main_circ.cy(3,qreg_0[0])
bindings = {param_1: -0.294000, param_2: -0.158000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
