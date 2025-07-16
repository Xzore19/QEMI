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
subcirc0.u(pi/2,0.757000,-0.244000, qreg_0[3])
subcirc0.rz(-0.598000, qreg_0[3])
subcirc0.rz(-0.503000, qreg_0[3])
subcirc0.u(pi/2,-0.554000,0.726000, qreg_0[3])
subcirc0.rz(-0.281000, qreg_0[0])
subcirc0.h(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.892000, qreg_0[2])
subcirc1.rz(0.235000, qreg_3[0])
subcirc1.h(qreg_0[2])
subcirc1.rx(0.294000, qreg_0[2])
subcirc1.rx(-0.659000, qreg_0[2])
subcirc1.rz(-0.049000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

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
param_4 = Parameter("param_4")

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.append(subcirc0,[3,0,qreg_0[1],2])
with else_4:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[0],2,3,qreg_0[1]])
			with else_1:
				main_circ.u(pi/2,0.502000,param_2, 0)
				main_circ.append(subcirc0,[3,qreg_0[0],qreg_0[1],1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_1,0.214000,param_2, 3)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.append(subcirc1,[0,2,3,qreg_0[1],qreg_0[0],1])
	with case_4(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.rx(param_2, qreg_0[1])
						main_circ.append(subcirc1,[2,qreg_0[1],qreg_0[0],1,0,3])
					with case_1(1):
						main_circ.rx(-0.079000, qreg_0[0])
						main_circ.h(qreg_0[0])
						main_circ.append(subcirc0,[qreg_0[1],2,qreg_0[0],0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.h(qreg_0[0])
					main_circ.rz(param_3, 3)
					main_circ.h(2)
					main_circ.barrier(2)
bindings = {param_1: -0.864000, param_2: 0.664000, param_3: -0.107000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1294")
