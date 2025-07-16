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
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rx(param_1, qreg_0[1])
		main_circ.rx(param_0, 3)
		main_circ.cx(0,3)
with else_2:
	main_circ.cz(qreg_0[0],1)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(0.230000, 2)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.z(3)
			main_circ.cz(2,qreg_0[0])
			main_circ.z(0)
			main_circ.cx(qreg_0[1],0)
		with case_1(1):
			main_circ.rx(-0.066000, 1)
			main_circ.z(qreg_0[1])
			main_circ.rx(param_1, 3)
			main_circ.cx(qreg_0[1],2)
main_circ.rx(0.870000, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[0],qreg_0[1])
				main_circ.rx(param_0, qreg_0[0])
				main_circ.cz(3,qreg_0[1])
				main_circ.cx(2,qreg_0[0])
			with case_1(1):
				main_circ.rx(param_2, 2)
				main_circ.cx(qreg_0[0],qreg_0[1])
				main_circ.cz(qreg_0[0],1)
				main_circ.cz(2,1)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(0,qreg_0[0])
				main_circ.cz(0,qreg_0[1])
				main_circ.cz(2,1)
				main_circ.rx(-0.218000, 3)
			with case_1(1):
				main_circ.cz(1,qreg_0[0])
				main_circ.cz(2,3)
				main_circ.cx(1,2)
				main_circ.z(2)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.cx(qreg_0[0],3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[1],qreg_0[0])
				main_circ.cz(qreg_0[0],0)
				main_circ.cz(3,2)
				main_circ.cz(2,qreg_0[0])
			with case_1(1):
				main_circ.cz(qreg_0[1],3)
				main_circ.cx(qreg_0[0],3)
				main_circ.cz(3,1)
				main_circ.cz(qreg_0[0],qreg_0[1])
	with case_2(1):
		main_circ.rx(-0.117000, qreg_0[0])
		main_circ.cz(qreg_0[0],1)
		main_circ.cx(3,0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_2, 0)
			main_circ.z(0)
			main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.783000, param_1: 0.781000, param_2: 0.329000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1094", "Collect1qRuns")
