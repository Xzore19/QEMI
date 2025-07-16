from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.x(qreg_1[2])
subcirc0.x(qreg_1[1])
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_1[2])
subcirc0.s(qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_1[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.u(-0.431000,-0.647000,-0.980000, qreg_0[2])
subcirc2.u(-0.513000,-0.726000,-0.893000, qreg_0[0])
subcirc2.x(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_0[0])
subcirc3.u(0.968000,-0.817000,-0.364000, qreg_0[2])
subcirc3.u(-0.882000,-0.352000,0.132000, qreg_3[0])
subcirc3.u(0.457000,0.799000,-0.023000, qreg_0[0])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_2[0])
subcirc4.s(qreg_1[0])
subcirc4.u(-0.612000,0.174000,0.912000, qreg_0[0])
subcirc4.s(qreg_2[0])
subcirc4.u(0.881000,-0.022000,0.560000, qreg_2[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],qreg_1[1],qreg_1[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_1[1])
		with else_1:
			main_circ.id(0)
		main_circ.u(param_2,-0.536000,-0.053000, qreg_1[1])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc4,[qreg_1[1],0,qreg_0[0],qreg_1[0]])
	with case_2(1):
		main_circ.u(0.141000,-0.347000,param_2, qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.h(qreg_3[0])
				main_circ.u(-0.740000,-0.768000,-0.011000, qreg_1[0])
				main_circ.append(subcirc3,[qreg_1[1],qreg_0[0],0,qreg_1[0],qreg_3[0]])
main_circ.u(0.814000,-0.423000,-0.663000, qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(0)
				main_circ.s(qreg_1[1])
				main_circ.s(qreg_3[0])
				main_circ.x(qreg_3[0])
			with case_1(1):
				main_circ.append(subcirc4,[qreg_0[0],qreg_3[0],qreg_1[1],0])
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(qreg_1[1])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc3,[0,qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc3,[qreg_3[0],qreg_1[0],qreg_1[1],qreg_0[0],0])
		with case_1(1):
			main_circ.u(-0.192000,-0.024000,-0.987000, qreg_1[1])
			main_circ.h(qreg_1[0])
			main_circ.u(param_1,param_1,-0.563000, qreg_3[0])
			main_circ.append(subcirc3,[0,qreg_3[0],qreg_0[0],qreg_1[1],qreg_1[0]])
with else_2:
	main_circ.u(-0.062000,param_1,-0.446000, qreg_1[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(param_0,-0.754000,param_2, 0)
			main_circ.barrier(qreg_1[1])
		with case_1(1):
			main_circ.u(param_0,0.364000,0.061000, qreg_1[0])
			main_circ.append(subcirc4,[qreg_1[1],qreg_1[0],qreg_0[0],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.u(param_0,param_2,param_1, 0)
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[1])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
		main_circ.id(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.id(qreg_3[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_1[1])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_1[1])
		with else_1:
			main_circ.id(qreg_1[1])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_1[0])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_3[0])
		with else_1:
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.barrier(qreg_3[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_1[1])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_3[0])
		with else_1:
			main_circ.id(qreg_1[1])
		main_circ.measure(qreg_1[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_1[0])
bindings = {param_0: 0.683000, param_1: 0.420000, param_2: 0.653000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "975")
