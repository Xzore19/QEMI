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
subcirc0.h(qreg_3[0])
subcirc0.rx(0.632000, qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.rx(-0.996000, qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.z(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_2[0])
subcirc1.z(qreg_0[1])
subcirc1.rx(-0.008000, qreg_2[0])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_2[0])
subcirc1.h(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[3])
subcirc2.x(qreg_0[3])
subcirc2.z(qreg_0[1])
subcirc2.rx(-0.940000, qreg_0[3])
subcirc2.rx(-0.451000, qreg_0[1])
subcirc2.rx(0.531000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.x(qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.h(0)
main_circ.z(qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_3[0],qreg_2[0],qreg_0[1]])
main_circ.z(0)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.rx(param_1, qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.z(0)
main_circ.append(subcirc1,[qreg_2[0],0,qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_2[0]])
main_circ.z(qreg_2[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_2[0],qreg_0[1],qreg_0[0],0])
main_circ.x(0)
main_circ.x(qreg_3[0])
main_circ.rx(-0.272000, 0)
main_circ.rx(0.111000, qreg_2[0])
main_circ.z(qreg_0[0])
main_circ.x(qreg_2[0])
bindings = {param_1: -0.170000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
