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
subcirc0.u(0,0,-0.747000, qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,0.262000, qreg_0[0])
subcirc0.u(0.719000,-0.598000,-0.467000, qreg_3[0])
subcirc0.h(qreg_0[0])
subcirc0.y(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.u(0,0,0.978000, qreg_0[2])
subcirc1.h(qreg_0[2])
subcirc1.u(0.652000,0.183000,0.597000, qreg_0[3])
subcirc1.u(0,0,-0.337000, qreg_0[0])
subcirc1.u(0,0,-0.747000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[2])
subcirc2.u(0,0,0.671000, qreg_0[3])
subcirc2.y(qreg_0[3])
subcirc2.u(0.651000,0.909000,0.049000, qreg_0[3])
subcirc2.u(0,0,-0.175000, qreg_0[0])
subcirc2.u(0,0,-0.606000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_0[0])
subcirc3.u(0,0,-0.299000, qreg_0[0])
subcirc3.h(qreg_3[0])
subcirc3.u(0,0,-0.446000, qreg_2[0])
subcirc3.h(qreg_0[1])
subcirc3.u(0,0,-0.927000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(-0.677000,0.899000,-0.186000, qreg_0[0])
subcirc4.h(qreg_1[1])
subcirc4.u(0,0,-0.674000, qreg_3[0])
subcirc4.y(qreg_1[1])
subcirc4.h(qreg_3[0])
subcirc4.y(qreg_1[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
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

main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_1[2],0,qreg_1[0],1])
				with case_1(1):
					main_circ.h(qreg_1[0])
					main_circ.h(qreg_0[0])
					main_circ.y(qreg_1[0])
					main_circ.append(subcirc2,[1,qreg_1[1],qreg_0[0],qreg_1[0]])
		with else_2:
			main_circ.measure(qreg_1[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_1[2])
			with else_1:
				main_circ.append(subcirc2,[0,qreg_1[0],1,qreg_0[0]])
	with else_3:
		main_circ.id(qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.barrier(0)
with else_4:
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.append(subcirc1,[1,qreg_0[0],0,qreg_1[1]])
			with case_2(1):
				main_circ.measure(qreg_1[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc3,[0,qreg_1[2],1,qreg_1[1],qreg_1[0]])
				with else_1:
					main_circ.h(qreg_1[0])
					main_circ.y(0)
					main_circ.h(0)
					main_circ.append(subcirc1,[qreg_1[2],0,qreg_0[0],1])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],0,1,qreg_0[0]])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "634")
