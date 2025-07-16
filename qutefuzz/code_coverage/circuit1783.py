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
subcirc0.rz(-0.734000, qreg_0[2])
subcirc0.x(qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.523000, qreg_1[0])
subcirc1.ry(0.697000, qreg_1[1])
subcirc1.cx(qreg_0[0],qreg_1[1])
subcirc1.cx(qreg_0[0],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.825000, qreg_0[3])
subcirc2.ry(0.535000, qreg_0[2])
subcirc2.rz(-0.653000, qreg_0[2])
subcirc2.cx(qreg_0[2],qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.x(qreg_0[2])
subcirc3.ry(0.435000, qreg_0[0])
subcirc3.cx(qreg_0[3],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.ry(0.614000, 0)
main_circ.ry(param_3, 3)
main_circ.cx(3,0)
main_circ.x(0)
main_circ.rz(param_0, 2)
main_circ.ry(-0.331000, 3)
main_circ.x(2)
main_circ.x(0)
main_circ.cx(1,0)
main_circ.ry(-0.670000, 3)
main_circ.x(0)
main_circ.rz(param_0, 3)
main_circ.rz(param_2, 0)
main_circ.x(2)
main_circ.cx(1,0)
main_circ.x(3)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.rz(param_0, 1)
main_circ.rz(param_2, 3)
main_circ.rz(param_3, 2)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.append(subcirc1,[2,1,0,3])
main_circ.cx(1,3)
main_circ.ry(param_3, 0)
main_circ.cx(1,2)
main_circ.cx(3,0)
main_circ.cx(3,1)
main_circ.cx(2,0)
main_circ.rz(0.763000, 3)
main_circ.rz(0.452000, 0)
main_circ.x(0)
main_circ.x(2)
main_circ.ry(param_2, 1)
main_circ.x(3)
main_circ.cx(3,1)
main_circ.cx(0,1)
main_circ.rz(-0.080000, 0)
main_circ.ry(-0.886000, 0)
bindings = {param_0: 0.757000, param_2: -0.749000, param_3: 0.355000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
