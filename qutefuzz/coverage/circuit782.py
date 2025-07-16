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
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0.rz(0.607000, qreg_3[0])
subcirc0.rz(0.517000, qreg_1[0])
subcirc0.x(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.rz(-0.045000, qreg_0[3])
subcirc1.rz(1.000000, qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_2[0])
subcirc2.rz(0.679000, qreg_2[0])
subcirc2.x(qreg_2[1])
subcirc2.rz(-0.112000, qreg_0[0])
subcirc2.rz(-0.079000, qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_2[0])
subcirc3.z(qreg_1[0])
subcirc3.x(qreg_2[1])
subcirc3.rz(-0.158000, qreg_1[0])
subcirc3.cz(qreg_2[0],qreg_2[1])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.append(subcirc3,[qreg_0[1],2,0,qreg_0[0],1])
main_circ.append(subcirc2,[3,0,1,2])
main_circ.append(subcirc3,[3,2,qreg_0[0],1,qreg_0[1]])
main_circ.append(subcirc0,[3,1,qreg_0[1],2,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[1],2,0,3])
main_circ.append(subcirc0,[2,3,qreg_0[0],0,1])
main_circ.z(qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[0,qreg_0[0],2,3,qreg_0[1]])
main_circ.append(subcirc3,[3,qreg_0[0],1,0,qreg_0[1]])
main_circ.cz(3,2)
main_circ.cz(qreg_0[1],0)
main_circ.cz(2,3)
main_circ.cz(1,qreg_0[1])
main_circ.cz(3,2)
main_circ.cz(2,qreg_0[0])
main_circ.cz(1,3)
main_circ.cz(2,qreg_0[1])
main_circ.cz(qreg_0[1],3)
main_circ.cz(2,qreg_0[0])
main_circ.z(3)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
