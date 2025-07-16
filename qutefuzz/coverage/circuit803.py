from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.rx(0.762000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.h(qreg_1[2])
subcirc0.rx(-0.529000, qreg_1[1])
subcirc0.ry(-0.510000, qreg_1[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(-0.287000, qreg_0[0])
subcirc1.rx(-0.216000, qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.rx(-0.511000, qreg_2[1])
subcirc1.ry(0.153000, qreg_2[0])
subcirc1.rx(0.617000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.h(qreg_1[0])
subcirc2.rx(-0.966000, qreg_1[0])
subcirc2.ry(-0.827000, qreg_1[1])
subcirc2.rx(0.027000, qreg_1[2])
subcirc2.s(qreg_1[0])
subcirc2.ry(-0.079000, qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(-0.790000, qreg_0[1])
subcirc3.rx(-0.238000, qreg_0[3])
subcirc3.s(qreg_0[3])
subcirc3.rx(-0.513000, qreg_0[2])
subcirc3.s(qreg_0[2])
subcirc3.rx(0.357000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

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

main_circ.s(qreg_1[0])
main_circ.h(0)
main_circ.append(subcirc2,[qreg_1[0],qreg_1[2],0,qreg_0[0]])
main_circ.append(subcirc2,[0,qreg_1[2],qreg_0[0],qreg_1[1]])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_0, qreg_1[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[1],qreg_1[2],0])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[2],0,qreg_1[1]])
main_circ.s(qreg_0[0])
main_circ.ry(0.868000, 0)
main_circ.rx(0.291000, qreg_1[2])
main_circ.ry(param_1, qreg_0[0])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_1[2],qreg_1[1]])
main_circ.rx(0.379000, qreg_1[0])
main_circ.ry(param_1, qreg_1[0])
main_circ.rx(param_2, qreg_1[2])
main_circ.h(qreg_0[0])
bindings = {param_0: 0.178000, param_1: 0.439000, param_2: 0.200000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "803")
