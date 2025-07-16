from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,-0.305000,0.173000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.u(pi/2,-0.217000,0.898000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.280000, qreg_0[1])
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_3[0])
subcirc1.rz(0.077000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,0.841000,0.725000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cx(3,2)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.z(1)
					main_circ.id(1)
				with case_1(1):
					main_circ.cx(0,3)
					main_circ.cx(1,0)
					main_circ.rz(-0.373000, 0)
					main_circ.barrier(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.rz(param_0, 1)
				main_circ.cx(0,1)
				main_circ.barrier(1)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(3)
			main_circ.u(pi/2,param_1,-0.030000, 1)
			main_circ.u(pi/2,param_2,0.189000, 1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.cx(3,0)
					main_circ.rz(param_3, 1)
					main_circ.id(0)
	with case_3(1):
		main_circ.u(param_0,param_0,param_3, 0)
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,0.220000,-0.946000, 0)
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.u(pi/2,0.866000,param_2, 3)
				main_circ.u(param_3,0.107000,0.819000, 2)
				main_circ.u(param_1,0.325000,param_2, 1)
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.cx(1,0)
						main_circ.cx(2,1)
						main_circ.z(2)
						main_circ.barrier(0)
				main_circ.z(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cx(3,0)
				main_circ.cx(3,0)
				main_circ.id(3)
			with else_1:
				main_circ.u(param_1,0.647000,param_2, 0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rz(param_1, 2)
					main_circ.z(3)
					main_circ.u(pi/2,param_3,param_1, 0)
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(2)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.z(0)
				main_circ.u(param_1,0.684000,param_1, 2)
			with else_1:
				main_circ.z(3)
				main_circ.barrier(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rz(param_2, 2)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.rz(-0.225000, 1)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.cx(1,2)
				main_circ.barrier(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.rz(0.920000, 1)
					main_circ.z(3)
					main_circ.u(param_3,param_0,param_2, 0)
					main_circ.u(param_1,0.049000,-0.254000, 0)
				with case_1(1):
					main_circ.cx(0,3)
					main_circ.u(param_3,-0.722000,0.633000, 3)
					main_circ.id(1)
		with else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.z(1)
				main_circ.cx(1,0)
				main_circ.cx(1,2)
				main_circ.cx(2,0)
				main_circ.cx(3,2)
	with case_3(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cx(2,1)
				main_circ.cx(1,0)
			main_circ.rz(param_2, 1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cx(0,1)
					main_circ.cx(0,3)
					main_circ.barrier(3)
				with case_1(1):
					main_circ.rz(param_0, 1)
					main_circ.barrier(2)
main_circ.rz(-0.843000, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.cx(2,1)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.barrier(1)
			main_circ.z(0)
			main_circ.barrier(0)
		with case_2(1):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.z(1)
				main_circ.z(3)
				main_circ.id(1)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.rz(param_0, 3)
				main_circ.barrier(1)
			main_circ.z(3)
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.z(1)
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(2)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(2)
		main_circ.id(1)
	with else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(1)
		main_circ.barrier(1)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.id(1)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.id(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.id(3)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.id(3)
			main_circ.id(2)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.barrier(3)
	with else_2:
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.id(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.id(2)
		main_circ.barrier(0)
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.barrier(2)
			main_circ.barrier(0)
		with case_2(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(3)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(1)
			main_circ.barrier(2)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.id(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(1)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(1)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.id(3)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.id(0)
	main_circ.id(1)
bindings = {param_0: -0.981000, param_1: 0.062000, param_2: -0.293000, param_3: 0.552000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "442", "Collect1qRuns")
