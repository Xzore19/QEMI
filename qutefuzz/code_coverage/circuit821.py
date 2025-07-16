from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.u(0.781000,-0.233000,-0.232000, qreg_2[0])
subcirc0.u(-0.095000,0.304000,-0.940000, qreg_0[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cx(qreg_1[0],qreg_1[1])
subcirc1.cx(qreg_1[0],qreg_0[0])
subcirc1.cy(qreg_1[1],qreg_1[0])
subcirc1.cx(qreg_1[1],qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_2[0],qreg_3[0])
subcirc2.cy(qreg_2[0],qreg_3[0])
subcirc2.cz(qreg_0[0],qreg_2[0])
subcirc2.u(0.220000,0.428000,-0.722000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(qreg_0[2],qreg_0[0])
			main_circ.barrier(qreg_0[1])
		main_circ.barrier(qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.barrier(qreg_0[2])
with else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[2])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cy(qreg_0[0],0)
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.cy(qreg_0[0],0)
			main_circ.barrier(qreg_0[1])
	with else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[2],qreg_0[3])
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[3])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(0,qreg_0[3])
					main_circ.cy(qreg_0[3],qreg_0[0])
					main_circ.cx(0,qreg_0[3])
					main_circ.cy(qreg_0[0],qreg_0[3])
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[3])
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cz(qreg_0[1],0)
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.cy(qreg_0[0],qreg_0[2])
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[1])
	with case_3(1):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_0[3],qreg_0[2])
				main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cx(qreg_0[1],qreg_0[0])
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.cy(qreg_0[0],0)
					main_circ.barrier(qreg_0[0])
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[1],0)
					main_circ.cz(0,qreg_0[3])
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[2])
			main_circ.id(0)
main_circ.cy(0,qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.cx(qreg_0[1],qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cz(qreg_0[3],qreg_0[1])
				main_circ.cz(qreg_0[1],qreg_0[3])
			with else_1:
				main_circ.cy(0,qreg_0[1])
				main_circ.id(qreg_0[0])
			main_circ.cx(qreg_0[2],qreg_0[3])
		with case_2(1):
			main_circ.u(-0.917000,param_0,param_0, qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.cz(qreg_0[0],qreg_0[3])
					main_circ.barrier(qreg_0[3])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_0,param_0,-0.278000, qreg_0[3])
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.u(param_0,param_0,0.738000, qreg_0[1])
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.cz(qreg_0[3],qreg_0[2])
					main_circ.barrier(qreg_0[0])
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(qreg_0[0],0)
		main_circ.id(qreg_0[2])
	with else_2:
		main_circ.barrier(qreg_0[1])
	main_circ.cy(qreg_0[3],qreg_0[2])
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(-0.811000,param_0,-0.991000, qreg_0[0])
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.u(param_0,param_0,-0.139000, qreg_0[0])
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cz(qreg_0[1],qreg_0[3])
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.cy(qreg_0[0],qreg_0[3])
				with case_1(1):
					main_circ.id(0)
		with case_2(1):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cx(qreg_0[0],qreg_0[3])
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.cz(qreg_0[0],qreg_0[3])
					main_circ.cz(qreg_0[3],0)
					main_circ.id(qreg_0[2])
			main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cy(0,qreg_0[2])
				main_circ.id(qreg_0[2])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cz(qreg_0[0],0)
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cz(qreg_0[0],qreg_0[3])
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.cx(qreg_0[0],qreg_0[3])
		with case_2(1):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cz(qreg_0[2],0)
				main_circ.cx(0,qreg_0[2])
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(qreg_0[1],qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,-0.137000,0.165000, 0)
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.cx(qreg_0[1],0)
					main_circ.id(qreg_0[2])
bindings = {param_0: 0.524000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "821")
