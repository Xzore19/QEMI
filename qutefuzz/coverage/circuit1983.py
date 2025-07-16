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
subcirc0.rx(0.520000, qreg_0[1])
subcirc0.rx(-0.515000, qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.797000, qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_2[0])
subcirc1.rx(0.508000, qreg_2[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
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
subcirc2.rz(-0.670000, qreg_0[0])
subcirc2.rz(-0.602000, qreg_1[0])
subcirc2.cz(qreg_3[0],qreg_1[0])
subcirc2.cz(qreg_0[0],qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(-0.152000, qreg_0[1])
subcirc3.cz(qreg_0[2],qreg_3[0])
subcirc3.cz(qreg_3[0],qreg_0[1])
subcirc3.rz(-0.364000, qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rz(0.648000, qreg_0[3])
subcirc4.rz(0.993000, qreg_0[3])
subcirc4.rz(-0.089000, qreg_0[0])
subcirc4.cz(qreg_0[2],qreg_0[3])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.rx(param_1, qreg_3[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.rz(param_1, qreg_1[0])
main_circ.rz(param_1, qreg_3[0])
main_circ.rz(0.785000, qreg_2[0])
main_circ.rz(0.579000, qreg_2[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_1[0]])
main_circ.z(qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],qreg_2[0],qreg_3[0],qreg_0[0]])
main_circ.z(qreg_1[0])
main_circ.rx(0.036000, qreg_3[0])
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.rx(0.737000, qreg_1[0])
main_circ.rz(param_1, qreg_1[0])
main_circ.rx(param_1, qreg_0[0])
main_circ.rz(param_0, qreg_2[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_2[0]])
main_circ.cz(qreg_3[0],qreg_1[0])
main_circ.z(qreg_1[0])
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.z(qreg_1[0])
main_circ.z(qreg_2[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[0],qreg_0[0],qreg_3[0]])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.z(qreg_1[0])
main_circ.rz(param_2, qreg_3[0])
main_circ.z(qreg_0[0])
main_circ.z(qreg_3[0])
bindings = {param_0: 0.832000, param_1: 0.764000, param_2: 0.034000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
