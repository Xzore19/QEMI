from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,0.222000,0.189000, qreg_0[0])
subcirc0.y(qreg_2[0])
subcirc0.y(qreg_2[0])
subcirc0.y(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.u(pi/2,-0.272000,-0.409000, qreg_2[0])
subcirc1.u(pi/2,-0.859000,0.070000, qreg_2[1])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.y(qreg_2[0])
subcirc2.y(qreg_0[0])
subcirc2.u(pi/2,-0.630000,0.304000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.349000,-0.171000, qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_3[0])
subcirc3.x(qreg_3[0])
subcirc3.x(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_0,0.016000,param_1, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc3,[2,0,1,3,qreg_0[0]])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[0],2,3,1])
			main_circ.y(qreg_0[0])
		with else_1:
			main_circ.u(pi/2,param_0,0.613000, 1)
			main_circ.cy(1,2)
			main_circ.cy(3,qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.y(0)
		main_circ.append(subcirc1,[2,qreg_0[0],3,0])
main_circ.x(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.append(subcirc1,[3,qreg_0[0],1,2])
	with case_2(1):
		main_circ.x(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,param_1,-0.148000, 1)
				main_circ.u(param_1,param_0,param_0, 0)
				main_circ.x(1)
				main_circ.cy(0,qreg_0[0])
			with case_1(1):
				main_circ.y(qreg_0[0])
				main_circ.u(pi/2,param_0,param_0, 0)
				main_circ.y(2)
				main_circ.cy(2,0)
main_circ.append(subcirc0,[0,qreg_0[0],3,1])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc3,[qreg_0[0],2,3,1,0])
	main_circ.cy(qreg_0[0],1)
with else_2:
	main_circ.cy(1,0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.cy(2,0)
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cy(3,qreg_0[0])
			main_circ.cy(2,3)
			main_circ.cy(3,qreg_0[0])
			main_circ.cy(3,0)
		with case_1(1):
			main_circ.cy(3,2)
			main_circ.cy(2,1)
			main_circ.cy(qreg_0[0],3)
			main_circ.cy(2,qreg_0[0])
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.u(param_1,param_0,param_1, qreg_0[0])
			main_circ.cy(0,qreg_0[0])
			main_circ.cy(0,3)
			main_circ.id(1)
main_circ.u(pi/2,param_1,-0.915000, 1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(0,2)
			main_circ.barrier(2)
		with case_1(1):
			main_circ.barrier(0)
	main_circ.y(1)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(3)
	with else_1:
		main_circ.barrier(2)
	main_circ.barrier(2)
bindings = {param_0: 0.364000, param_1: -0.669000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "340")
