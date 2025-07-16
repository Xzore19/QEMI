from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rz(-0.943000, qreg_0[1])
subcirc0.rz(0.586000, qreg_0[1])
subcirc0.x(qreg_2[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[0])
subcirc1.rz(0.475000, qreg_0[0])
subcirc1.s(qreg_3[0])
subcirc1.rz(0.204000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.s(0)
main_circ.append(subcirc1,[qreg_0[0],2,1,0,3])
main_circ.rz(-0.772000, 3)
main_circ.x(2)
main_circ.rz(param_0, 3)
main_circ.x(2)
main_circ.rz(0.423000, 1)
main_circ.append(subcirc1,[3,0,qreg_0[0],1,2])
main_circ.s(0)
main_circ.x(3)
main_circ.s(qreg_0[0])
main_circ.append(subcirc1,[3,0,1,2,qreg_0[0]])
main_circ.s(2)
main_circ.cx(2,3)
main_circ.append(subcirc1,[3,2,0,qreg_0[0],1])
main_circ.cx(2,0)
main_circ.cx(2,qreg_0[0])
main_circ.cx(2,0)
main_circ.cx(3,0)
main_circ.cx(0,1)
main_circ.cx(0,2)
main_circ.cx(2,3)
main_circ.cx(2,qreg_0[0])
main_circ.cx(0,2)
main_circ.s(qreg_0[0])
bindings = {param_0: -0.241000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
