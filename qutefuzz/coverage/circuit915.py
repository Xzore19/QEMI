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
subcirc0.u(-0.174000,0.356000,-0.505000, qreg_0[0])
subcirc0.cy(qreg_1[0],qreg_1[1])
subcirc0.rz(0.096000, qreg_3[0])
subcirc0.u(0.057000,0.550000,0.917000, qreg_1[1])
subcirc0.u(0,0,0.468000, qreg_1[0])
subcirc0.cy(qreg_0[0],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0,0,-0.786000, qreg_1[2])
subcirc1.cy(qreg_1[1],qreg_1[2])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.cy(qreg_1[2],qreg_1[0])
subcirc1.rz(0.584000, qreg_1[0])
subcirc1.u(0,0,-0.490000, qreg_1[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.416000, qreg_1[0])
subcirc2.rz(-0.635000, qreg_1[1])
subcirc2.u(0,0,0.563000, qreg_0[0])
subcirc2.u(0.768000,0.882000,-0.794000, qreg_1[1])
subcirc2.rz(0.299000, qreg_0[0])
subcirc2.cy(qreg_0[0],qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(-0.298000, qreg_0[2])
subcirc3.u(0.813000,-0.727000,-0.393000, qreg_0[2])
subcirc3.u(0.857000,-0.508000,0.955000, qreg_0[3])
subcirc3.u(0,0,0.229000, qreg_0[0])
subcirc3.rz(0.690000, qreg_0[1])
subcirc3.cy(qreg_0[1],qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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

main_circ.append(subcirc0,[qreg_1[2],0,qreg_1[0],qreg_0[0]])
main_circ.rz(param_3, qreg_1[2])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_1[2],0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],0,qreg_1[0]])
main_circ.append(subcirc2,[0,qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_1[1],qreg_1[2]])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[2],qreg_1[1],0])
main_circ.cy(qreg_1[2],0)
main_circ.cy(qreg_1[2],qreg_1[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],0,qreg_1[2]])
bindings = {param_3: 0.381000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
