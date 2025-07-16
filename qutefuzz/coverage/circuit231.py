from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rz(0.926000, qreg_0[0])
subcirc0.u(0.582000,-0.393000,0.017000, qreg_2[1])
subcirc0.rz(-0.187000, qreg_2[1])
subcirc0.rz(0.622000, qreg_2[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.cy(qreg_2[0],qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.ry(-0.204000, qreg_2[0])
						main_circ.ry(0.078000, qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.rz(0.846000, qreg_2[0])
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.u(param_4,0.167000,param_3, qreg_2[0])
							main_circ.cy(qreg_0[1],qreg_2[0])
						with case_1(1):
							main_circ.ry(0.919000, qreg_3[0])
							main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0]])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.ry(-0.922000, qreg_2[0])
						main_circ.cy(qreg_0[0],qreg_2[0])
						main_circ.ry(-0.725000, qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.rz(0.869000, qreg_2[0])
						main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
					with else_1:
						main_circ.ry(-0.574000, qreg_0[1])
						main_circ.u(param_4,0.888000,-0.633000, qreg_0[1])
		with else_3:
			main_circ.rz(0.230000, qreg_3[0])
			main_circ.rz(param_1, qreg_3[0])
			main_circ.rz(param_4, qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.ry(-0.244000, qreg_0[0])
						main_circ.cy(qreg_3[0],qreg_0[1])
					with else_1:
						main_circ.rz(0.597000, qreg_0[1])
						main_circ.cy(qreg_0[1],qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.u(param_3,-0.044000,-0.715000, qreg_2[0])
						main_circ.cy(qreg_3[0],qreg_0[1])
						main_circ.u(-0.493000,-0.406000,param_1, qreg_0[1])
						main_circ.u(param_0,param_2,param_1, qreg_0[0])
						main_circ.u(param_0,0.825000,0.866000, qreg_3[0])
	with case_4(1):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.cy(qreg_0[1],qreg_0[0])
							main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
						with case_1(1):
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.cy(qreg_0[0],qreg_2[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.cy(qreg_0[1],qreg_2[0])
						main_circ.cy(qreg_0[0],qreg_3[0])
					with else_1:
						main_circ.cy(qreg_0[0],qreg_2[0])
						main_circ.ry(0.226000, qreg_2[0])
						main_circ.u(-0.179000,-0.923000,param_0, qreg_0[0])
			with case_3(1):
				main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.rz(0.247000, qreg_2[0])
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_3[0])
	main_circ.barrier(qreg_2[0])
with else_4:
	main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.518000, param_1: 0.852000, param_2: -0.209000, param_3: 0.880000, param_4: 0.124000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "231", "Collect2qBlocks")
