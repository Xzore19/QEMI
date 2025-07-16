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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cz(qreg_2[1],qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_1[0])
subcirc0.cy(qreg_0[0],qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.164000, qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.cy(qreg_3[0],qreg_0[2])
subcirc1.rz(0.595000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.138000, qreg_3[0])
subcirc2.rz(0.877000, qreg_2[0])
subcirc2.u(pi/2,0.044000,0.897000, qreg_0[0])
subcirc2.u(pi/2,0.666000,-0.305000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cy(qreg_1[0],qreg_2[0])
subcirc3.cz(qreg_2[0],qreg_3[0])
subcirc3.rz(0.597000, qreg_3[0])
subcirc3.cz(qreg_3[0],qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.cy(qreg_0[0],1)
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.append(subcirc2,[0,qreg_0[2],1,qreg_0[0],qreg_0[1]])
main_circ.rz(param_2, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[2],0,qreg_0[1],1])
main_circ.cy(0,qreg_0[3])
main_circ.rz(param_0, qreg_0[3])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],1,0,qreg_0[1]])
main_circ.rz(param_1, qreg_0[2])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.append(subcirc3,[qreg_0[0],1,qreg_0[2],qreg_0[1]])
main_circ.rz(0.515000, 0)
main_circ.append(subcirc3,[qreg_0[2],0,qreg_0[0],1])
main_circ.cz(0,1)
main_circ.append(subcirc3,[qreg_0[2],1,0,qreg_0[0]])
main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.rz(param_2, qreg_0[0])
main_circ.cy(qreg_0[0],0)
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3],0])
main_circ.rz(-0.140000, 0)
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],0,qreg_0[3],qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[1],1,qreg_0[3],qreg_0[2]])
main_circ.cz(1,qreg_0[1])
bindings = {param_0: 0.835000, param_1: 0.077000, param_2: 0.977000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
