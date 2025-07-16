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
subcirc0.rz(-0.136000, qreg_0[0])
subcirc0.u(pi/2,0.542000,0.581000, qreg_3[0])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0.u(0.791000,0.267000,-0.658000, qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_1[0],qreg_1[2],qreg_0[0],0])
with else_1:
	main_circ.u(pi/2,0.516000,param_0, qreg_1[0])
	main_circ.u(param_3,-0.981000,param_0, qreg_1[2])
	main_circ.u(0.831000,param_0,0.290000, 0)
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_3,-0.172000,param_3, qreg_0[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_1[1],qreg_1[0])
		main_circ.u(param_3,param_3,param_4, qreg_1[2])
		main_circ.u(pi/2,param_2,param_3, qreg_1[1])
		main_circ.u(pi/2,0.615000,0.872000, qreg_0[0])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.492000,param_0,0.908000, qreg_1[1])
	main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],0,qreg_1[0]])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],0,qreg_0[0]])
with else_1:
	main_circ.u(param_2,-0.288000,0.664000, qreg_0[0])
	main_circ.cy(qreg_1[1],0)
	main_circ.append(subcirc0,[qreg_0[0],0,qreg_1[1],qreg_1[0]])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.230000,param_4,0.502000, qreg_1[1])
	main_circ.rz(-0.704000, qreg_1[0])
	main_circ.cy(qreg_0[0],0)
	main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_0[0],qreg_1[2]])
with else_1:
	main_circ.u(param_3,param_0,-0.549000, qreg_1[2])
main_circ.u(-0.592000,0.880000,0.694000, 0)
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc0,[0,qreg_1[1],qreg_1[2],qreg_1[0]])
bindings = {param_0: 0.049000, param_2: 0.697000, param_3: 0.036000, param_4: 0.751000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "836")
