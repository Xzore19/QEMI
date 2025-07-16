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
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_2[0])
subcirc0.x(qreg_0[0])
subcirc0.rz(0.432000, qreg_0[0])
subcirc0.x(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
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

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.rz(-0.959000, qreg_0[0])
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_1,param_2,0.690000, 0)
							main_circ.x(1)
							main_circ.u(param_2,0,0.880000, 2)
							main_circ.cx(3,1)
						with case_1(1):
							main_circ.append(subcirc0,[0,qreg_1[0],1,3])
				with case_2(1):
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.u(param_0,param_1,0.291000, qreg_1[0])
						main_circ.x(qreg_0[0])
					with else_1:
						main_circ.rz(param_1, 2)
						main_circ.u(param_2,param_1,param_1, 2)
						main_circ.cx(3,2)
						main_circ.rz(param_0, qreg_1[0])
		with case_3(1):
			main_circ.rz(param_0, 3)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.x(qreg_0[0])
						main_circ.u(0,param_2,-0.300000, qreg_0[0])
						main_circ.rz(param_1, 1)
						main_circ.append(subcirc0,[0,2,1,qreg_0[0]])
					with case_1(1):
						main_circ.rz(-0.211000, 3)
						main_circ.rz(param_1, 3)
						main_circ.u(param_1,0,param_2, 1)
						main_circ.u(0,0,param_0, 2)
			with else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0,param_1,param_2, qreg_1[0])
					main_circ.u(0,param_0,0.996000, qreg_0[0])
					main_circ.cx(2,1)
				main_circ.x(qreg_0[0])
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cx(3,qreg_1[0])
						main_circ.cx(qreg_0[0],2)
						main_circ.cx(0,qreg_1[0])
						main_circ.cx(3,qreg_0[0])
					with case_1(1):
						main_circ.cx(1,0)
						main_circ.cx(0,2)
						main_circ.cx(0,3)
						main_circ.cx(3,2)
with else_4:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(qreg_0[0],0)
				main_circ.cx(3,2)
				main_circ.cx(qreg_0[0],qreg_1[0])
				main_circ.u(param_1,param_0,0.013000, qreg_1[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.x(qreg_0[0])
					main_circ.cx(2,qreg_1[0])
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(qreg_0[0])
		with else_2:
			main_circ.id(2)
bindings = {param_0: -0.688000, param_1: 0.776000, param_2: -0.236000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1958", "Collect1qRuns")
