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
subcirc0.u(-0.441000,-0.723000,0.340000, qreg_1[0])
subcirc0.u(-0.297000,-0.816000,0.694000, qreg_1[1])
subcirc0.u(-0.335000,-0.025000,-0.889000, qreg_1[0])
subcirc0.ry(0.453000, qreg_1[0])
subcirc0.cy(qreg_0[0],qreg_1[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1.ry(-0.727000, qreg_0[0])
subcirc1.ry(-0.670000, qreg_3[0])
subcirc1.ry(0.502000, qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_0[3])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[3])
subcirc2.ry(0.649000, qreg_0[1])
subcirc2.x(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.244000, qreg_0[0])
subcirc3.ry(-0.971000, qreg_0[0])
subcirc3.u(0.262000,-0.272000,0.278000, qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.ry(-0.147000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0.877000,-0.686000,-0.634000, qreg_0[0])
subcirc4.x(qreg_0[2])
subcirc4.cy(qreg_0[1],qreg_0[3])
subcirc4.x(qreg_0[3])
subcirc4.u(0.056000,0.784000,-0.324000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(param_2, 3)
main_circ.ry(0.096000, 1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.append(subcirc1,[2,1,0,3])
with else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(2)
		main_circ.append(subcirc1,[2,1,0,3])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(3)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0.166000,0.533000,0.108000, 1)
			main_circ.x(1)
			main_circ.cy(1,0)
			main_circ.append(subcirc4,[3,2,0,1])
		with case_1(1):
			main_circ.x(3)
			main_circ.u(param_0,-0.905000,0.530000, 0)
			main_circ.u(param_1,-0.147000,-0.929000, 3)
			main_circ.cy(3,1)
with else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(3)
		main_circ.append(subcirc4,[2,3,0,1])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc1,[2,3,0,1])
main_circ.cy(3,0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[2,1,3,0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.cy(3,1)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(1,3)
		main_circ.cy(0,2)
		main_circ.cy(3,1)
	with else_1:
		main_circ.append(subcirc1,[1,0,3,2])
with else_2:
	main_circ.append(subcirc3,[0,1,2,3])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.x(0)
	with else_1:
		main_circ.u(param_2,0.076000,param_0, 0)
		main_circ.id(2)
	main_circ.id(3)
with else_2:
	main_circ.barrier(1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(1,3)
		main_circ.barrier(1)
	with else_1:
		main_circ.barrier(1)
bindings = {param_0: -0.056000, param_1: 0.600000, param_2: 0.150000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1466")
