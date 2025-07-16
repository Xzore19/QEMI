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
subcirc0.s(qreg_0[1])
subcirc0.ry(-0.959000, qreg_0[0])
subcirc0.u(0,0,0.372000, qreg_0[2])
subcirc0.rx(0.071000, qreg_0[2])
subcirc0.u(0,0,0.732000, qreg_3[0])
subcirc0.u(0,0,0.254000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.381000, qreg_0[2])
subcirc1.u(0,0,-0.491000, qreg_0[1])
subcirc1.rx(-0.024000, qreg_0[3])
subcirc1.ry(-0.449000, qreg_0[1])
subcirc1.u(0,0,0.855000, qreg_0[0])
subcirc1.ry(-0.062000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.144000, qreg_1[1])
subcirc2.u(0,0,0.290000, qreg_1[1])
subcirc2.rx(0.230000, qreg_3[0])
subcirc2.ry(0.882000, qreg_1[0])
subcirc2.s(qreg_1[0])
subcirc2.u(0,0,-0.873000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.s(qreg_0[1])
subcirc3.rx(-0.938000, qreg_2[0])
subcirc3.s(qreg_2[1])
subcirc3.rx(0.487000, qreg_0[0])
subcirc3.s(qreg_2[0])
subcirc3.s(qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_3 = Parameter("param_3")

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc3,[1,2,0,qreg_0[0]])
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0,0,param_1, 3)
					main_circ.append(subcirc3,[0,qreg_0[0],1,3])
				with case_1(1):
					main_circ.id(0)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.id(2)
	with case_4(1):
		main_circ.append(subcirc2,[1,qreg_0[0],2,0,3])
main_circ.append(subcirc3,[3,0,1,qreg_0[0]])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.append(subcirc2,[3,2,0,1,qreg_0[0]])
			with case_3(1):
				main_circ.append(subcirc0,[1,2,0,3])
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.u(0,0,param_1, 0)
						main_circ.ry(-0.919000, 3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.u(0,param_1,param_0, 0)
						main_circ.append(subcirc3,[1,qreg_0[0],2,0])
				with case_2(1):
					main_circ.u(param_2,0,param_0, 2)
					main_circ.append(subcirc2,[qreg_0[0],2,0,3,1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.u(param_1,param_3,-0.756000, 0)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.rx(param_1, 2)
						main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.rx(0.120000, 3)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.s(1)
						main_circ.u(0,0,-0.996000, qreg_0[0])
						main_circ.rx(-0.531000, 2)
				with case_2(1):
					main_circ.barrier(0)
		with case_3(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(0)
					main_circ.id(0)
				with case_2(1):
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(3)
					main_circ.barrier(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.barrier(3)
			main_circ.id(1)
bindings = {param_0: -0.959000, param_1: -0.939000, param_2: 0.482000, param_3: 0.655000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "747")
