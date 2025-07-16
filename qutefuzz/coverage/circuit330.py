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
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.u(0,0,0.430000, qreg_3[0])
subcirc0.z(qreg_0[1])
subcirc0.rz(0.872000, qreg_0[1])
subcirc0.z(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.521000, qreg_0[1])
subcirc1.u(0,0,-0.788000, qreg_0[0])
subcirc1.u(0,0,0.056000, qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.u(0,0,0.498000, qreg_0[1])
subcirc1.u(0,0,0.089000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.356000, qreg_3[0])
subcirc2.u(0,0,-0.069000, qreg_0[2])
subcirc2.rz(-0.657000, qreg_0[2])
subcirc2.u(-0.865000,0.357000,-0.652000, qreg_0[1])
subcirc2.rz(0.611000, qreg_3[0])
subcirc2.z(qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(0.987000, qreg_0[1])
subcirc3.z(qreg_0[0])
subcirc3.u(-0.048000,-0.101000,-0.184000, qreg_0[1])
subcirc3.u(0,0,0.459000, qreg_2[0])
subcirc3.rz(-0.449000, qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,0.303000, qreg_3[0])
subcirc4.z(qreg_2[0])
subcirc4.u(0.749000,-0.107000,0.096000, qreg_0[1])
subcirc4.z(qreg_3[0])
subcirc4.rz(0.834000, qreg_0[1])
subcirc4.u(-0.883000,-0.442000,0.045000, qreg_0[1])

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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[2])
	with else_1:
		main_circ.u(param_0,0,param_0, qreg_0[2])
		main_circ.rz(-0.565000, qreg_0[1])
		main_circ.id(qreg_3[0])
	main_circ.z(qreg_0[2])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.z(qreg_3[0])
		main_circ.barrier(qreg_0[2])
	with else_1:
		main_circ.u(param_0,0.346000,-0.181000, qreg_0[1])
		main_circ.u(-0.299000,param_0,param_0, qreg_0[0])
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.z(qreg_0[2])
		main_circ.z(qreg_3[0])
	with else_1:
		main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(0,0,param_0, qreg_0[2])
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.z(qreg_3[0])
				main_circ.barrier(qreg_3[0])
		main_circ.barrier(qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[2])
		main_circ.u(0,0,param_0, qreg_0[0])
		main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
	with case_2(1):
		main_circ.rz(0.767000, qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[2])
			with case_1(1):
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rz(param_0, qreg_3[0])
				main_circ.u(0.078000,param_0,-0.404000, qreg_0[1])
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.barrier(qreg_3[0])
		main_circ.u(param_0,param_0,param_0, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(-0.934000,-0.605000,-0.068000, qreg_0[0])
		main_circ.id(qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_3[0])
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.063000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "330", "ElidePermutations")
