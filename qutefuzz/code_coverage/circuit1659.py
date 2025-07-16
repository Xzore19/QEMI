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
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.u(0,0,-0.654000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.u(0,0,-0.702000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_2[0])
subcirc1.u(0,0,0.313000, qreg_3[0])
subcirc1.x(qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.ry(0.254000, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.u(param_0,0,param_0, qreg_0[1])
main_circ.u(0,param_1,-0.984000, qreg_0[2])
main_circ.ry(param_1, qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.u(0,param_1,-0.968000, qreg_0[1])
main_circ.ry(param_1, qreg_0[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_3[0],qreg_0[1])
bindings = {param_0: -0.879000, param_1: 0.752000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
