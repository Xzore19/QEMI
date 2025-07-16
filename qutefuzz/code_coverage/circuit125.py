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
subcirc0.y(qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0.rz(-0.049000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.rz(-0.295000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.y(0)
					main_circ.id(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.cy(3,0)
					main_circ.id(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.x(0)
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.y(3)
					main_circ.y(0)
					main_circ.x(1)
					main_circ.rz(-0.118000, 3)
					main_circ.y(2)
				with else_1:
					main_circ.cy(0,2)
					main_circ.rz(param_0, 2)
			with case_2(1):
				main_circ.x(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.x(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cy(0,1)
						main_circ.cy(1,3)
						main_circ.y(0)
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(1)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rz(param_0, 1)
			with else_1:
				main_circ.rz(param_0, 2)
				main_circ.rz(0.572000, 2)
				main_circ.rz(param_0, 1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.cy(3,0)
						main_circ.y(2)
						main_circ.id(0)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.x(0)
					main_circ.id(3)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.x(1)
						main_circ.x(2)
						main_circ.cy(2,3)
						main_circ.y(2)
					with case_1(1):
						main_circ.y(2)
						main_circ.id(3)
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.y(3)
					main_circ.x(2)
					main_circ.cy(1,0)
				with else_1:
					main_circ.cy(1,0)
					main_circ.cy(2,3)
					main_circ.cy(0,2)
					main_circ.cy(0,3)
					main_circ.cy(2,0)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.x(2)
				main_circ.x(3)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(3,0)
					main_circ.x(1)
					main_circ.barrier(2)
				with case_1(1):
					main_circ.rz(param_4, 1)
					main_circ.y(1)
					main_circ.id(2)
bindings = {param_0: -0.244000, param_4: -0.618000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "125")
