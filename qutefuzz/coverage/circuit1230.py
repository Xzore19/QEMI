from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rz(param_0, 1)
				main_circ.x(qreg_0[3])
				main_circ.cz(qreg_0[2],qreg_0[3])
				main_circ.rz(param_0, qreg_0[3])
			with case_1(1):
				main_circ.x(qreg_0[0])
				main_circ.cx(1,qreg_0[1])
				main_circ.cz(qreg_0[2],qreg_0[1])
				main_circ.cz(qreg_0[2],qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(0,qreg_0[0])
				main_circ.cx(qreg_0[3],qreg_0[0])
				main_circ.x(qreg_0[1])
				main_circ.cz(qreg_0[2],qreg_0[0])
			with case_1(1):
				main_circ.rz(-0.023000, qreg_0[1])
				main_circ.rz(param_1, qreg_0[2])
				main_circ.x(qreg_0[2])
				main_circ.x(0)
main_circ.x(1)
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.x(qreg_0[2])
			main_circ.x(qreg_0[0])
			main_circ.cx(1,qreg_0[0])
			main_circ.rz(0.352000, qreg_0[3])
		with case_1(1):
			main_circ.rz(param_1, qreg_0[3])
			main_circ.cz(qreg_0[1],qreg_0[2])
			main_circ.cx(1,qreg_0[0])
			main_circ.x(qreg_0[3])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.x(qreg_0[2])
			main_circ.cz(qreg_0[2],1)
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.rz(-0.230000, qreg_0[0])
		with else_1:
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.x(qreg_0[3])
			main_circ.cz(0,qreg_0[0])
			main_circ.cx(0,1)
			main_circ.cz(qreg_0[1],qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(1)
			main_circ.rz(param_1, qreg_0[1])
			main_circ.cx(qreg_0[2],1)
			main_circ.cz(1,qreg_0[3])
			main_circ.cx(0,qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.x(1)
		main_circ.x(qreg_0[2])
		main_circ.cz(qreg_0[0],qreg_0[1])
	with else_1:
		main_circ.rz(0.738000, qreg_0[1])
		main_circ.cx(0,1)
		main_circ.cz(qreg_0[3],1)
		main_circ.rz(param_1, qreg_0[0])
		main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(qreg_0[1],1)
			main_circ.x(qreg_0[2])
			main_circ.rz(0.293000, qreg_0[3])
			main_circ.cz(qreg_0[1],1)
	with case_2(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(qreg_0[1],qreg_0[3])
			main_circ.x(qreg_0[1])
			main_circ.id(qreg_0[3])
		main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.916000, param_1: -0.175000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1230", "OptimizeCliffords")
