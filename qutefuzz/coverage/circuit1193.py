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
subcirc0.rz(0.324000, qreg_2[0])
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.z(qreg_2[1])
subcirc0.cz(qreg_2[1],qreg_1[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cy(qreg_1[2],qreg_1[1])
subcirc1.cz(qreg_1[2],qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_1[1])
subcirc1.z(qreg_0[0])
subcirc1.cz(qreg_1[1],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.cz(qreg_0[3],qreg_0[1])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.z(qreg_0[1])
subcirc2.cy(qreg_0[0],qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_2[0])
subcirc3.rz(-0.827000, qreg_2[0])
subcirc3.rz(0.519000, qreg_2[0])
subcirc3.cy(qreg_2[0],qreg_0[1])
subcirc3.cz(qreg_2[1],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[0],qreg_3[0])
subcirc4.cy(qreg_0[0],qreg_3[0])
subcirc4.rz(0.425000, qreg_0[1])
subcirc4.cz(qreg_0[0],qreg_0[2])
subcirc4.rz(0.619000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.rz(0.127000, 0)
main_circ.append(subcirc2,[3,qreg_0[1],2,qreg_0[0]])
main_circ.cz(2,qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],1,3])
main_circ.cz(qreg_0[0],3)
main_circ.append(subcirc0,[0,1,qreg_0[0],3])
main_circ.rz(param_1, qreg_0[1])
main_circ.cz(3,0)
main_circ.append(subcirc2,[0,qreg_0[0],3,qreg_0[1]])
main_circ.append(subcirc3,[2,1,qreg_0[0],qreg_0[1],0,3])
main_circ.append(subcirc4,[0,1,qreg_0[1],qreg_0[0],2,3])
main_circ.cz(3,qreg_0[1])
main_circ.append(subcirc3,[1,qreg_0[1],0,3,2,qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[1],2,1,0])
main_circ.cy(1,2)
main_circ.rz(param_0, 3)
bindings = {param_0: 0.679000, param_1: 0.307000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1193")
