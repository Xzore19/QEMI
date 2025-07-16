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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cz(1,qreg_0[2])
			main_circ.cz(1,qreg_0[1])
			main_circ.u(0.251000,param_3,param_2, qreg_0[2])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[0],qreg_0[3])
				main_circ.cz(qreg_0[1],qreg_0[0])
				main_circ.u(-0.455000,param_1,param_0, qreg_0[1])
				main_circ.cz(qreg_0[0],1)
			with case_1(1):
				main_circ.u(0.907000,-0.315000,-0.272000, 1)
				main_circ.u(-0.546000,0.340000,param_2, qreg_0[3])
				main_circ.u(param_2,-0.436000,param_3, qreg_0[3])
				main_circ.cx(qreg_0[1],qreg_0[2])
	with case_2(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(0.064000,param_0,param_3, qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.cx(qreg_0[1],1)
			main_circ.cz(qreg_0[2],qreg_0[0])
			main_circ.u(param_0,param_3,param_0, qreg_0[0])
		with else_1:
			main_circ.cz(qreg_0[0],1)
			main_circ.u(0.705000,-0.036000,param_0, qreg_0[3])
			main_circ.s(qreg_0[0])
			main_circ.s(qreg_0[1])
			main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(qreg_0[2])
			main_circ.s(qreg_0[2])
		with else_1:
			main_circ.u(0.524000,0.723000,-0.804000, qreg_0[1])
			main_circ.u(param_0,param_3,-0.947000, qreg_0[2])
			main_circ.s(qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.s(1)
				main_circ.cz(qreg_0[0],qreg_0[3])
				main_circ.s(0)
				main_circ.cz(0,qreg_0[3])
			with case_1(1):
				main_circ.u(-0.592000,param_2,param_1, 1)
				main_circ.cx(qreg_0[0],qreg_0[3])
				main_circ.cz(qreg_0[1],1)
				main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0.806000,0.461000,param_0, qreg_0[0])
			main_circ.cx(qreg_0[3],0)
			main_circ.cz(qreg_0[1],qreg_0[2])
			main_circ.cx(0,qreg_0[2])
			main_circ.cz(1,qreg_0[2])
		with else_1:
			main_circ.s(1)
			main_circ.cx(qreg_0[3],0)
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cz(qreg_0[1],qreg_0[2])
			main_circ.u(param_2,param_2,param_1, 1)
			main_circ.cz(qreg_0[2],qreg_0[1])
		with else_1:
			main_circ.cz(1,0)
			main_circ.cx(1,qreg_0[2])
			main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cz(qreg_0[0],qreg_0[3])
			main_circ.cz(qreg_0[0],qreg_0[3])
			main_circ.s(0)
			main_circ.u(0.648000,-0.412000,param_1, qreg_0[0])
			main_circ.cz(qreg_0[2],qreg_0[0])
		with else_1:
			main_circ.cz(qreg_0[2],qreg_0[3])
			main_circ.s(qreg_0[0])
			main_circ.s(0)
			main_circ.cz(qreg_0[1],qreg_0[0])
			main_circ.cz(qreg_0[3],qreg_0[0])
	with case_2(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(1)
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.id(1)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[1])
		main_circ.id(qreg_0[2])
bindings = {param_0: 0.646000, param_1: -0.201000, param_2: 0.192000, param_3: -0.983000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1716")
