from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(3,2)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(0,0,0.010000, 2)
			main_circ.cz(2,0)
		with else_1:
			main_circ.u(0.274000,-0.894000,param_0, 0)
			main_circ.cz(qreg_0[0],1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.s(0)
					main_circ.s(qreg_0[0])
					main_circ.u(0.901000,-0.489000,param_0, 0)
					main_circ.u(param_0,-0.009000,0.740000, qreg_0[0])
				with case_1(1):
					main_circ.cz(0,qreg_0[0])
					main_circ.u(param_0,param_0,0.684000, 0)
					main_circ.cz(1,qreg_0[0])
					main_circ.u(0.831000,-0.670000,-0.628000, 2)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(2)
				main_circ.s(1)
				main_circ.u(param_0,param_0,param_0, qreg_0[0])
				main_circ.cz(2,1)
				main_circ.u(0.961000,param_0,-0.589000, 3)
			with else_1:
				main_circ.u(param_0,param_0,0.327000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(qreg_0[0])
				main_circ.u(param_0,param_0,-0.692000, 3)
				main_circ.s(qreg_0[0])
				main_circ.u(0,0,param_0, 0)
		with case_2(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_0,0,-0.104000, 2)
				main_circ.u(param_0,0.476000,-0.785000, 3)
				main_circ.cz(0,3)
				main_circ.cz(0,3)
				main_circ.cz(2,3)
			with else_1:
				main_circ.u(0.088000,param_0,0.698000, 2)
with else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.s(1)
			main_circ.s(qreg_0[0])
			main_circ.s(1)
			main_circ.cz(3,qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(1,0)
				main_circ.cz(1,3)
				main_circ.cz(2,3)
				main_circ.s(qreg_0[0])
			with else_1:
				main_circ.s(3)
	with case_3(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(2)
				main_circ.cz(1,3)
				main_circ.u(param_0,0,param_0, 3)
				main_circ.u(param_0,-0.543000,param_0, qreg_0[0])
				main_circ.u(0.269000,-0.612000,-0.068000, 3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0,0,0.228000, 1)
			main_circ.s(3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(2)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.barrier(1)
		main_circ.barrier(0)
	with case_3(1):
		main_circ.barrier(2)
bindings = {param_0: -0.010000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "20", "CommutationAnalysis")
