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
subcirc0.y(qreg_3[0])
subcirc0.rz(-0.526000, qreg_0[0])
subcirc0.y(qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(param_1, 0)
			main_circ.y(qreg_0[0])
			main_circ.cy(0,qreg_0[0])
			main_circ.u(param_0,param_7,param_3, 1)
		with else_1:
			main_circ.cy(2,1)
			main_circ.cy(1,2)
			main_circ.u(param_0,0.497000,param_6, qreg_0[0])
			main_circ.cy(3,2)
main_circ.rz(-0.897000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.append(subcirc0,[3,0,qreg_0[0],2])
with else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_7,0.074000,param_5, 0)
		with else_1:
			main_circ.rz(0.917000, 2)
			main_circ.y(3)
			main_circ.cy(1,2)
			main_circ.cy(0,3)
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cy(3,2)
			main_circ.y(0)
		with else_1:
			main_circ.cy(2,qreg_0[0])
			main_circ.cy(qreg_0[0],2)
			main_circ.y(3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.u(0.878000,param_3,0.685000, qreg_0[0])
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.y(qreg_0[0])
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cy(0,1)
			main_circ.append(subcirc0,[3,0,qreg_0[0],1])
		with else_1:
			main_circ.rz(param_4, 2)
			main_circ.rz(param_2, 2)
			main_circ.append(subcirc0,[2,qreg_0[0],3,0])
	with else_2:
		main_circ.u(param_0,-0.888000,param_1, 0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cy(3,qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(-0.300000,param_0,param_2, qreg_0[0])
			main_circ.rz(param_4, 0)
			main_circ.rz(0.877000, qreg_0[0])
		with else_1:
			main_circ.u(-0.709000,-0.976000,param_4, 2)
			main_circ.barrier(qreg_0[0])
	with else_2:
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.599000, param_1: -0.461000, param_2: -0.804000, param_3: 0.594000, param_4: -0.558000, param_5: -0.180000, param_6: 0.107000, param_7: 0.811000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "683", "Collect2qBlocks")
