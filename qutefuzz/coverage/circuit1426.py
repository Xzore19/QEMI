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
subcirc0.rx(0.132000, qreg_0[0])
subcirc0.u(0,0,-0.740000, qreg_0[0])
subcirc0.u(0,0,-0.600000, qreg_0[1])
subcirc0.rx(-0.408000, qreg_0[0])
subcirc0.u(pi/2,0.420000,-0.212000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.cx(0,1)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc0,[qreg_1[0],1,qreg_3[0],qreg_1[1]])
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(qreg_0[0],qreg_3[0])
			with else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[1],qreg_1[0]])
	with case_3(1):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cx(1,0)
						main_circ.cx(qreg_3[0],qreg_1[0])
						main_circ.append(subcirc0,[qreg_1[1],1,0,qreg_1[0]])
					with case_1(1):
						main_circ.rx(0.726000, qreg_0[0])
						main_circ.rx(param_0, qreg_1[0])
						main_circ.cx(qreg_1[1],0)
						main_circ.u(0,param_2,-0.758000, qreg_1[1])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_2,0,0.587000, 1)
						main_circ.cx(qreg_3[0],1)
						main_circ.rx(param_0, qreg_3[0])
						main_circ.u(pi/2,param_0,param_1, qreg_1[0])
					with case_1(1):
						main_circ.u(param_2,0,-0.145000, qreg_0[0])
						main_circ.u(param_0,0,param_1, qreg_0[0])
						main_circ.u(param_2,0.306000,param_2, 0)
						main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],1,0])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(param_1, 0)
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_1[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_1,0.466000,param_0, qreg_1[0])
				main_circ.rx(param_0, 0)
				main_circ.cx(qreg_3[0],qreg_1[1])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(1,0)
				main_circ.cx(qreg_1[1],qreg_0[0])
				main_circ.cx(qreg_1[0],1)
				main_circ.cx(1,qreg_3[0])
				main_circ.cx(qreg_3[0],qreg_0[0])
		with case_2(1):
			main_circ.cx(qreg_0[0],qreg_3[0])
			main_circ.cx(0,qreg_1[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(qreg_3[0],qreg_1[0])
				main_circ.cx(1,qreg_1[1])
				main_circ.append(subcirc0,[0,qreg_1[1],qreg_0[0],qreg_1[0]])
			with else_1:
				main_circ.u(0,param_2,0.108000, qreg_3[0])
				main_circ.barrier(qreg_1[1])
with else_3:
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.974000, param_1: 0.633000, param_2: -0.766000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1426", "TemplateOptimization")
