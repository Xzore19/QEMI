from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_5 = Parameter("param_5")

main_circ.ry(param_0, qreg_0[0])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(0.038000, qreg_0[1])
	main_circ.u(param_3,param_2,0.872000, qreg_0[0])
	main_circ.cy(1,0)
	main_circ.u(-0.885000,-0.379000,param_0, qreg_2[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_0,param_5,param_0, 0)
	main_circ.u(param_4,0.805000,0.138000, qreg_0[0])
	main_circ.ry(0.508000, 0)
	main_circ.cy(qreg_0[0],qreg_0[1])
with else_1:
	main_circ.ry(-0.345000, 1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(1,qreg_2[1])
	main_circ.u(0.215000,-0.108000,0.305000, qreg_0[1])
	main_circ.ry(param_4, qreg_0[1])
main_circ.cy(qreg_0[1],0)
main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.339000, 0)
		main_circ.u(param_4,-0.545000,param_2, 0)
		main_circ.u(param_3,-0.979000,-0.052000, qreg_0[0])
		main_circ.cy(qreg_2[1],1)
	with case_1(1):
		main_circ.u(param_2,param_5,param_1, 0)
		main_circ.ry(param_0, qreg_0[1])
		main_circ.u(param_4,0.888000,0.138000, qreg_2[0])
		main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(qreg_2[1],qreg_0[1])
with else_1:
	main_circ.u(0.603000,0.629000,param_3, 0)
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_0[1],qreg_2[1])
	main_circ.ry(0.252000, qreg_2[1])
	main_circ.ry(param_3, qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_2[0],1)
		main_circ.u(pi/2,0.428000,param_5, qreg_2[1])
		main_circ.u(param_2,0.125000,-0.751000, qreg_2[0])
		main_circ.cy(0,qreg_0[1])
	with case_1(1):
		main_circ.cy(qreg_2[1],1)
		main_circ.cy(qreg_2[1],qreg_0[1])
		main_circ.u(param_4,param_1,param_4, qreg_2[0])
		main_circ.ry(param_1, qreg_2[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_3,0.808000,param_1, 1)
		main_circ.u(0.682000,0.553000,0.768000, qreg_0[0])
		main_circ.u(0.451000,param_3,-0.482000, 0)
		main_circ.u(param_1,param_0,param_1, qreg_2[1])
	with case_1(1):
		main_circ.cy(qreg_2[1],qreg_0[0])
		main_circ.cy(qreg_2[1],1)
		main_circ.cy(qreg_2[0],qreg_0[0])
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.717000, param_1: 0.405000, param_2: -0.195000, param_3: -0.576000, param_4: -0.045000, param_5: -0.553000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "428")
