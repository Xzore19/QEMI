from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.cy(qreg_0[0],0)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cy(qreg_1[0],qreg_1[1])
						main_circ.x(qreg_1[0])
						main_circ.cy(qreg_3[0],qreg_1[1])
						main_circ.cy(qreg_0[0],qreg_1[1])
					with case_1(1):
						main_circ.x(0)
						main_circ.cz(qreg_1[1],qreg_3[0])
						main_circ.rz(param_0, qreg_1[0])
						main_circ.cy(qreg_0[0],qreg_1[0])
			with else_2:
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(qreg_1[0],0)
					main_circ.cy(qreg_3[0],qreg_0[0])
				with else_1:
					main_circ.x(qreg_1[1])
					main_circ.cz(qreg_1[1],0)
					main_circ.rz(param_3, 0)
		with else_3:
			main_circ.measure(qreg_1[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(qreg_1[1],qreg_1[0])
					main_circ.cy(qreg_1[1],0)
				with else_1:
					main_circ.rz(0.454000, qreg_1[1])
	with case_4(1):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.cy(qreg_1[1],qreg_3[0])
							main_circ.cy(qreg_1[0],0)
							main_circ.x(qreg_0[0])
							main_circ.x(0)
							main_circ.cz(qreg_0[0],0)
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.rz(param_1, 0)
							main_circ.x(qreg_3[0])
							main_circ.cy(qreg_0[0],qreg_1[0])
							main_circ.rz(param_0, 0)
							main_circ.rz(param_0, 0)
			with case_3(1):
				main_circ.x(0)
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.x(0)
							main_circ.cz(qreg_0[0],0)
							main_circ.cy(qreg_1[1],qreg_1[0])
							main_circ.rz(param_1, qreg_1[1])
						with case_1(1):
							main_circ.cz(qreg_0[0],qreg_3[0])
							main_circ.cy(qreg_3[0],qreg_1[1])
							main_circ.x(0)
							main_circ.cz(qreg_1[0],qreg_3[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.cy(qreg_1[0],qreg_3[0])
						main_circ.rz(param_2, qreg_1[0])
						main_circ.rz(-0.396000, qreg_0[0])
						main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cz(qreg_1[0],qreg_3[0])
		main_circ.rz(-0.326000, qreg_1[1])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(param_3, qreg_3[0])
					main_circ.cy(qreg_1[0],qreg_1[1])
					main_circ.cz(qreg_1[1],qreg_3[0])
					main_circ.rz(0.906000, qreg_1[1])
				with case_1(1):
					main_circ.rz(0.892000, 0)
					main_circ.cy(qreg_0[0],qreg_1[0])
					main_circ.rz(-0.929000, qreg_1[0])
					main_circ.barrier(qreg_1[0])
with else_4:
	main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.748000, param_1: 0.324000, param_2: -0.878000, param_3: 0.438000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "464", "RemoveResetInZeroState")
