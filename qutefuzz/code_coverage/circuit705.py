from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
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

main_circ.cx(qreg_3[0],qreg_2[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_2[0],qreg_0[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(param_0,param_0,0.817000, qreg_3[0])
					main_circ.cx(0,qreg_3[0])
					main_circ.u(param_0,0,0.564000, qreg_2[0])
					main_circ.cx(qreg_0[1],0)
				with else_1:
					main_circ.cx(qreg_3[0],0)
					main_circ.ry(0.529000, qreg_3[0])
					main_circ.ry(param_0, qreg_0[0])
					main_circ.ry(-0.282000, 0)
					main_circ.y(qreg_0[1])
	with case_4(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_0,0,param_0, 0)
							main_circ.y(qreg_3[0])
							main_circ.ry(0.507000, qreg_0[1])
							main_circ.u(param_0,param_0,0.017000, qreg_0[1])
						with case_1(1):
							main_circ.u(0,param_0,param_0, qreg_0[0])
							main_circ.u(param_0,0,param_0, qreg_0[1])
							main_circ.cx(qreg_2[0],qreg_0[1])
							main_circ.cx(qreg_0[0],0)
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.cx(qreg_0[0],qreg_3[0])
						main_circ.u(0,0,param_0, qreg_3[0])
						main_circ.cx(qreg_0[0],qreg_3[0])
						main_circ.u(0,0,-0.795000, qreg_2[0])
						main_circ.cx(qreg_0[0],0)
					with else_1:
						main_circ.cx(qreg_0[0],qreg_3[0])
						main_circ.y(qreg_0[1])
						main_circ.cx(qreg_0[0],qreg_0[1])
						main_circ.u(param_0,param_0,0.344000, qreg_0[1])
		with else_3:
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.cx(qreg_0[0],qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.cx(0,qreg_2[0])
						main_circ.cx(0,qreg_3[0])
						main_circ.y(qreg_2[0])
						main_circ.ry(-0.104000, qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.u(0,param_0,0.056000, qreg_3[0])
							main_circ.u(0,0,param_0, qreg_0[0])
							main_circ.y(0)
							main_circ.cx(qreg_0[1],0)
						with case_1(1):
							main_circ.u(param_0,param_0,param_0, qreg_3[0])
							main_circ.ry(param_0, qreg_3[0])
							main_circ.ry(-0.020000, qreg_0[0])
							main_circ.ry(param_0, 0)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.y(qreg_0[1])
				main_circ.cx(qreg_3[0],qreg_0[0])
				main_circ.ry(param_0, qreg_3[0])
			with else_1:
				main_circ.ry(param_0, qreg_2[0])
				main_circ.u(param_0,param_0,param_0, qreg_3[0])
				main_circ.ry(param_0, qreg_3[0])
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, qreg_2[0])
				main_circ.y(0)
				main_circ.u(param_0,0,0.877000, qreg_0[1])
				main_circ.u(param_0,0,param_0, qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(param_0, qreg_3[0])
				main_circ.cx(qreg_0[0],qreg_2[0])
				main_circ.cx(qreg_0[1],qreg_2[0])
				main_circ.ry(param_0, 0)
				main_circ.ry(param_0, qreg_0[0])
			with else_1:
				main_circ.u(0,param_0,param_0, qreg_0[1])
	with else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_0,param_0,param_0, qreg_3[0])
				main_circ.cx(qreg_0[1],qreg_0[0])
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(0)
			main_circ.barrier(qreg_3[0])
		with else_2:
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.381000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "705")
