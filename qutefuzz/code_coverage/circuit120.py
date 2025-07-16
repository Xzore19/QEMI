from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.s(qreg_1[0])
subcirc0.u(pi/2,0.450000,0.716000, qreg_1[0])
subcirc0.u(-0.747000,-0.530000,-0.107000, qreg_2[0])
subcirc0.ry(0.239000, qreg_2[0])
subcirc0.ry(-0.022000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(1)
	main_circ.s(qreg_0[0])
	main_circ.u(0.058000,param_2,param_0, qreg_0[1])
	main_circ.u(pi/2,-0.276000,param_0, 3)
with else_1:
	main_circ.s(0)
	main_circ.s(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[3,qreg_0[0],0,2])
with else_1:
	main_circ.u(pi/2,-0.656000,-0.538000, 2)
	main_circ.append(subcirc0,[0,1,qreg_0[1],qreg_0[0]])
main_circ.ry(-0.303000, 1)
main_circ.ry(0.416000, 3)
main_circ.u(param_3,-0.391000,0.482000, 1)
main_circ.u(param_0,0.121000,0.035000, 2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,-0.936000,param_3, 2)
		main_circ.u(0.768000,0.902000,0.183000, 1)
		main_circ.u(pi/2,0.527000,0.605000, 3)
		main_circ.ry(param_1, 3)
	with case_1(1):
		main_circ.ry(param_0, qreg_0[1])
		main_circ.s(0)
		main_circ.ry(-0.718000, 0)
		main_circ.s(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[1],2,0,qreg_0[0]])
with else_1:
	main_circ.append(subcirc0,[qreg_0[1],2,1,3])
main_circ.ry(-0.986000, qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.334000,param_2,param_1, 3)
	main_circ.u(param_1,0.047000,0.789000, 3)
bindings = {param_0: 0.346000, param_1: 0.708000, param_2: -0.347000, param_3: 0.246000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "120", "CommutativeInverseCancellation")
