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
subcirc0.rz(0.664000, qreg_0[2])
subcirc0.u(0,0,0.008000, qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.u(0,0,-0.413000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_1[0])
subcirc1.rz(0.097000, qreg_3[0])
subcirc1.rz(0.635000, qreg_1[0])
subcirc1.rz(0.442000, qreg_1[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0,0,-0.018000, qreg_1[2])
subcirc2.u(0,0,-0.183000, qreg_1[2])
subcirc2.cz(qreg_0[0],qreg_1[1])
subcirc2.rz(0.168000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(-0.479000, qreg_2[1])
subcirc3.x(qreg_2[0])
subcirc3.u(0,0,-0.656000, qreg_1[0])
subcirc3.cz(qreg_0[0],qreg_2[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,-0.700000, qreg_3[0])
subcirc4.x(qreg_0[2])
subcirc4.x(qreg_0[0])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],0,qreg_0[1]])
main_circ.u(0,0,param_2, qreg_0[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.barrier(qreg_3[0])
			with case_3(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_3[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.rz(0.093000, 0)
							main_circ.cz(qreg_0[1],1)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_0[2])
						with else_1:
							main_circ.rz(0.368000, qreg_0[0])
							main_circ.x(qreg_0[1])
							main_circ.x(0)
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.cz(qreg_3[0],1)
							main_circ.append(subcirc3,[1,qreg_0[2],qreg_3[0],qreg_0[1]])
	with case_4(1):
		main_circ.u(0,param_0,param_3, qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.rz(0.447000, qreg_0[0])
							main_circ.u(param_2,param_0,0.695000, 1)
							main_circ.u(param_4,param_0,param_0, qreg_3[0])
							main_circ.rz(param_2, 1)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
				with else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.u(param_1,0,param_0, qreg_0[2])
							main_circ.append(subcirc3,[0,qreg_3[0],qreg_0[2],1])
						with case_1(1):
							main_circ.cz(qreg_0[2],qreg_3[0])
							main_circ.cz(qreg_3[0],qreg_0[2])
							main_circ.cz(1,0)
							main_circ.cz(qreg_0[0],qreg_0[2])
			with case_3(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.cz(1,qreg_0[2])
							main_circ.cz(qreg_0[2],1)
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.x(qreg_0[2])
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.rz(param_1, 1)
					with case_2(1):
						main_circ.append(subcirc3,[qreg_0[0],0,qreg_3[0],1])
main_circ.cz(0,qreg_0[0])
bindings = {param_0: 0.683000, param_1: 0.171000, param_2: -0.133000, param_3: -0.316000, param_4: 0.541000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "149", "ConsolidateBlocks")
