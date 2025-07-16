from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.cx(3,qreg_0[0])
		main_circ.cx(1,3)
		main_circ.cx(qreg_0[0],3)
	with case_1(1):
		main_circ.x(qreg_1[0])
		main_circ.x(qreg_1[0])
		main_circ.x(2)
		main_circ.cx(3,qreg_1[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_0[0],0)
	main_circ.x(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(qreg_1[0],1)
	main_circ.cy(qreg_0[0],3)
	main_circ.x(2)
	main_circ.x(0)
with else_1:
	main_circ.x(qreg_1[0])
	main_circ.cx(0,qreg_1[0])
	main_circ.cx(qreg_0[0],qreg_1[0])
	main_circ.u(0.456000,0.982000,param_0, 0)
	main_circ.x(2)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.x(1)
	main_circ.u(0.336000,param_1,0.339000, 0)
	main_circ.cx(1,2)
	main_circ.u(-0.405000,param_0,param_0, qreg_1[0])
with else_1:
	main_circ.cx(1,3)
	main_circ.x(1)
	main_circ.x(1)
	main_circ.u(-0.759000,0.938000,param_0, 3)
	main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(3,2)
		main_circ.u(0.745000,-0.304000,param_0, 2)
		main_circ.cx(3,qreg_0[0])
		main_circ.x(2)
	with case_1(1):
		main_circ.x(1)
		main_circ.x(1)
		main_circ.x(3)
		main_circ.cy(1,3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cx(2,3)
	main_circ.x(qreg_1[0])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0.097000,param_1,param_0, qreg_1[0])
		main_circ.x(0)
		main_circ.cy(qreg_0[0],3)
		main_circ.cy(1,2)
	with case_1(1):
		main_circ.cy(3,qreg_1[0])
		main_circ.x(0)
		main_circ.u(param_1,param_1,-0.008000, 0)
		main_circ.cx(0,qreg_1[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(3,0)
		main_circ.x(3)
		main_circ.cy(1,qreg_1[0])
		main_circ.x(2)
	with case_1(1):
		main_circ.u(param_1,0.452000,param_0, qreg_1[0])
		main_circ.x(qreg_0[0])
		main_circ.x(3)
		main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(qreg_1[0],1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_1,param_0, 3)
		main_circ.x(3)
		main_circ.barrier(2)
	with case_1(1):
		main_circ.barrier(0)
bindings = {param_0: 0.035000, param_1: -0.597000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1489", "Optimize1qGates")
