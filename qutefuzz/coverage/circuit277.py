from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,0.106000,0.642000, qreg_0[3])
subcirc0.u(pi/2,0.163000,0.875000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cz(3,1)
			main_circ.s(1)
			main_circ.cz(3,0)
			main_circ.cz(qreg_0[0],0)
		with case_1(1):
			main_circ.append(subcirc0,[qreg_0[0],0,3,2,1])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,param_1,0.817000, 2)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(qreg_0[0])
			main_circ.append(subcirc0,[1,0,2,3,qreg_0[0]])
		with else_1:
			main_circ.cz(qreg_0[0],1)
			main_circ.u(param_1,param_0,-0.936000, 3)
			main_circ.u(param_0,0.635000,0.898000, qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc0,[2,qreg_0[0],3,0,1])
		with else_1:
			main_circ.cz(qreg_0[0],3)
			main_circ.s(2)
			main_circ.cz(1,2)
			main_circ.s(2)
			main_circ.s(2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.cz(0,2)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.y(3)
			main_circ.u(pi/2,-0.053000,-0.336000, 2)
			main_circ.append(subcirc0,[2,qreg_0[0],0,1,3])
	with case_2(1):
		main_circ.y(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cz(qreg_0[0],3)
			main_circ.y(1)
			main_circ.cz(1,3)
			main_circ.y(qreg_0[0])
		with else_1:
			main_circ.cz(qreg_0[0],0)
			main_circ.cz(2,0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cz(3,1)
		main_circ.append(subcirc0,[qreg_0[0],3,0,2,1])
	with else_1:
		main_circ.append(subcirc0,[3,qreg_0[0],1,2,0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.s(3)
		main_circ.s(qreg_0[0])
		main_circ.y(2)
		main_circ.u(pi/2,param_1,param_1, qreg_0[0])
		main_circ.cz(3,1)
	with else_1:
		main_circ.y(3)
		main_circ.id(3)
bindings = {param_0: 0.588000, param_1: 0.818000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "277", "ElidePermutations")
