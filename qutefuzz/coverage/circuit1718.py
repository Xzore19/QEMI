from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.u(pi/2,0.012000,param_2, qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rz(param_2, qreg_0[3])
				main_circ.cx(qreg_0[3],qreg_0[1])
				main_circ.u(pi/2,param_4,-0.116000, qreg_0[2])
				main_circ.cx(qreg_0[1],qreg_0[0])
			with case_1(1):
				main_circ.rz(-0.003000, qreg_0[3])
				main_circ.rz(-0.778000, qreg_0[0])
				main_circ.u(pi/2,-0.571000,param_3, qreg_0[3])
				main_circ.rx(-0.178000, qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rz(0.845000, qreg_0[3])
			main_circ.u(pi/2,-0.513000,0.729000, qreg_0[1])
			main_circ.cx(qreg_0[0],qreg_0[2])
			main_circ.u(pi/2,-0.091000,param_0, qreg_0[2])
main_circ.rx(param_2, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(0.851000, qreg_0[0])
		main_circ.rx(-0.890000, qreg_0[1])
		main_circ.cx(qreg_0[3],qreg_0[0])
		main_circ.u(pi/2,-0.850000,-0.239000, qreg_0[3])
		main_circ.u(param_1,param_0,0.237000, qreg_0[0])
with else_2:
	main_circ.cx(qreg_0[1],qreg_0[2])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(pi/2,param_5,param_1, qreg_0[1])
		main_circ.rz(param_0, qreg_0[2])
		main_circ.u(pi/2,-0.878000,0.289000, qreg_0[2])
		main_circ.rx(0.449000, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(pi/2,param_5,param_2, qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(0.809000, qreg_0[0])
			main_circ.cx(qreg_0[3],qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(-0.339000, qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(0.417000, qreg_0[3])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,-0.914000,0.950000, qreg_0[2])
			main_circ.rx(0.750000, qreg_0[0])
			main_circ.rx(-0.356000, qreg_0[3])
			main_circ.cx(qreg_0[1],qreg_0[3])
			main_circ.rx(param_1, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.u(param_4,param_5,param_2, qreg_0[3])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.rz(param_3, qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[0])
		with case_1(1):
			main_circ.cx(qreg_0[2],qreg_0[0])
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.cx(qreg_0[3],qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(qreg_0[3],qreg_0[0])
		main_circ.cx(qreg_0[3],qreg_0[1])
		main_circ.rz(param_2, qreg_0[1])
		main_circ.cx(qreg_0[2],qreg_0[3])
		main_circ.rx(param_1, qreg_0[1])
	with else_1:
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.rx(param_3, qreg_0[3])
		main_circ.cx(qreg_0[3],qreg_0[1])
		main_circ.rz(0.618000, qreg_0[0])
		main_circ.id(qreg_0[0])
bindings = {param_0: -0.835000, param_1: 0.106000, param_2: -0.761000, param_3: -0.062000, param_4: -0.014000, param_5: 0.839000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1718")
