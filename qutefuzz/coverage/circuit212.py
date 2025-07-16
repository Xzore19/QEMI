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
subcirc0.rx(-0.358000, qreg_3[0])
subcirc0.ry(0.544000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.rx(-0.877000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.rx(0.067000, qreg_0[2])
subcirc1.rx(-0.961000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.998000, qreg_0[1])
subcirc2.rx(0.733000, qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.u(0,0,0.392000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.ry(0.829000, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.s(qreg_0[0])
					main_circ.rx(0.256000, qreg_0[0])
					main_circ.ry(-0.871000, 0)
					main_circ.barrier(0)
				with case_1(1):
					main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[1],0,qreg_0[2]])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rx(param_1, qreg_0[1])
				main_circ.u(0,0,0.237000, qreg_0[2])
				main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(0,param_1,param_0, qreg_0[2])
					main_circ.s(qreg_0[1])
					main_circ.ry(param_0, qreg_0[2])
					main_circ.ry(param_0, qreg_0[1])
				with case_1(1):
					main_circ.u(param_0,param_1,0.743000, qreg_0[3])
					main_circ.ry(0.104000, qreg_0[0])
					main_circ.barrier(qreg_0[3])
		with case_2(1):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rx(param_1, qreg_0[3])
			main_circ.s(qreg_0[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.u(param_0,0,0.097000, qreg_0[3])
				main_circ.rx(0.077000, qreg_0[1])
				main_circ.u(param_0,param_1,param_0, 0)
			with else_1:
				main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],0,qreg_0[1],qreg_0[3]])
				main_circ.rx(param_1, qreg_0[0])
with else_3:
	main_circ.ry(-0.120000, qreg_0[3])
	main_circ.rx(-0.298000, qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.u(0,param_1,0.450000, qreg_0[1])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3],0])
main_circ.rx(-0.892000, qreg_0[3])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[1],qreg_0[3],qreg_0[0]])
			with case_1(1):
				main_circ.barrier(qreg_0[2])
	with else_2:
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.ry(param_0, qreg_0[0])
				main_circ.id(qreg_0[3])
			with case_1(1):
				main_circ.s(qreg_0[3])
				main_circ.s(qreg_0[2])
				main_circ.id(0)
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[2])
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[3])
		with else_1:
			main_circ.id(0)
		main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.521000, param_1: 0.583000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "212", "HoareOptimizer")
