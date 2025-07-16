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
subcirc0.ry(-0.918000, qreg_1[0])
subcirc0.cz(qreg_1[0],qreg_2[1])
subcirc0.ry(-0.879000, qreg_0[0])
subcirc0.ry(-0.279000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_2[1])
subcirc0.u(-0.203000,0.294000,0.415000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.007000, qreg_0[0])
subcirc1.u(0.049000,-0.903000,0.535000, qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.u(0.730000,-0.014000,-0.148000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.ry(0.852000, qreg_2[1])
subcirc2.cz(qreg_0[0],qreg_1[0])
subcirc2.cz(qreg_2[0],qreg_2[1])
subcirc2.cz(qreg_0[0],qreg_2[0])
subcirc2.x(qreg_0[0])
subcirc2.u(-0.920000,0.408000,0.786000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[3],qreg_0[0])
subcirc3.x(qreg_0[1])
subcirc3.ry(0.633000, qreg_0[2])
subcirc3.u(-0.812000,-0.164000,0.132000, qreg_0[2])
subcirc3.cz(qreg_0[0],qreg_0[2])
subcirc3.x(qreg_0[3])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.u(param_0,-0.719000,0.225000, qreg_0[0])
main_circ.ry(0.161000, qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.ry(param_2, qreg_2[0])
main_circ.u(param_0,-0.419000,param_0, qreg_2[0])
main_circ.x(qreg_2[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],qreg_3[0],qreg_0[1]])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.ry(-0.620000, qreg_2[0])
main_circ.u(-0.564000,0.335000,param_1, qreg_0[0])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.u(param_0,param_2,param_0, qreg_2[0])
main_circ.append(subcirc3,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.cz(qreg_3[0],qreg_0[1])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.ry(param_0, qreg_0[1])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.u(-0.982000,param_0,param_1, qreg_2[0])
main_circ.cz(qreg_0[0],qreg_0[1])
bindings = {param_0: 0.766000, param_1: -0.299000, param_2: 0.295000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
