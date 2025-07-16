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
subcirc0.u(pi/2,0.949000,-0.356000, qreg_0[0])
subcirc0.u(0,0,0.533000, qreg_0[3])
subcirc0.rz(-0.918000, qreg_0[1])
subcirc0.u(pi/2,0.493000,0.696000, qreg_0[3])
subcirc0.rz(0.170000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.270000, qreg_2[0])
subcirc1.u(pi/2,0.872000,0.395000, qreg_2[0])
subcirc1.u(pi/2,-0.227000,-0.099000, qreg_2[0])
subcirc1.u(0,0,0.121000, qreg_3[0])
subcirc1.rx(0.918000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.rx(0.307000, qreg_2[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_1, qreg_1[0])
		main_circ.u(param_2,param_4,param_1, qreg_0[0])
		main_circ.u(0,param_1,-0.478000, qreg_2[0])
		main_circ.barrier(qreg_2[0])
	with case_1(1):
		main_circ.rz(-0.131000, qreg_0[0])
		main_circ.append(subcirc1,[qreg_2[0],qreg_1[0],qreg_3[0],qreg_0[0]])
main_circ.rz(0.727000, qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(0.631000, qreg_2[0])
		main_circ.u(param_0,param_4,0.673000, qreg_0[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.u(param_2,param_3,-0.087000, qreg_0[0])
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_3, qreg_3[0])
		main_circ.rz(param_3, qreg_1[0])
		main_circ.rx(param_4, qreg_1[0])
		main_circ.barrier(qreg_2[0])
	with case_1(1):
		main_circ.id(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(-0.155000, qreg_0[0])
main_circ.u(pi/2,param_3,0.699000, qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_2, qreg_1[0])
		main_circ.u(param_4,0,param_4, qreg_3[0])
		main_circ.append(subcirc1,[qreg_1[0],qreg_2[0],qreg_0[0],qreg_3[0]])
	with case_1(1):
		main_circ.rx(-0.654000, qreg_2[0])
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(0.070000, qreg_2[0])
		main_circ.rx(0.851000, qreg_1[0])
		main_circ.rz(param_1, qreg_0[0])
		main_circ.rx(-0.340000, qreg_3[0])
	with case_1(1):
		main_circ.u(0,param_4,param_3, qreg_3[0])
		main_circ.rx(-0.373000, qreg_2[0])
		main_circ.u(0,param_1,param_0, qreg_0[0])
		main_circ.u(0,0,-0.295000, qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(0.622000, qreg_2[0])
		main_circ.u(pi/2,param_1,param_2, qreg_3[0])
		main_circ.rx(0.703000, qreg_3[0])
		main_circ.rz(-0.868000, qreg_3[0])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_2[0]])
bindings = {param_0: 0.250000, param_1: -0.882000, param_2: 0.340000, param_3: 0.539000, param_4: 0.218000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "721")
