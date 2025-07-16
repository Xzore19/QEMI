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
subcirc0.u(pi/2,0.873000,0.877000, qreg_3[0])
subcirc0.u(-0.429000,0.573000,-0.077000, qreg_0[0])
subcirc0.u(pi/2,-0.355000,0.550000, qreg_3[0])
subcirc0.u(pi/2,0.855000,0.072000, qreg_3[0])
subcirc0.x(qreg_0[0])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(2)
	main_circ.z(2)
main_circ.x(1)
main_circ.append(subcirc0,[1,qreg_0[0],0,3])
main_circ.u(param_0,param_3,param_2, qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(1)
	main_circ.z(3)
	main_circ.append(subcirc0,[0,qreg_0[0],3,1])
with else_1:
	main_circ.u(param_0,-0.680000,-0.602000, qreg_0[0])
	main_circ.append(subcirc0,[3,0,1,qreg_0[0]])
main_circ.u(param_2,param_3,0.459000, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(2)
	main_circ.u(0.140000,param_0,-0.989000, 1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_2,param_3,0.728000, 2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[0,3,qreg_0[0],1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[2,0,qreg_0[0],1])
	with case_1(1):
		main_circ.u(pi/2,-0.580000,param_3, 3)
		main_circ.append(subcirc0,[0,qreg_0[0],2,3])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0.865000,param_0,param_2, 0)
		main_circ.u(-0.470000,0.139000,0.939000, 1)
		main_circ.u(pi/2,param_1,0.633000, qreg_0[0])
		main_circ.x(1)
	with case_1(1):
		main_circ.u(param_2,0.166000,-0.703000, 1)
		main_circ.barrier(qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.barrier(2)
	with case_1(1):
		main_circ.z(qreg_0[0])
		main_circ.x(3)
		main_circ.barrier(qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.u(-0.697000,param_2,0.265000, 0)
bindings = {param_0: 0.515000, param_1: 0.942000, param_2: -0.880000, param_3: 0.702000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1708")
