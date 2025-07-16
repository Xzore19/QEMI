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
subcirc0.u(pi/2,-0.912000,0.289000, qreg_0[1])
subcirc0.u(pi/2,0.980000,-0.990000, qreg_3[0])
subcirc0.ry(0.873000, qreg_3[0])
subcirc0.u(pi/2,0.987000,0.244000, qreg_2[0])
subcirc0.cz(qreg_0[0],qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(-0.412000, qreg_0[0])
subcirc1.ry(-0.889000, qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_1[1])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cz(qreg_1[0],qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.861000, qreg_0[1])
subcirc2.u(pi/2,0.555000,0.508000, qreg_0[1])
subcirc2.rz(0.660000, qreg_0[1])
subcirc2.u(pi/2,-0.219000,-0.055000, qreg_0[1])
subcirc2.u(pi/2,0.678000,-0.419000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],1,0])
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc1,[qreg_2[0],qreg_3[0],1,qreg_0[1]])
				with else_1:
					main_circ.barrier(1)
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(param_3,-0.076000,param_0, 0)
				with else_1:
					main_circ.cz(qreg_3[0],qreg_2[0])
					main_circ.cz(qreg_2[0],qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc2,[qreg_3[0],1,0,qreg_0[1],qreg_2[0]])
				with else_1:
					main_circ.cz(0,qreg_3[0])
main_circ.cz(qreg_3[0],1)
main_circ.u(param_4,-0.458000,param_2, qreg_0[1])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.append(subcirc2,[0,1,qreg_0[0],qreg_0[1],qreg_3[0]])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.cz(qreg_0[0],qreg_0[1])
					main_circ.measure(qreg_2[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.append(subcirc2,[qreg_2[0],qreg_3[0],1,qreg_0[0],0])
						with case_1(1):
							main_circ.cz(qreg_3[0],0)
							main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],0,qreg_3[0]])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.append(subcirc1,[qreg_0[0],1,0,qreg_3[0]])
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.938000, param_2: -0.850000, param_3: 0.908000, param_4: 0.502000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1582", "Collect1qRuns")
