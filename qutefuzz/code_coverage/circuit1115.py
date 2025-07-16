from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.rx(param_2, qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(0.788000,param_2,-0.606000, qreg_0[1])
					main_circ.ry(param_4, qreg_2[1])
					main_circ.u(param_1,-0.829000,-0.686000, qreg_2[1])
				with else_1:
					main_circ.u(0.548000,param_4,param_4, 0)
					main_circ.cz(qreg_2[0],qreg_0[0])
			with else_2:
				main_circ.cz(qreg_2[0],1)
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_4, qreg_2[1])
					main_circ.cz(qreg_2[1],0)
					main_circ.u(-0.798000,param_3,param_3, 0)
					main_circ.u(0.033000,param_4,param_2, qreg_2[1])
		with case_3(1):
			main_circ.u(param_3,0.064000,-0.352000, qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.u(-0.733000,param_3,-0.791000, qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.ry(0.882000, qreg_0[0])
					main_circ.rx(param_4, qreg_2[1])
				with else_1:
					main_circ.u(param_0,param_2,-0.990000, 1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(qreg_2[0],1)
					main_circ.u(0.280000,0.457000,0.104000, qreg_0[0])
					main_circ.ry(param_3, qreg_0[1])
					main_circ.rx(-0.060000, qreg_2[1])
				with else_1:
					main_circ.u(-0.201000,0.766000,-0.866000, 1)
					main_circ.ry(param_4, qreg_2[1])
					main_circ.u(-0.007000,0.762000,-0.828000, 0)
					main_circ.u(0.169000,param_1,param_2, 1)
			with else_2:
				main_circ.rx(0.251000, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(0.779000,-0.271000,param_4, qreg_2[0])
						main_circ.rx(0.734000, qreg_0[0])
						main_circ.u(0.107000,param_3,-0.901000, qreg_0[0])
						main_circ.ry(param_4, qreg_0[0])
					with case_1(1):
						main_circ.u(param_3,-0.739000,param_1, qreg_2[0])
						main_circ.rx(param_4, 0)
						main_circ.rx(param_3, qreg_2[0])
						main_circ.rx(param_1, qreg_2[0])
			with case_2(1):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.cz(0,qreg_2[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(0,qreg_0[1])
					main_circ.cz(qreg_0[1],qreg_0[0])
					main_circ.cz(qreg_0[0],0)
					main_circ.cz(1,qreg_0[1])
				with else_1:
					main_circ.cz(qreg_2[0],1)
					main_circ.cz(1,qreg_2[1])
					main_circ.cz(qreg_0[1],0)
					main_circ.cz(qreg_0[1],qreg_0[0])
					main_circ.cz(qreg_0[1],qreg_2[0])
	with else_3:
		main_circ.u(0.922000,0.203000,0.110000, 0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rx(param_4, qreg_2[1])
					main_circ.ry(param_4, qreg_2[1])
					main_circ.cz(qreg_2[1],1)
					main_circ.rx(param_2, qreg_0[0])
				with case_1(1):
					main_circ.id(1)
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[1])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_2[1])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[1])
			main_circ.id(1)
with else_4:
	main_circ.id(qreg_0[1])
bindings = {param_0: 0.642000, param_1: -0.829000, param_2: 0.583000, param_3: 0.469000, param_4: 0.334000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1115", "Optimize1qGatesSimpleCommutation")
