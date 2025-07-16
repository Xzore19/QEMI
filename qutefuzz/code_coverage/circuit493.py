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

main_circ.u(param_2,0,-0.136000, 1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(2,0)
				main_circ.cz(3,1)
				main_circ.u(param_2,param_0,param_2, 1)
				main_circ.z(2)
			with case_1(1):
				main_circ.z(qreg_0[0])
				main_circ.u(param_1,param_2,0.629000, 0)
				main_circ.u(0.155000,param_1,param_0, qreg_0[0])
				main_circ.u(param_1,param_1,-0.522000, 1)
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(3,1)
				main_circ.cz(1,3)
				main_circ.z(qreg_0[0])
				main_circ.z(qreg_0[0])
			with case_1(1):
				main_circ.cz(0,2)
				main_circ.u(param_1,0.120000,0.371000, 2)
				main_circ.cz(qreg_0[0],2)
				main_circ.cz(1,2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(1,qreg_0[0])
				main_circ.cz(qreg_0[0],3)
				main_circ.z(qreg_0[0])
				main_circ.z(3)
			with case_1(1):
				main_circ.u(0.453000,param_2,param_1, qreg_0[0])
				main_circ.u(param_0,0.560000,0.822000, 2)
				main_circ.u(-0.074000,param_1,param_2, qreg_0[0])
				main_circ.cz(0,2)
	with case_2(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_2,0,param_1, 0)
			main_circ.u(-0.644000,0.651000,0.315000, 2)
			main_circ.cz(3,0)
			main_circ.cz(2,3)
		with else_1:
			main_circ.z(0)
			main_circ.u(param_0,param_2,-0.614000, 3)
			main_circ.u(param_0,-0.879000,-0.116000, qreg_0[0])
			main_circ.cz(1,3)
			main_circ.u(0,param_0,-0.318000, 2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0.047000,0.483000,param_0, 0)
			main_circ.u(param_1,param_1,param_0, 3)
			main_circ.z(1)
			main_circ.u(param_1,param_0,-0.219000, 3)
		with case_1(1):
			main_circ.z(3)
			main_circ.cz(2,qreg_0[0])
			main_circ.u(param_0,0,param_1, 3)
			main_circ.u(param_1,param_0,0.868000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(3)
			main_circ.u(param_0,param_0,0.038000, 2)
			main_circ.u(param_2,param_1,-0.664000, qreg_0[0])
			main_circ.id(2)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(3)
		main_circ.barrier(qreg_0[0])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.id(3)
bindings = {param_0: -0.895000, param_1: -0.118000, param_2: 0.170000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "493")
