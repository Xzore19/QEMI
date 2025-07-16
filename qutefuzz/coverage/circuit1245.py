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
subcirc0.u(0,0,-0.898000, qreg_0[2])
subcirc0.u(pi/2,0.882000,0.461000, qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.u(pi/2,0.152000,0.932000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,0.080000, qreg_0[2])
subcirc1.u(pi/2,-0.757000,0.936000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_1[1])
subcirc2.u(pi/2,0.891000,-0.659000, qreg_1[2])
subcirc2.z(qreg_1[1])
subcirc2.z(qreg_1[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.z(3)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,0,param_1, 0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,param_2,param_0, 0)
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(0)
		main_circ.append(subcirc1,[3,qreg_0[0],1,2])
with else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.z(2)
			main_circ.u(pi/2,0.076000,param_2, 2)
			main_circ.cy(1,0)
			main_circ.u(pi/2,param_1,0.364000, 3)
	with else_2:
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cy(2,qreg_0[1])
				main_circ.z(1)
				main_circ.append(subcirc1,[qreg_0[1],0,2,3])
			with case_1(1):
				main_circ.cy(1,3)
				main_circ.u(0,param_1,0.760000, qreg_0[0])
				main_circ.append(subcirc2,[2,1,3,qreg_0[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(pi/2,param_1,param_0, 2)
		with else_1:
			main_circ.u(pi/2,0.645000,param_2, 1)
			main_circ.u(pi/2,param_1,param_2, 2)
			main_circ.append(subcirc2,[3,qreg_0[1],qreg_0[0],0])
	with else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,0.432000,-0.821000, 0)
			main_circ.cy(qreg_0[0],qreg_0[1])
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cy(qreg_0[1],0)
				main_circ.cy(1,3)
				main_circ.cy(1,3)
				main_circ.cy(2,qreg_0[1])
			with case_1(1):
				main_circ.cy(3,qreg_0[1])
				main_circ.cy(1,2)
				main_circ.cy(1,0)
				main_circ.cy(2,1)
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.cy(qreg_0[0],0)
			main_circ.cy(3,0)
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.u(param_0,param_3,0.618000, qreg_0[1])
				main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.barrier(1)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(3)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.id(0)
bindings = {param_0: -0.525000, param_1: 0.589000, param_2: 0.186000, param_3: 0.238000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1245", "CollectCliffords")
