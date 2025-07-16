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
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.rz(0.248000, qreg_0[2])
subcirc0.cx(qreg_0[0],qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.cx(qreg_0[2],qreg_0[1])
	main_circ.rz(-0.204000, qreg_3[0])
	main_circ.rz(0.900000, qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(qreg_0[0],qreg_0[2])
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
with else_1:
	main_circ.rz(param_2, qreg_3[0])
	main_circ.cx(qreg_3[0],qreg_0[1])
	main_circ.cx(qreg_0[0],qreg_0[1])
	main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(qreg_0[0])
	main_circ.cx(qreg_0[0],qreg_3[0])
	main_circ.y(qreg_0[0])
with else_1:
	main_circ.cx(qreg_3[0],qreg_0[0])
	main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_3[0])
	main_circ.rz(-0.224000, qreg_3[0])
	main_circ.y(qreg_3[0])
	main_circ.y(qreg_0[2])
with else_1:
	main_circ.barrier(qreg_0[1])
bindings = {param_2: -0.851000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1828", "CommutativeCancellation")
