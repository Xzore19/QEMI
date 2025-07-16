from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.324000, qreg_1[1])
subcirc0.ry(0.763000, qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_1[0])
subcirc0.ry(-0.719000, qreg_0[0])
subcirc0.u(0,0,0.764000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.348000, qreg_3[0])
subcirc1.u(0,0,-0.686000, qreg_0[2])
subcirc1.ry(-0.990000, qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.ry(0.142000, qreg_3[0])
subcirc2.z(qreg_0[1])
subcirc2.u(0,0,0.913000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cx(qreg_0[2],qreg_0[0])
subcirc3.u(0,0,0.868000, qreg_0[2])
subcirc3.z(qreg_0[3])
subcirc3.z(qreg_0[2])
subcirc3.u(0,0,0.890000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_1[1],qreg_0[0])
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],1,0])
		with case_1(1):
			main_circ.barrier(1)
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.ry(param_0, 1)
		main_circ.u(param_0,param_0,-0.226000, qreg_1[1])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_0,0,param_0, 0)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[0,qreg_3[0],qreg_1[0],qreg_0[0]])
			with case_1(1):
				main_circ.u(0,0,-0.961000, 0)
				main_circ.ry(param_0, 0)
				main_circ.append(subcirc0,[qreg_0[0],1,qreg_1[1],qreg_1[0]])
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc0,[1,0,qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(qreg_1[1])
main_circ.append(subcirc1,[qreg_1[0],qreg_3[0],1,qreg_1[1]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_0[0],qreg_1[1])
			main_circ.cx(qreg_0[0],qreg_3[0])
			main_circ.cx(1,qreg_0[0])
			main_circ.cx(qreg_0[0],qreg_1[1])
		with case_1(1):
			main_circ.cx(qreg_1[1],qreg_3[0])
			main_circ.cx(qreg_0[0],qreg_1[1])
			main_circ.cx(qreg_1[0],1)
			main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_1[0],0])
bindings = {param_0: 0.783000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1652")
