from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_2[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(0.740000, qreg_0[1])
subcirc0.u(pi/2,0.997000,0.066000, qreg_0[0])
subcirc0.s(qreg_0[1])

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

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(3)
		main_circ.u(param_1,0.117000,param_6, 0)
		main_circ.u(pi/2,0.073000,param_4, qreg_0[0])
		main_circ.append(subcirc0,[3,2,qreg_0[0],1])
	with case_1(1):
		main_circ.u(pi/2,-0.306000,param_5, 0)
		main_circ.u(pi/2,-0.189000,-0.596000, 0)
		main_circ.rz(param_5, 2)
		main_circ.s(2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(pi/2,0.168000,0.908000, 0)
	main_circ.append(subcirc0,[2,3,qreg_0[0],0])
with else_1:
	main_circ.s(1)
	main_circ.z(2)
	main_circ.u(param_4,param_6,0.525000, 1)
	main_circ.u(param_5,param_2,0.885000, 2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,-0.433000,param_1, 2)
	main_circ.z(3)
	main_circ.s(1)
	main_circ.rz(param_1, 2)
	main_circ.u(param_5,param_1,0.575000, 1)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],2,0,3])
	with case_1(1):
		main_circ.u(pi/2,param_5,param_1, 1)
		main_circ.rz(0.724000, 1)
		main_circ.append(subcirc0,[1,0,3,qreg_0[0]])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(3)
	main_circ.s(1)
	main_circ.append(subcirc0,[2,0,1,qreg_0[0]])
main_circ.s(3)
main_circ.rz(param_2, qreg_0[0])
bindings = {param_1: -0.559000, param_2: -0.554000, param_4: -0.775000, param_5: -0.843000, param_6: -0.988000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1743")
