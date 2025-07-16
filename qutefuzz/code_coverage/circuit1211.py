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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(1,3)
	main_circ.cz(2,0)
main_circ.x(qreg_0[0])
main_circ.x(3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0,param_3,0.227000, 3)
					main_circ.u(param_3,0,0.776000, qreg_0[0])
					main_circ.u(param_0,0,0.026000, qreg_0[0])
					main_circ.u(param_6,0.685000,-0.584000, qreg_0[0])
				with case_1(1):
					main_circ.x(0)
					main_circ.cz(2,0)
					main_circ.x(1)
					main_circ.u(param_1,0,-0.698000, qreg_0[0])
	with case_3(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_1,param_6,param_4, 3)
				main_circ.u(pi/2,0.432000,-0.250000, 0)
				main_circ.u(param_5,0.301000,param_5, 0)
				main_circ.u(0,0,param_0, 0)
main_circ.x(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(0,qreg_0[0])
				main_circ.cz(qreg_0[0],2)
				main_circ.u(pi/2,param_3,param_3, 3)
				main_circ.u(pi/2,param_6,param_1, 0)
				main_circ.u(param_3,0,0.934000, 2)
			with else_1:
				main_circ.x(2)
				main_circ.x(qreg_0[0])
				main_circ.x(0)
				main_circ.cz(0,qreg_0[0])
		with else_2:
			main_circ.u(0,0,param_0, 2)
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(0,0,param_2, qreg_0[0])
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_0,param_0,-0.790000, 3)
				main_circ.x(2)
				main_circ.cz(2,3)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0,0,0.365000, 2)
					main_circ.cz(2,0)
					main_circ.u(pi/2,param_1,-0.428000, 0)
					main_circ.x(2)
				with case_1(1):
					main_circ.cz(0,1)
					main_circ.cz(3,2)
					main_circ.cz(0,2)
					main_circ.cz(qreg_0[0],2)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(1,qreg_0[0])
					main_circ.cz(qreg_0[0],2)
				with else_1:
					main_circ.cz(2,qreg_0[0])
					main_circ.u(pi/2,param_4,0.374000, 1)
					main_circ.cz(0,3)
			with case_2(1):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.x(2)
					main_circ.cz(1,3)
					main_circ.x(0)
				with else_1:
					main_circ.u(pi/2,0.273000,0.708000, 3)
					main_circ.cz(3,1)
					main_circ.u(param_6,0,-0.784000, 1)
					main_circ.barrier(qreg_0[0])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(2)
			main_circ.id(1)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(1)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(2)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(1)
			main_circ.id(qreg_0[0])
		main_circ.barrier(2)
bindings = {param_0: -0.884000, param_1: 0.738000, param_2: 0.838000, param_3: 0.129000, param_4: 0.819000, param_5: 0.751000, param_6: 0.724000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1211")
