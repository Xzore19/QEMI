from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.rx(param_0, qreg_0[0])
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.rx(-0.053000, qreg_0[2])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cx(qreg_0[0],qreg_0[3])
						main_circ.cx(0,qreg_0[2])
						main_circ.cx(qreg_0[1],0)
						main_circ.rx(param_0, qreg_0[0])
						main_circ.cy(qreg_0[3],qreg_0[0])
					with else_1:
						main_circ.cy(qreg_0[1],qreg_0[2])
						main_circ.cx(qreg_0[2],qreg_0[1])
			with case_3(1):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.u(0,0,0.065000, qreg_0[1])
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.cy(qreg_0[1],0)
								main_circ.rx(-0.410000, 0)
								main_circ.u(0,param_1,0.718000, qreg_0[1])
								main_circ.u(0,0,0.565000, qreg_0[3])
							with case_1(1):
								main_circ.u(param_0,param_1,param_0, qreg_0[2])
								main_circ.cy(qreg_0[2],0)
								main_circ.cy(qreg_0[1],qreg_0[2])
								main_circ.u(param_1,param_1,-0.599000, qreg_0[0])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.cy(qreg_0[2],qreg_0[3])
							main_circ.rx(param_2, qreg_0[3])
							main_circ.cy(qreg_0[2],qreg_0[0])
							main_circ.cx(0,qreg_0[0])
	with case_4(1):
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(qreg_0[1],qreg_0[3])
		main_circ.rx(param_2, qreg_0[1])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_0[3])
					main_circ.u(param_0,param_0,param_0, 0)
					main_circ.cx(qreg_0[3],qreg_0[0])
				with else_1:
					main_circ.rx(0.959000, qreg_0[3])
					main_circ.u(param_0,0,0.582000, qreg_0[3])
					main_circ.u(param_2,param_2,param_2, 0)
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(0,param_2,0.507000, 0)
						main_circ.rx(param_1, qreg_0[2])
						main_circ.cx(0,qreg_0[1])
						main_circ.rx(param_1, qreg_0[2])
					with case_1(1):
						main_circ.cy(qreg_0[3],0)
						main_circ.cx(qreg_0[3],0)
						main_circ.cy(qreg_0[0],qreg_0[2])
						main_circ.cx(qreg_0[2],0)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_1,param_0, qreg_0[3])
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rx(0.232000, qreg_0[3])
				with else_1:
					main_circ.cx(0,qreg_0[0])
					main_circ.u(0,param_0,param_2, qreg_0[1])
					main_circ.cy(qreg_0[2],0)
					main_circ.rx(param_2, qreg_0[3])
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_1, qreg_0[2])
					main_circ.rx(param_0, qreg_0[0])
					main_circ.cy(0,qreg_0[1])
					main_circ.cx(qreg_0[0],qreg_0[2])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.cx(qreg_0[1],qreg_0[0])
							main_circ.cx(qreg_0[1],qreg_0[2])
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.barrier(0)
			main_circ.id(qreg_0[2])
bindings = {param_0: 0.556000, param_1: -0.112000, param_2: 0.207000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1434")
