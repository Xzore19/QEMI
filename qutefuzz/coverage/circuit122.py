from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rz(0.133000, qreg_3[0])
subcirc0.rz(-0.062000, qreg_0[0])
subcirc0.rz(0.850000, qreg_0[0])
subcirc0.z(qreg_3[0])
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

main_circ.cz(3,0)
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.append(subcirc0,[1,0,3,qreg_0[0],2])
	with case_4(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.y(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.append(subcirc0,[3,qreg_0[0],0,1,2])
			with else_2:
				main_circ.append(subcirc0,[1,0,qreg_0[0],3,2])
		with else_3:
			main_circ.rz(param_0, qreg_0[0])
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cz(3,2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.z(0)
					main_circ.y(0)
					main_circ.cz(3,qreg_0[0])
				with else_1:
					main_circ.append(subcirc0,[qreg_0[0],2,1,3,0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rz(param_0, 3)
				with else_1:
					main_circ.append(subcirc0,[2,1,0,3,qreg_0[0]])
					main_circ.z(0)
		with else_3:
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.z(1)
							main_circ.append(subcirc0,[0,1,qreg_0[0],3,2])
						with case_1(1):
							main_circ.y(qreg_0[0])
							main_circ.append(subcirc0,[1,0,2,qreg_0[0],3])
				with case_2(1):
					main_circ.cz(2,qreg_0[0])
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.cz(2,0)
						main_circ.cz(3,2)
						main_circ.cz(2,1)
						main_circ.cz(1,qreg_0[0])
					with else_1:
						main_circ.cz(0,1)
						main_circ.cz(2,qreg_0[0])
						main_circ.cz(3,0)
						main_circ.cz(0,1)
	with case_4(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.cz(3,2)
								main_circ.cz(2,qreg_0[0])
								main_circ.cz(2,qreg_0[0])
								main_circ.cz(qreg_0[0],1)
							with case_1(1):
								main_circ.rz(param_0, 0)
								main_circ.z(qreg_0[0])
								main_circ.id(2)
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(0)
						main_circ.barrier(2)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.id(3)
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.id(2)
				main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.844000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "122", "Optimize1qGatesSimpleCommutation")
