from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.943000,-0.056000, qreg_3[0])
subcirc0.rz(-0.465000, qreg_1[0])
subcirc0.u(pi/2,-0.050000,0.093000, qreg_0[0])
subcirc0.rz(0.648000, qreg_0[0])

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

main_circ.s(0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],0,2,1])
	with case_1(1):
		main_circ.rx(param_1, 2)
		main_circ.rx(-0.937000, qreg_0[0])
		main_circ.rx(0.067000, qreg_0[0])
		main_circ.rx(param_0, qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(pi/2,-0.678000,param_0, 3)
	main_circ.u(pi/2,-0.337000,param_1, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[3,qreg_0[0],0,2])
main_circ.s(2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(pi/2,param_0,param_1, qreg_0[0])
	main_circ.u(pi/2,0.414000,0.929000, 1)
with else_1:
	main_circ.u(pi/2,param_1,param_1, 0)
	main_circ.append(subcirc0,[3,1,2,qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(pi/2,param_0,-0.546000, qreg_0[0])
	main_circ.append(subcirc0,[0,3,2,qreg_0[0]])
with else_1:
	main_circ.s(0)
	main_circ.u(param_0,0.672000,param_0, 1)
	main_circ.rz(-0.877000, 0)
	main_circ.append(subcirc0,[2,qreg_0[0],1,0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.019000, qreg_0[0])
	main_circ.rx(param_0, 2)
	main_circ.rz(0.523000, qreg_0[0])
	main_circ.rz(param_0, 3)
	main_circ.u(pi/2,param_0,param_1, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[1,3,0,2])
	with case_1(1):
		main_circ.s(qreg_0[0])
		main_circ.append(subcirc0,[2,0,3,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[1,qreg_0[0],2,3])
	with case_1(1):
		main_circ.u(param_1,-0.180000,param_0, 1)
		main_circ.rx(param_1, qreg_0[0])
		main_circ.append(subcirc0,[0,1,2,qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(1)
with else_1:
	main_circ.id(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(3)
	main_circ.barrier(1)
bindings = {param_0: 0.153000, param_1: 0.527000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1662")
