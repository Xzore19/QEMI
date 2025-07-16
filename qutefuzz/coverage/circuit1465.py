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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(-0.907000,0.105000,-0.098000, 2)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(0)
					main_circ.cx(2,3)
					main_circ.u(param_0,param_1,param_2, 0)
				with else_1:
					main_circ.h(2)
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(param_1,-0.459000,param_0, 0)
					main_circ.u(0.172000,0.109000,param_2, qreg_0[0])
					main_circ.h(1)
					main_circ.u(param_0,-0.064000,0.992000, 3)
					main_circ.cx(qreg_0[0],2)
	with else_3:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(0,qreg_0[0])
				main_circ.u(param_1,0.257000,param_1, 2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cx(1,3)
					main_circ.cx(2,qreg_0[0])
					main_circ.u(param_2,-0.601000,0.933000, qreg_0[0])
					main_circ.z(qreg_0[0])
				with case_1(1):
					main_circ.h(qreg_0[0])
					main_circ.h(2)
					main_circ.h(2)
					main_circ.h(0)
with else_4:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cx(1,qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.z(qreg_0[0])
					main_circ.h(2)
				main_circ.z(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(3,1)
						main_circ.u(0.616000,param_1,0.072000, 0)
						main_circ.h(2)
						main_circ.u(0.782000,-0.933000,param_2, 0)
					with case_1(1):
						main_circ.cx(qreg_0[0],2)
						main_circ.cx(1,qreg_0[0])
						main_circ.u(-0.547000,param_2,param_0, qreg_0[0])
						main_circ.cx(2,3)
			with case_2(1):
				main_circ.cx(3,2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cx(1,0)
					main_circ.h(0)
					main_circ.u(0.902000,param_1,-0.146000, 2)
					main_circ.h(1)
main_circ.cx(qreg_0[0],1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(3,1)
						main_circ.cx(qreg_0[0],2)
						main_circ.cx(3,0)
						main_circ.cx(2,qreg_0[0])
					with case_1(1):
						main_circ.u(param_2,0.178000,param_1, 3)
						main_circ.z(0)
						main_circ.u(param_0,0.111000,param_0, 1)
						main_circ.h(3)
			with else_2:
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cx(1,0)
						main_circ.z(qreg_0[0])
						main_circ.h(3)
						main_circ.u(param_1,param_2,param_1, qreg_0[0])
					with case_1(1):
						main_circ.h(2)
						main_circ.u(-0.890000,0.756000,-0.228000, qreg_0[0])
						main_circ.u(param_1,param_0,0.309000, 2)
						main_circ.id(1)
		with else_3:
			main_circ.id(2)
	with case_4(1):
		main_circ.barrier(2)
bindings = {param_0: -0.415000, param_1: 0.005000, param_2: -0.536000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1465", "CommutativeInverseCancellation")
