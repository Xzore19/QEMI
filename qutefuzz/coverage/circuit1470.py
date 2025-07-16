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
subcirc0.rz(0.408000, qreg_3[0])
subcirc0.rz(-0.542000, qreg_3[0])
subcirc0.rz(0.289000, qreg_0[1])
subcirc0.u(pi/2,-0.795000,-0.837000, qreg_0[1])
subcirc0.u(pi/2,0.283000,0.676000, qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rz(-0.600000, qreg_0[2])
				main_circ.x(qreg_0[1])
				main_circ.rx(0.660000, qreg_3[0])
				main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
			with else_1:
				main_circ.u(pi/2,param_3,-0.793000, qreg_0[1])
				main_circ.u(pi/2,-0.776000,0.943000, qreg_0[0])
		with case_2(1):
			main_circ.x(qreg_0[0])
			main_circ.rx(param_2, qreg_0[1])
			main_circ.x(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_3,0.025000,-0.406000, qreg_0[2])
				main_circ.x(qreg_0[0])
			with else_1:
				main_circ.u(param_4,0.303000,0.724000, qreg_3[0])
with else_3:
	main_circ.rx(-0.564000, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rx(0.595000, qreg_0[2])
			main_circ.u(pi/2,param_4,0.812000, qreg_0[1])
			main_circ.rz(0.802000, qreg_3[0])
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
		with else_1:
			main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
			with else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(pi/2,param_1,param_4, qreg_0[0])
				main_circ.x(qreg_3[0])
				main_circ.u(param_3,param_0,param_0, qreg_3[0])
				main_circ.rx(param_2, qreg_0[0])
			with else_1:
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
	with case_3(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_4, qreg_3[0])
					main_circ.rx(param_0, qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.x(qreg_0[0])
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[2])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_0[2])
bindings = {param_0: 0.795000, param_1: -0.182000, param_2: 0.574000, param_3: -0.193000, param_4: -0.426000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1470")
