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
subcirc0.u(pi/2,0.506000,0.955000, qreg_0[1])
subcirc0.u(-0.294000,0.256000,0.196000, qreg_0[2])
subcirc0.u(pi/2,0.176000,-0.878000, qreg_0[3])
subcirc0.u(pi/2,0.037000,-0.118000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

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

main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.rz(param_2, qreg_0[3])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rz(param_2, 1)
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[1,qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2],0])
					with case_1(1):
						main_circ.rz(param_1, 1)
						main_circ.h(qreg_0[0])
						main_circ.rz(-0.898000, 1)
						main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[0],1,0,qreg_0[2]])
		with case_3(1):
			main_circ.h(0)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.rz(param_3, qreg_0[1])
						main_circ.h(qreg_0[2])
						main_circ.u(param_1,param_1,0.099000, 1)
						main_circ.u(param_3,param_2,param_0, qreg_0[0])
					with case_1(1):
						main_circ.h(qreg_0[1])
						main_circ.u(param_0,param_3,0.049000, qreg_0[0])
						main_circ.u(param_3,-0.850000,param_1, 1)
						main_circ.h(0)
with else_4:
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.u(0.749000,param_2,param_3, qreg_0[1])
				main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[3],qreg_0[1],1,qreg_0[0]])
			with case_2(1):
				main_circ.rz(0.695000, qreg_0[2])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(pi/2,0.685000,param_1, 0)
					main_circ.u(param_2,param_0,param_1, 1)
					main_circ.h(qreg_0[3])
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[3],qreg_0[1],1])
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_0,0.149000,param_3, qreg_0[3])
				main_circ.rz(0.591000, 1)
				main_circ.rz(param_3, 0)
				main_circ.h(qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(1)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.rz(param_0, 0)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc0,[0,1,qreg_0[1],qreg_0[3],qreg_0[2],qreg_0[0]])
				main_circ.rz(param_3, qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rz(param_2, qreg_0[0])
					main_circ.u(-0.518000,-0.320000,param_0, qreg_0[1])
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[3],1,qreg_0[1]])
				with case_1(1):
					main_circ.h(qreg_0[3])
					main_circ.barrier(qreg_0[0])
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[3])
				with else_1:
					main_circ.id(0)
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.id(1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_0[1])
			with case_2(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.id(0)
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.id(qreg_0[2])
bindings = {param_0: -0.648000, param_1: -0.532000, param_2: -0.964000, param_3: 0.965000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1379")
