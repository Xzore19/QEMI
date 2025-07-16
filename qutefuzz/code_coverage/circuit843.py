from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_1[2])
subcirc0.z(qreg_1[1])
subcirc0.u(0,0,-0.997000, qreg_1[0])
subcirc0.x(qreg_1[2])
subcirc0.z(qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(0)
		main_circ.rz(-0.060000, 0)
		main_circ.append(subcirc0,[1,0,3,2])
	with case_1(1):
		main_circ.x(2)
		main_circ.u(param_3,0,param_3, 2)
		main_circ.append(subcirc0,[1,0,2,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_2,param_0,-0.729000, 2)
	main_circ.append(subcirc0,[0,3,1,2])
with else_1:
	main_circ.x(2)
	main_circ.append(subcirc0,[3,2,1,0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[1,3,2,0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(-0.991000, 1)
	main_circ.append(subcirc0,[1,0,3,2])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,param_1,param_3, 2)
	main_circ.id(3)
with else_1:
	main_circ.id(3)
bindings = {param_0: -0.592000, param_1: -0.279000, param_2: 0.975000, param_3: -0.722000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "843", "HoareOptimizer")
