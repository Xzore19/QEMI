from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(2,3)
				main_circ.cx(3,0)
				main_circ.rx(0.390000, qreg_0[1])
				main_circ.cx(qreg_0[1],1)
			with else_1:
				main_circ.cx(2,qreg_0[0])
				main_circ.rx(param_2, qreg_0[0])
				main_circ.rx(0.190000, qreg_0[0])
				main_circ.u(0,param_2,param_1, 1)
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(3,qreg_0[0])
				main_circ.x(0)
				main_circ.rx(param_1, 1)
			with else_1:
				main_circ.rx(-0.314000, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(qreg_0[1])
				main_circ.x(1)
				main_circ.cx(2,qreg_0[1])
				main_circ.u(param_0,param_1,param_2, 2)
				main_circ.u(param_2,0,param_2, 3)
		with else_2:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cx(2,qreg_0[1])
				main_circ.x(3)
				main_circ.cx(qreg_0[0],qreg_0[1])
				main_circ.cx(2,qreg_0[0])
				main_circ.x(1)
			with else_1:
				main_circ.u(param_0,param_2,0.104000, qreg_0[1])
with else_4:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.x(0)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rx(param_1, 0)
					main_circ.x(0)
					main_circ.u(0,param_0,-0.930000, 3)
					main_circ.rx(param_0, 1)
				with case_1(1):
					main_circ.u(param_1,param_2,param_0, 1)
					main_circ.x(3)
					main_circ.cx(3,0)
					main_circ.x(qreg_0[1])
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cx(qreg_0[1],1)
				main_circ.u(0,0,param_2, qreg_0[1])
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cx(qreg_0[0],2)
				main_circ.cx(3,qreg_0[0])
				main_circ.cx(2,1)
				main_circ.rx(param_2, 3)
				main_circ.cx(2,3)
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.x(0)
					main_circ.u(param_1,0,param_0, 2)
				with else_1:
					main_circ.cx(0,2)
					main_circ.cx(1,0)
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rx(-0.744000, 0)
				with else_1:
					main_circ.x(3)
					main_circ.u(param_2,0,0.671000, 3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cx(0,qreg_0[0])
					main_circ.x(3)
					main_circ.barrier(0)
bindings = {param_0: 0.002000, param_1: -0.838000, param_2: -0.855000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1320")
