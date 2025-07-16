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
subcirc0.x(qreg_0[0])
subcirc0.rx(-0.767000, qreg_0[3])
subcirc0.x(qreg_0[3])
subcirc0.u(0,0,-0.197000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.366000, qreg_3[0])
subcirc1.rz(-0.547000, qreg_0[0])
subcirc1.u(0,0,0.606000, qreg_3[0])
subcirc1.rx(-0.684000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.472000, qreg_0[0])
subcirc2.u(0,0,-0.329000, qreg_0[2])
subcirc2.x(qreg_0[2])
subcirc2.rz(0.146000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.367000, qreg_0[0])
subcirc3.u(0,0,0.514000, qreg_3[0])
subcirc3.x(qreg_0[0])
subcirc3.rx(0.321000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0,0,0.724000, qreg_0[2])
subcirc4.rx(0.214000, qreg_0[1])
subcirc4.rx(-0.768000, qreg_0[0])
subcirc4.u(0,0,-0.070000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0,param_2,param_3, qreg_0[0])
					main_circ.u(param_2,param_0,param_3, qreg_0[0])
					main_circ.u(param_0,0,param_1, 2)
					main_circ.append(subcirc1,[2,qreg_0[0],1,qreg_1[0]])
				with case_1(1):
					main_circ.append(subcirc4,[3,0,2,qreg_1[0],qreg_0[0],1])
		with else_2:
			main_circ.append(subcirc1,[3,2,qreg_1[0],qreg_0[0]])
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc3,[3,qreg_0[0],qreg_1[0],2])
				with case_1(1):
					main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],3,1,0])
	with case_3(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc3,[3,1,0,2])
				with case_1(1):
					main_circ.append(subcirc1,[1,0,qreg_1[0],2])
		with else_2:
			main_circ.append(subcirc1,[2,qreg_1[0],qreg_0[0],3])
			main_circ.u(param_1,param_2,param_2, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rz(param_3, qreg_1[0])
					main_circ.x(1)
					main_circ.rx(param_1, qreg_1[0])
					main_circ.rx(0.818000, 2)
				with else_1:
					main_circ.append(subcirc2,[2,3,1,qreg_0[0],qreg_1[0]])
					main_circ.u(param_0,0,-0.770000, qreg_0[0])
			with case_2(1):
				main_circ.append(subcirc2,[0,qreg_1[0],qreg_0[0],2,3])
	with case_3(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.rx(param_2, 1)
				main_circ.id(1)
		with else_2:
			main_circ.id(1)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_1[0])
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.x(qreg_1[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(1)
			main_circ.id(qreg_1[0])
		main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.005000, param_1: -0.431000, param_2: -0.744000, param_3: -0.809000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1825", "InverseCancellation")
