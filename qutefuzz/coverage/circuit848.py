from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.z(qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.rz(0.096000, qreg_1[0])
subcirc0.u(-0.100000,-0.260000,-0.075000, qreg_0[0])
subcirc0.rz(0.730000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(0.524000, qreg_0[1])
	main_circ.z(qreg_0[3])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(-0.134000, 0)
	main_circ.z(0)
	main_circ.rz(-0.803000, qreg_0[1])
	main_circ.rz(-0.657000, 0)
	main_circ.u(param_0,param_2,param_1, 0)
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(-0.984000,-0.485000,0.989000, qreg_0[0])
	main_circ.z(qreg_0[0])
	main_circ.id(qreg_0[3])
with else_1:
	main_circ.u(param_0,-0.303000,0.002000, qreg_0[3])
	main_circ.z(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[1],0)
	main_circ.u(param_2,0.097000,-0.221000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.250000,param_3,0.407000, qreg_0[1])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[0],0)
		main_circ.cz(qreg_0[0],qreg_0[2])
		main_circ.rz(-0.824000, qreg_0[2])
		main_circ.id(0)
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_4, qreg_0[3])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(0,qreg_0[0])
with else_1:
	main_circ.cz(0,qreg_0[0])
	main_circ.cz(qreg_0[3],qreg_0[2])
	main_circ.rz(param_4, qreg_0[1])
	main_circ.cz(qreg_0[1],qreg_0[2])
	main_circ.u(param_2,param_2,0.087000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.u(param_3,-0.403000,param_4, qreg_0[3])
	main_circ.cz(qreg_0[3],qreg_0[0])
	main_circ.rz(-0.165000, qreg_0[2])
	main_circ.rz(param_2, qreg_0[2])
	main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.z(qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(qreg_0[1],qreg_0[3])
with else_1:
	main_circ.cz(qreg_0[2],qreg_0[1])
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.cz(qreg_0[3],0)
	main_circ.barrier(0)
main_circ.rz(-0.301000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0.606000,param_3,-0.492000, qreg_0[2])
		main_circ.z(qreg_0[0])
		main_circ.z(0)
		main_circ.u(0.733000,param_1,param_4, 0)
	with case_1(1):
		main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[1])
	with case_1(1):
		main_circ.u(-0.830000,-0.775000,0.712000, qreg_0[2])
		main_circ.u(param_4,param_1,param_2, qreg_0[1])
		main_circ.u(param_0,-0.900000,-0.219000, qreg_0[1])
		main_circ.u(param_0,-0.745000,param_3, 0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rz(-0.629000, qreg_0[1])
with else_1:
	main_circ.id(qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
bindings = {param_0: 0.005000, param_1: 0.335000, param_2: 0.178000, param_3: 0.757000, param_4: -0.915000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "848", "OptimizeCliffords")
