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
subcirc0.y(qreg_1[1])
subcirc0.y(qreg_1[2])
subcirc0.y(qreg_1[2])
subcirc0.cz(qreg_0[0],qreg_1[1])
subcirc0.z(qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.z(qreg_2[0])
subcirc1.cy(qreg_0[1],qreg_2[0])
subcirc1.z(qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_0[2])
subcirc2.y(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[1],qreg_0[0])
subcirc3.z(qreg_0[2])
subcirc3.cy(qreg_0[3],qreg_0[2])
subcirc3.cz(qreg_0[2],qreg_0[3])
subcirc3.cz(qreg_0[1],qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.y(qreg_0[0])
subcirc4.z(qreg_0[1])
subcirc4.y(qreg_3[0])
subcirc4.y(qreg_0[0])
subcirc4.y(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.y(1)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.y(0)
						main_circ.cy(0,2)
						main_circ.id(1)
					with else_1:
						main_circ.id(1)
					main_circ.cz(1,2)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.append(subcirc0,[2,0,3,1])
				with case_2(1):
					main_circ.id(1)
	with case_4(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.z(2)
						main_circ.append(subcirc0,[3,2,1,0])
					with else_1:
						main_circ.cy(1,3)
						main_circ.barrier(0)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.append(subcirc0,[2,1,3,0])
				with else_2:
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.z(2)
							main_circ.barrier(0)
						with case_1(1):
							main_circ.cy(0,1)
							main_circ.append(subcirc3,[0,2,1,3])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.cy(2,1)
								main_circ.barrier(0)
							with case_1(1):
								main_circ.append(subcirc3,[3,0,2,1])
					with case_2(1):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.cy(3,0)
								main_circ.append(subcirc3,[1,0,2,3])
							with case_1(1):
								main_circ.z(3)
								main_circ.cz(2,3)
								main_circ.id(1)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.z(0)
						main_circ.barrier(2)
				with else_2:
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cy(1,2)
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.cz(3,1)
							main_circ.barrier(0)
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.z(0)
							main_circ.cy(0,1)
							main_circ.y(3)
							main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.cy(2,1)
							main_circ.z(3)
							main_circ.y(3)
							main_circ.barrier(2)
						with case_1(1):
							main_circ.z(1)
							main_circ.id(2)
	with case_4(1):
		main_circ.append(subcirc3,[2,3,0,1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1133")
