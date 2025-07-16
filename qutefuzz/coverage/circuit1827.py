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
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[3])
subcirc0.u(0.808000,0.608000,0.265000, qreg_0[1])
subcirc0.cy(qreg_0[3],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0.524000,-0.841000,0.046000, qreg_1[0])
subcirc1.u(0.028000,0.477000,0.334000, qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_1[2])
subcirc1.y(qreg_1[2])
subcirc1.cy(qreg_1[0],qreg_1[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_0,param_0,param_0, qreg_0[1])
				main_circ.id(qreg_0[2])
			main_circ.cx(qreg_0[1],qreg_3[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(0.875000,0.817000,-0.032000, qreg_0[0])
				main_circ.cx(qreg_0[0],qreg_0[1])
		with case_2(1):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(qreg_3[0],qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cx(qreg_0[0],qreg_0[2])
					main_circ.cx(qreg_0[0],qreg_0[2])
					main_circ.cy(qreg_0[2],qreg_0[0])
					main_circ.cy(qreg_0[2],qreg_0[1])
				with case_1(1):
					main_circ.u(-0.765000,param_0,0.044000, qreg_0[1])
					main_circ.u(0.970000,0.098000,param_0, qreg_0[2])
					main_circ.cx(qreg_3[0],qreg_0[2])
					main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.y(qreg_3[0])
		with else_1:
			main_circ.y(qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_3[0])
	with else_2:
		main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.barrier(qreg_3[0])
		main_circ.u(0.154000,-0.912000,0.986000, qreg_0[2])
		main_circ.u(-0.329000,-0.903000,param_0, qreg_0[2])
		main_circ.u(0.473000,param_0,param_0, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
			with case_1(1):
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.cy(qreg_0[2],qreg_0[1])
				main_circ.cy(qreg_0[0],qreg_0[1])
				main_circ.y(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_0,param_0,param_0, qreg_3[0])
			main_circ.cx(qreg_3[0],qreg_0[1])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(qreg_3[0],qreg_0[2])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cx(qreg_0[1],qreg_3[0])
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.y(qreg_3[0])
			main_circ.y(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0.482000,param_0,-0.368000, qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[2],qreg_0[1]])
		with else_1:
			main_circ.barrier(qreg_3[0])
	with else_2:
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[2],qreg_0[1])
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.y(qreg_0[1])
				main_circ.cy(qreg_0[2],qreg_0[1])
				main_circ.y(qreg_0[1])
				main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.457000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1827")
