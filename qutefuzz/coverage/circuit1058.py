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
subcirc0.ry(0.371000, qreg_0[0])
subcirc0.rx(-0.630000, qreg_1[0])
subcirc0.u(pi/2,0.206000,0.844000, qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_1[0],qreg_1[1])
subcirc1.rx(0.569000, qreg_1[1])
subcirc1.cy(qreg_3[0],qreg_1[1])
subcirc1.rx(0.790000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.882000, qreg_3[0])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.ry(-0.115000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(pi/2,0.207000,-0.352000, qreg_0[0])
subcirc3.rx(0.548000, qreg_2[1])
subcirc3.u(pi/2,0.820000,0.308000, qreg_0[1])
subcirc3.cy(qreg_2[1],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_3[0],0,1])
				with case_1(1):
					main_circ.cy(qreg_0[1],1)
					main_circ.u(param_0,param_0,-0.669000, qreg_3[0])
					main_circ.append(subcirc3,[1,qreg_2[0],0,qreg_0[0],qreg_0[1],qreg_3[0]])
with else_4:
	main_circ.append(subcirc1,[qreg_0[1],1,0,qreg_0[0],qreg_3[0]])
	main_circ.append(subcirc1,[0,1,qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],0,1,qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_0[1]])
		main_circ.append(subcirc2,[qreg_0[1],1,0,qreg_3[0]])
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cy(qreg_0[1],qreg_2[0])
				main_circ.ry(0.557000, 1)
			with else_1:
				main_circ.cy(qreg_2[0],qreg_0[0])
				main_circ.append(subcirc3,[qreg_0[0],1,0,qreg_0[1],qreg_3[0],qreg_2[0]])
with else_4:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],1,qreg_2[0],qreg_3[0]])
				with case_1(1):
					main_circ.append(subcirc0,[1,0,qreg_0[1],qreg_2[0]])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],1,0])
				with case_1(1):
					main_circ.append(subcirc1,[qreg_2[0],qreg_3[0],qreg_0[1],1,qreg_0[0]])
	with else_3:
		main_circ.rx(0.202000, 0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_2[0],0,1,qreg_0[0],qreg_0[1]])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.552000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1058", "InverseCancellation")
