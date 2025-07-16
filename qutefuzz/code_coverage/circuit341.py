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
subcirc0.rz(-0.547000, qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0.ry(0.053000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.s(qreg_1[1])
subcirc1.ry(-0.961000, qreg_0[0])
subcirc1.rz(-0.628000, qreg_0[0])
subcirc1.rx(0.075000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.rz(-0.430000, qreg_1[0])
subcirc2.rz(0.051000, qreg_0[0])
subcirc2.s(qreg_1[2])
subcirc2.s(qreg_1[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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
param_4 = Parameter("param_4")

main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_2[1],0])
main_circ.s(0)
main_circ.append(subcirc0,[0,qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,qreg_2[0]])
main_circ.ry(0.512000, qreg_0[1])
main_circ.rx(0.579000, 0)
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.rz(0.016000, qreg_2[0])
main_circ.rx(-0.918000, qreg_2[1])
main_circ.rz(param_2, qreg_0[0])
main_circ.s(0)
main_circ.rx(0.160000, qreg_2[0])
main_circ.s(qreg_2[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],qreg_2[0],0])
main_circ.rz(param_1, qreg_2[0])
main_circ.append(subcirc2,[qreg_2[1],0,qreg_2[0],qreg_0[0]])
main_circ.rz(param_3, qreg_0[1])
main_circ.ry(0.010000, qreg_0[0])
main_circ.s(qreg_2[1])
bindings = {param_1: 0.545000, param_2: 0.247000, param_3: -0.659000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "341")
