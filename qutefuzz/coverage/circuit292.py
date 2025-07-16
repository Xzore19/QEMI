from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_2[0])
subcirc0.u(0,0,-0.211000, qreg_3[0])
subcirc0.cx(qreg_2[0],qreg_3[0])
subcirc0.u(0,0,-0.830000, qreg_2[0])
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.u(0,param_2,0.935000, qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(2,1)
				main_circ.id(3)
			with case_1(1):
				main_circ.u(param_0,0,-0.295000, 2)
				main_circ.u(0,param_1,param_3, 2)
				main_circ.u(param_1,param_2,param_3, 0)
				main_circ.rx(param_1, 3)
	with else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cx(qreg_0[0],2)
			main_circ.u(param_3,0,-0.817000, 0)
		with else_1:
			main_circ.cx(3,qreg_0[0])
			main_circ.u(param_3,param_3,param_0, 1)
			main_circ.rx(0.434000, 0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(0,0,param_2, 2)
					main_circ.cz(1,qreg_0[0])
					main_circ.cx(0,3)
					main_circ.rx(param_2, 2)
			with case_2(1):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_3, 1)
					main_circ.u(param_0,param_1,param_1, qreg_0[0])
					main_circ.cx(2,1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(1,2)
					main_circ.cx(2,3)
					main_circ.cx(qreg_0[0],0)
	with case_3(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(0,0,-0.042000, 2)
					main_circ.cx(2,0)
				with else_1:
					main_circ.u(0,0,param_1, 3)
					main_circ.id(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_3, 2)
					main_circ.u(0,param_2,param_3, qreg_0[0])
					main_circ.barrier(0)
			with case_2(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(0,0,param_3, 2)
				with else_1:
					main_circ.rx(param_1, 3)
					main_circ.cz(qreg_0[0],0)
					main_circ.cz(2,qreg_0[0])
					main_circ.u(0,0,param_0, qreg_0[0])
					main_circ.cz(qreg_0[0],3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cz(2,0)
						main_circ.cz(2,qreg_0[0])
						main_circ.id(0)
					with case_1(1):
						main_circ.cx(0,2)
						main_circ.cz(2,0)
						main_circ.u(param_1,0,0.784000, 2)
						main_circ.rx(-0.934000, 0)
			with case_2(1):
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cz(2,qreg_0[0])
					main_circ.u(param_1,param_2,param_0, 2)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cx(0,qreg_0[0])
					main_circ.cx(0,2)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.rx(0.415000, qreg_0[0])
					main_circ.cx(3,qreg_0[0])
					main_circ.cz(qreg_0[0],3)
					main_circ.rx(-0.286000, 0)
			with case_2(1):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(0,qreg_0[0])
					main_circ.u(0,0,param_2, 1)
				with else_1:
					main_circ.u(param_1,param_2,-0.552000, 2)
					main_circ.cx(3,0)
					main_circ.id(3)
bindings = {param_0: 0.532000, param_1: -0.611000, param_2: 0.635000, param_3: 0.782000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "292", "CollectMultiQBlocks")
