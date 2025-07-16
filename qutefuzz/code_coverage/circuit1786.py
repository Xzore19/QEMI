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
subcirc0.rx(-0.166000, qreg_1[2])
subcirc0.u(pi/2,0.392000,-0.928000, qreg_1[1])
subcirc0.rx(-0.094000, qreg_0[0])
subcirc0.rx(-0.712000, qreg_0[0])
subcirc0.rx(-0.900000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[1],qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_2[0])
subcirc1.u(pi/2,0.935000,-0.285000, qreg_0[0])
subcirc1.rx(0.053000, qreg_3[0])
subcirc1.u(0,0,-0.190000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.137000, qreg_1[1])
subcirc2.u(0,0,0.364000, qreg_3[0])
subcirc2.u(0,0,0.222000, qreg_3[0])
subcirc2.rx(0.681000, qreg_3[0])
subcirc2.rx(0.444000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_2[0])
subcirc3.u(pi/2,-0.227000,0.028000, qreg_2[0])
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.u(0,0,0.737000, qreg_2[0])
subcirc3.u(pi/2,-0.395000,0.064000, qreg_2[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_1[2])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.cz(qreg_1[2],qreg_1[0])
			main_circ.rx(0.361000, qreg_1[0])
			main_circ.rx(-0.311000, qreg_1[2])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rx(param_0, qreg_1[1])
			main_circ.u(0,param_1,param_1, qreg_1[2])
			main_circ.append(subcirc3,[qreg_1[2],qreg_0[0],qreg_1[1],qreg_1[0]])
	with case_2(1):
		main_circ.u(param_0,0.324000,param_1, qreg_1[2])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cz(qreg_1[2],qreg_1[0])
			main_circ.id(qreg_1[2])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_0,-0.422000,param_0, qreg_1[0])
			main_circ.u(pi/2,-0.065000,-0.358000, qreg_0[0])
			main_circ.u(param_1,param_1,0.530000, qreg_1[2])
			main_circ.rx(param_1, qreg_0[0])
		with else_1:
			main_circ.u(pi/2,-0.488000,0.631000, qreg_1[1])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.cz(qreg_1[1],qreg_1[2])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc0,[qreg_1[2],qreg_0[0],qreg_1[0],qreg_1[1]])
		with else_1:
			main_circ.barrier(qreg_1[1])
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc0,[qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
		with else_1:
			main_circ.append(subcirc3,[qreg_1[1],qreg_1[2],qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(qreg_1[1])
	main_circ.append(subcirc3,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_1[2]])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cz(qreg_1[2],qreg_1[0])
		with else_1:
			main_circ.cz(qreg_1[2],qreg_0[0])
			main_circ.cz(qreg_1[0],qreg_0[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_1[2],qreg_0[0])
				main_circ.cz(qreg_1[0],qreg_1[1])
				main_circ.rx(0.642000, qreg_1[1])
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.u(param_1,param_1,param_0, qreg_1[2])
				main_circ.barrier(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rx(param_1, qreg_1[0])
			main_circ.id(qreg_1[1])
		main_circ.measure(qreg_1[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rx(param_1, qreg_1[2])
			main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.id(qreg_1[0])
	with case_2(1):
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(pi/2,param_1,param_0, qreg_1[2])
		main_circ.id(qreg_1[0])
	main_circ.id(qreg_1[2])
bindings = {param_0: -0.425000, param_1: 0.056000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1786")
