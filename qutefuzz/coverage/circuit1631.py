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
subcirc0.rz(0.571000, qreg_0[0])
subcirc0.cx(qreg_1[2],qreg_1[0])
subcirc0.cx(qreg_1[0],qreg_1[2])
subcirc0.ry(-0.393000, qreg_0[0])
subcirc0.rz(-0.587000, qreg_1[1])
subcirc0.ry(0.132000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_2[0])
subcirc1.ry(0.148000, qreg_2[1])
subcirc1.h(qreg_0[0])
subcirc1.ry(-0.471000, qreg_2[0])
subcirc1.h(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[3])
subcirc2.h(qreg_0[3])
subcirc2.rz(0.465000, qreg_0[3])
subcirc2.h(qreg_0[2])
subcirc2.ry(0.454000, qreg_0[2])
subcirc2.rz(-0.774000, qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_1[1],qreg_1[0])
subcirc3.rz(0.427000, qreg_0[0])
subcirc3.rz(-0.065000, qreg_0[0])
subcirc3.ry(0.064000, qreg_1[1])
subcirc3.h(qreg_3[0])
subcirc3.h(qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.h(qreg_1[2])
subcirc4.cx(qreg_0[0],qreg_1[2])
subcirc4.h(qreg_0[0])
subcirc4.ry(0.661000, qreg_0[0])
subcirc4.h(qreg_1[2])
subcirc4.ry(-0.379000, qreg_1[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc2,[1,3,0,2])
					with case_1(1):
						main_circ.append(subcirc2,[1,3,0,qreg_0[0]])
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.ry(param_6, 1)
						main_circ.append(subcirc2,[0,2,3,1])
					with case_1(1):
						main_circ.append(subcirc3,[0,1,2,3])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.append(subcirc4,[qreg_0[0],0,1,3,2])
with else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[0,3,qreg_0[0],1])
				with case_1(1):
					main_circ.append(subcirc4,[qreg_0[0],2,0,1,3])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cx(0,qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(2,0)
						main_circ.cx(2,qreg_0[0])
						main_circ.cx(0,1)
						main_circ.cx(1,qreg_0[0])
					with case_1(1):
						main_circ.cx(0,2)
						main_circ.cx(0,3)
						main_circ.cx(2,0)
						main_circ.cx(2,1)
			with case_2(1):
				main_circ.cx(3,0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(2)
				main_circ.barrier(qreg_0[0])
	with else_3:
		main_circ.barrier(1)
bindings = {param_6: 0.004000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1631", "CollectMultiQBlocks")
