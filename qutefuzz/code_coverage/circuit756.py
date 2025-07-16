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
subcirc0.u(0,0,0.172000, qreg_0[1])
subcirc0.cy(qreg_3[0],qreg_0[2])
subcirc0.u(0,0,0.872000, qreg_0[1])
subcirc0.u(0,0,0.298000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cy(qreg_3[0],qreg_0[2])
subcirc1.u(0,0,0.224000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.391000, qreg_0[2])
subcirc2.rz(-0.763000, qreg_0[1])
subcirc2.rz(0.339000, qreg_3[0])
subcirc2.cz(qreg_0[2],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

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

main_circ.append(subcirc0,[3,qreg_1[0],qreg_0[0],0])
main_circ.append(subcirc0,[0,3,1,qreg_0[0]])
main_circ.append(subcirc0,[1,3,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc1,[qreg_0[0],3,1,qreg_1[0]])
main_circ.append(subcirc1,[2,0,qreg_0[0],qreg_1[0]])
main_circ.u(param_0,param_1,param_0, 3)
main_circ.append(subcirc1,[2,1,qreg_1[0],qreg_0[0]])
main_circ.cy(qreg_0[0],2)
main_circ.rz(param_0, 1)
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],3,0])
main_circ.cz(3,qreg_0[0])
main_circ.cz(1,qreg_0[0])
main_circ.cz(qreg_1[0],2)
main_circ.cy(1,qreg_1[0])
main_circ.append(subcirc0,[0,2,qreg_0[0],1])
main_circ.cz(0,1)
bindings = {param_0: 0.013000, param_1: -0.240000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
