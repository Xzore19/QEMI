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
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.u(pi/2,0.115000,-0.458000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.rx(-0.421000, qreg_2[1])
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.u(pi/2,-0.597000,0.677000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,0.492000,-0.576000, qreg_2[1])
subcirc2.cy(qreg_0[1],qreg_2[0])
subcirc2.cz(qreg_2[1],qreg_0[0])
subcirc2.u(pi/2,0.378000,-0.364000, qreg_2[0])
subcirc2.rx(-0.701000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cy(qreg_3[0],qreg_2[0])
subcirc3.cz(qreg_1[0],qreg_0[0])
subcirc3.u(pi/2,0.590000,0.029000, qreg_2[0])
subcirc3.rx(0.048000, qreg_1[0])
subcirc3.cy(qreg_3[0],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rx(param_2, qreg_2[1])
					main_circ.barrier(qreg_2[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_1[0])
			with else_1:
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cz(0,qreg_1[0])
				main_circ.id(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.u(param_0,0.826000,-0.035000, qreg_1[0])
				main_circ.id(0)
			with else_1:
				main_circ.u(param_2,-0.086000,param_1, 0)
		with case_2(1):
			main_circ.barrier(qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[0],1)
				main_circ.cy(qreg_0[0],0)
				main_circ.barrier(qreg_2[1])
			with case_1(1):
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(1,0)
				main_circ.barrier(0)
			with case_1(1):
				main_circ.cz(qreg_2[1],qreg_1[0])
				main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_0, 1)
			main_circ.append(subcirc1,[qreg_0[0],0,qreg_2[1],qreg_2[0],1])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc1,[qreg_0[0],0,qreg_2[0],qreg_1[0],1])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cy(qreg_0[0],1)
					main_circ.id(0)
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc1,[qreg_2[1],1,qreg_2[0],0,qreg_1[0]])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cz(qreg_0[0],0)
				main_circ.cz(0,qreg_0[0])
				main_circ.append(subcirc1,[qreg_1[0],1,0,qreg_2[1],qreg_0[0]])
			with else_1:
				main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_1[0],qreg_2[1]])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.rx(0.964000, qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.cz(1,qreg_1[0])
			main_circ.id(qreg_1[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_2[0])
		with else_1:
			main_circ.u(param_2,param_1,param_3, 0)
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.cy(qreg_1[0],qreg_2[0])
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.u(param_3,-0.182000,-0.701000, 1)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.cy(qreg_2[0],qreg_1[0])
					main_circ.cy(qreg_1[0],qreg_0[0])
					main_circ.u(param_2,-0.822000,param_3, qreg_1[0])
					main_circ.barrier(0)
		with case_2(1):
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_1[0],1])
				with case_1(1):
					main_circ.cy(qreg_1[0],1)
					main_circ.append(subcirc1,[1,qreg_0[0],0,qreg_2[0],qreg_1[0]])
bindings = {param_0: -0.284000, param_1: 0.342000, param_2: 0.926000, param_3: 0.491000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1571", "ResetAfterMeasureSimplification")
