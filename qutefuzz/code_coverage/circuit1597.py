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
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.rx(0.235000, qreg_0[2])
subcirc0.u(0,0,0.825000, qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[1])
subcirc0.rx(-0.149000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.587000, qreg_3[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.u(0,0,-0.073000, qreg_3[0])
subcirc1.cz(qreg_2[0],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_0[0],qreg_0[1])
subcirc2.cz(qreg_3[0],qreg_0[2])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2.cz(qreg_0[0],qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_1,0,param_2, 3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.rx(param_2, 3)
	with else_3:
		main_circ.append(subcirc2,[1,0,2,3])
with else_4:
	main_circ.cx(1,2)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.u(param_1,param_1,param_2, 1)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.append(subcirc0,[3,2,0,1])
			with case_3(1):
				main_circ.u(0,param_2,-0.031000, 0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.rx(param_0, 3)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.rx(0.954000, 1)
								main_circ.rx(param_0, 2)
								main_circ.u(param_1,0,-0.850000, 3)
								main_circ.u(0,param_0,-0.298000, 0)
							with case_1(1):
								main_circ.append(subcirc2,[1,2,3,0])
					with case_2(1):
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.u(0,param_1,0.329000, 0)
								main_circ.cz(1,3)
								main_circ.append(subcirc2,[1,0,3,2])
							with case_1(1):
								main_circ.append(subcirc2,[3,2,0,1])
	with case_4(1):
		main_circ.cx(3,1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.rx(param_1, 1)
			with else_2:
				main_circ.append(subcirc0,[1,3,2,0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.cx(1,3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc2,[2,0,3,1])
					with case_1(1):
						main_circ.cx(1,0)
						main_circ.cx(1,2)
						main_circ.cz(2,0)
						main_circ.id(3)
			with else_2:
				main_circ.id(1)
		with case_3(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.barrier(1)
				with case_2(1):
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.barrier(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.id(1)
			with else_2:
				main_circ.id(1)
			main_circ.barrier(0)
bindings = {param_0: -0.874000, param_1: 0.804000, param_2: 0.320000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1597", "CommutativeCancellation")
