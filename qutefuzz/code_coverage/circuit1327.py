from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.cz(qreg_2[0],qreg_0[1])
			main_circ.u(0.095000,param_1,-0.061000, qreg_0[1])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(qreg_2[0])
						main_circ.s(qreg_2[0])
						main_circ.rz(-0.050000, qreg_2[0])
						main_circ.u(-0.120000,-0.485000,-0.634000, qreg_0[0])
					with case_1(1):
						main_circ.s(qreg_0[1])
						main_circ.rz(0.454000, qreg_2[0])
						main_circ.cz(qreg_2[0],qreg_0[1])
						main_circ.u(0.263000,0.060000,-0.877000, qreg_0[0])
		with case_3(1):
			main_circ.rz(0.848000, qreg_0[1])
			main_circ.rz(param_1, 0)
			main_circ.u(-0.963000,0.234000,0.947000, qreg_0[1])
			main_circ.rz(0.143000, qreg_2[1])
main_circ.s(0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.s(qreg_2[1])
					main_circ.rz(-0.685000, qreg_0[1])
					main_circ.u(-0.983000,0.551000,param_0, qreg_2[1])
					main_circ.cz(qreg_0[1],qreg_2[0])
			with case_2(1):
				main_circ.cz(qreg_0[1],qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(0,qreg_2[1])
					main_circ.s(0)
				with else_1:
					main_circ.cz(qreg_0[1],qreg_2[1])
					main_circ.rz(param_0, qreg_2[0])
					main_circ.cz(qreg_0[0],qreg_2[1])
					main_circ.s(qreg_2[1])
with else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.s(qreg_2[1])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(-0.672000,0.724000,-0.665000, qreg_0[0])
					main_circ.u(-0.896000,-0.083000,-0.749000, qreg_0[1])
					main_circ.s(0)
					main_circ.cz(qreg_2[1],qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(0,qreg_0[1])
					main_circ.cz(qreg_2[1],qreg_0[0])
					main_circ.cz(qreg_2[0],0)
					main_circ.cz(qreg_2[0],0)
			with else_2:
				main_circ.s(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(0)
						main_circ.rz(0.058000, qreg_0[1])
						main_circ.s(qreg_0[0])
						main_circ.s(qreg_2[1])
					with case_1(1):
						main_circ.cz(qreg_2[1],0)
						main_circ.s(qreg_0[1])
						main_circ.barrier(qreg_0[0])
		with case_3(1):
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(0)
			with else_2:
				main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_0[0])
bindings = {param_0: 0.224000, param_1: 0.910000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1327", "OptimizeAnnotated")
