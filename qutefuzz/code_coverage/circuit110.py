from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
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

main_circ.u(param_1,0.122000,param_0, qreg_2[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rx(0.770000, qreg_0[0])
					main_circ.rx(param_2, 0)
					main_circ.z(qreg_3[0])
					main_circ.z(qreg_3[0])
				with case_1(1):
					main_circ.rx(-0.442000, qreg_3[0])
					main_circ.u(pi/2,0.110000,param_0, qreg_2[0])
					main_circ.u(pi/2,0.164000,param_0, qreg_3[0])
					main_circ.u(param_0,param_0,0.408000, qreg_3[0])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(-0.985000, qreg_3[0])
				main_circ.ry(param_0, 0)
				main_circ.z(qreg_3[0])
				main_circ.ry(0.786000, 0)
			with else_1:
				main_circ.ry(param_2, 0)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.z(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rx(0.780000, qreg_3[0])
				main_circ.ry(param_2, qreg_0[0])
				main_circ.rx(param_1, 0)
				main_circ.ry(-0.691000, qreg_0[0])
			with case_1(1):
				main_circ.z(qreg_3[0])
				main_circ.z(qreg_2[0])
				main_circ.rx(0.993000, 0)
				main_circ.u(param_1,param_0,-0.890000, qreg_0[0])
with else_3:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.rx(param_2, qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.z(0)
			main_circ.u(pi/2,0.269000,0.785000, qreg_2[0])
			main_circ.ry(param_1, qreg_0[1])
			main_circ.u(pi/2,param_0,param_1, qreg_0[0])
		with else_1:
			main_circ.rx(param_1, qreg_0[0])
			main_circ.rx(param_0, qreg_3[0])
			main_circ.rx(param_2, qreg_0[1])
			main_circ.ry(0.995000, qreg_2[0])
	with else_2:
		main_circ.rx(-0.574000, qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_0,param_0,-0.833000, 0)
				main_circ.ry(param_2, 0)
				main_circ.u(pi/2,-0.230000,-0.650000, 0)
				main_circ.u(pi/2,param_0,param_1, qreg_2[0])
			with case_1(1):
				main_circ.ry(0.428000, qreg_3[0])
				main_circ.ry(param_2, qreg_2[0])
				main_circ.rx(param_1, qreg_2[0])
				main_circ.u(pi/2,param_2,0.224000, qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.ry(param_1, qreg_0[1])
				main_circ.ry(0.483000, qreg_0[1])
				main_circ.u(pi/2,param_0,param_0, qreg_0[0])
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_2[0])
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.barrier(0)
	with else_2:
		main_circ.id(qreg_0[0])
bindings = {param_0: -0.936000, param_1: 0.360000, param_2: 0.068000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "110")
