from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.008000,0.751000, qreg_0[0])
subcirc0.rz(-0.477000, qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0.u(pi/2,0.807000,0.509000, qreg_2[0])
subcirc0.z(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_2[0])
subcirc1.rz(0.452000, qreg_2[0])
subcirc1.u(pi/2,0.711000,-0.967000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(-0.056000, qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.763000, qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.cx(qreg_3[0],qreg_1[1])
subcirc2.cx(qreg_1[1],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[qreg_0[0],0,qreg_2[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[1],qreg_2[0]])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],0,qreg_1[0]])
main_circ.cx(qreg_2[1],qreg_2[0])
main_circ.u(param_1,param_0,0.554000, qreg_1[0])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_2[1],qreg_1[0]])
main_circ.cx(qreg_0[0],qreg_2[0])
main_circ.rz(0.749000, 0)
main_circ.rz(0.837000, 0)
main_circ.cx(qreg_0[0],qreg_2[0])
main_circ.append(subcirc1,[0,qreg_2[1],qreg_2[0],qreg_1[0]])
main_circ.cx(qreg_0[0],qreg_2[1])
main_circ.cx(qreg_2[0],qreg_1[0])
main_circ.cx(qreg_2[0],qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_2[1],0)
main_circ.z(qreg_1[0])
main_circ.z(0)
main_circ.cx(qreg_0[0],qreg_2[0])
bindings = {param_0: -0.835000, param_1: 0.139000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
