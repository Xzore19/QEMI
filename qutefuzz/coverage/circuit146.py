from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,0.864000, qreg_2[0])
subcirc0.u(-0.703000,-0.473000,-0.382000, qreg_3[0])
subcirc0.u(0.360000,-0.090000,-0.443000, qreg_3[0])
subcirc0.u(0,0,0.363000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.157000, qreg_0[3])
subcirc1.u(pi/2,-0.956000,0.230000, qreg_0[0])
subcirc1.u(pi/2,-0.563000,-0.975000, qreg_0[2])
subcirc1.u(-0.426000,-0.084000,0.092000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,0.773000,0.870000, qreg_0[2])
	main_circ.u(param_0,param_0,param_0, qreg_0[0])
	main_circ.u(param_0,-0.697000,-0.993000, qreg_0[0])
main_circ.u(param_0,-0.224000,param_0, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.u(param_0,param_0,0.341000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_0, qreg_0[1])
		main_circ.u(pi/2,param_0,param_0, qreg_3[0])
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.u(0,0,param_0, qreg_0[1])
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.u(param_0,0,param_0, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_0,param_0, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.797000, qreg_0[2])
	main_circ.id(qreg_0[2])
with else_1:
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,0.067000,0.389000, qreg_0[2])
		main_circ.ry(param_0, qreg_0[0])
		main_circ.ry(param_0, qreg_3[0])
		main_circ.u(param_0,param_0,param_0, qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.u(param_0,param_0,-0.486000, qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(0.771000, qreg_0[0])
	main_circ.u(param_0,-0.471000,param_0, qreg_3[0])
with else_1:
	main_circ.u(-0.939000,param_0,0.314000, qreg_0[1])
main_circ.u(0,param_0,param_0, qreg_3[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
	with case_1(1):
		main_circ.u(param_0,param_0,0.039000, qreg_3[0])
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
with else_1:
	main_circ.ry(param_0, qreg_0[2])
	main_circ.u(param_0,-0.544000,param_0, qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(0.653000, qreg_0[0])
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,param_0,-0.283000, qreg_0[0])
	main_circ.u(pi/2,0.825000,-0.639000, qreg_0[1])
bindings = {param_0: -0.102000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "146")
