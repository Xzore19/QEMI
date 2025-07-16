from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0.349000,-0.416000,-0.082000, qreg_0[2])
subcirc0.u(-0.708000,-0.926000,-0.522000, qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.818000,0.573000,0.709000, qreg_0[2])
subcirc1.u(-0.079000,-0.548000,0.631000, qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1.u(0.948000,0.305000,0.790000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(1)
main_circ.u(pi/2,0.629000,param_0, 2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.h(3)
						main_circ.h(1)
						main_circ.barrier(0)
					with case_1(1):
						main_circ.y(1)
						main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(2)
					main_circ.h(1)
					main_circ.h(3)
					main_circ.u(pi/2,0.271000,-0.005000, 3)
				with else_1:
					main_circ.y(1)
					main_circ.barrier(1)
			with case_2(1):
				main_circ.u(param_0,param_0,0.880000, 0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.y(3)
					main_circ.id(1)
				with else_1:
					main_circ.h(0)
					main_circ.append(subcirc1,[3,1,0,2])
	with else_3:
		main_circ.append(subcirc1,[2,0,3,1])
		main_circ.y(0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.u(0.948000,param_0,0.859000, 2)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.u(-0.624000,-0.914000,param_0, 1)
			with else_1:
				main_circ.append(subcirc1,[2,1,3,0])
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.append(subcirc1,[2,0,1,3])
with else_4:
	main_circ.u(pi/2,0.922000,-0.491000, 1)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.u(param_0,-0.046000,param_0, 3)
				main_circ.h(1)
				main_circ.u(param_0,param_0,0.674000, 3)
				main_circ.append(subcirc1,[2,1,3,0])
			with else_1:
				main_circ.append(subcirc1,[1,2,3,0])
	with else_3:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(param_0,param_0,0.859000, 2)
					main_circ.u(param_0,param_0,param_0, 0)
					main_circ.append(subcirc1,[2,3,0,1])
				with else_1:
					main_circ.barrier(3)
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0.553000,param_0,-0.026000, 0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.y(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.id(3)
bindings = {param_0: -0.215000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "246", "CollectLinearFunctions")
