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
subcirc0.u(0,0,0.801000, qreg_0[1])
subcirc0.rz(0.556000, qreg_3[0])
subcirc0.ry(-0.256000, qreg_3[0])
subcirc0.rz(-0.254000, qreg_0[1])
subcirc0.ry(-0.557000, qreg_0[2])
subcirc0.u(0,0,0.218000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_1,0,0.153000, 3)
	main_circ.u(param_2,0,-0.134000, 2)
	main_circ.append(subcirc0,[3,1,2,0])
main_circ.append(subcirc0,[2,1,0,3])
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(0.625000, 1)
		main_circ.u(0,0,param_5, 1)
		main_circ.append(subcirc0,[0,2,1,3])
	with case_1(1):
		main_circ.u(param_3,param_1,param_4, 1)
		main_circ.cx(2,3)
		main_circ.u(param_2,param_0,param_0, 1)
		main_circ.rz(-0.951000, 1)
main_circ.rz(0.916000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,0,-0.305000, 0)
	main_circ.u(0,0,0.755000, 3)
	main_circ.append(subcirc0,[0,3,2,1])
with else_1:
	main_circ.cx(1,2)
main_circ.cx(3,0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(0,3)
	main_circ.cx(3,1)
	main_circ.cx(0,3)
	main_circ.cx(3,2)
with else_1:
	main_circ.cx(3,2)
	main_circ.cx(2,1)
	main_circ.cx(0,2)
	main_circ.cx(0,2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(0,2)
	main_circ.cx(2,3)
	main_circ.cx(3,1)
	main_circ.id(0)
with else_1:
	main_circ.u(param_1,param_1,param_2, 0)
bindings = {param_0: -0.286000, param_1: -0.212000, param_2: 0.020000, param_3: -0.945000, param_4: -0.961000, param_5: 0.443000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "589")
