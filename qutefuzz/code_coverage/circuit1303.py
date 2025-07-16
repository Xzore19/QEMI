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
subcirc0.u(0,0,0.182000, qreg_0[1])
subcirc0.rz(-0.233000, qreg_0[0])
subcirc0.u(0,0,0.658000, qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.u(0,0,-0.893000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.214000, qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.rz(-0.593000, qreg_0[0])
subcirc1.cz(qreg_1[1],qreg_3[0])
subcirc1.y(qreg_1[0])
subcirc1.rz(0.044000, qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[2],qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.rz(-0.978000, qreg_0[0])
subcirc2.u(0,0,-0.590000, qreg_0[1])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.u(0,0,0.997000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[2,1,qreg_0[0],0,3])
main_circ.rz(0.394000, qreg_0[0])
main_circ.append(subcirc0,[1,0,2,3,qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[0],1,2,3])
main_circ.append(subcirc0,[0,3,2,qreg_0[0],1])
main_circ.u(param_0,0,-0.375000, 0)
main_circ.append(subcirc2,[3,0,1,qreg_0[0]])
main_circ.append(subcirc0,[0,3,qreg_0[0],1,2])
main_circ.cz(1,3)
main_circ.cz(2,qreg_0[0])
main_circ.cz(2,0)
main_circ.y(1)
main_circ.append(subcirc0,[1,2,qreg_0[0],3,0])
main_circ.rz(param_0, qreg_0[0])
bindings = {param_0: 0.667000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
