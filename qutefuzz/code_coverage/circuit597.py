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
subcirc0.rz(0.934000, qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[3])
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[3])
subcirc1.s(qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.295000, qreg_2[0])
subcirc2.s(qreg_2[0])
subcirc2.cy(qreg_2[0],qreg_0[0])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cy(qreg_0[1],qreg_3[0])
subcirc3.rz(-0.257000, qreg_2[0])
subcirc3.h(qreg_2[0])
subcirc3.s(qreg_0[0])
subcirc3.h(qreg_3[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rz(-0.217000, qreg_0[1])
subcirc4.s(qreg_0[2])
subcirc4.s(qreg_0[0])
subcirc4.cy(qreg_0[0],qreg_0[3])
subcirc4.rz(-0.512000, qreg_0[3])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.h(qreg_0[0])
main_circ.cy(qreg_0[0],qreg_2[1])
main_circ.s(qreg_2[1])
main_circ.rz(0.248000, qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.s(qreg_2[1])
main_circ.append(subcirc1,[qreg_1[0],qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.s(qreg_1[0])
main_circ.s(qreg_2[0])
main_circ.h(qreg_2[1])
main_circ.h(qreg_2[1])
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.h(qreg_2[1])
main_circ.rz(0.559000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],qreg_2[1],qreg_2[0]])
main_circ.rz(param_0, qreg_2[1])
main_circ.h(qreg_1[0])
main_circ.h(qreg_2[0])
main_circ.cy(qreg_2[0],qreg_0[0])
main_circ.cy(qreg_1[0],qreg_2[0])
main_circ.h(qreg_1[0])
main_circ.h(qreg_2[0])
main_circ.cy(qreg_0[0],qreg_2[1])
main_circ.rz(0.485000, qreg_1[0])
main_circ.rz(-0.497000, qreg_2[1])
main_circ.s(qreg_2[1])
main_circ.s(qreg_2[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],qreg_2[0],qreg_2[1]])
main_circ.h(qreg_1[0])
main_circ.s(qreg_2[0])
bindings = {param_0: 0.074000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "597")
