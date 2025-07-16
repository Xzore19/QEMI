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
subcirc0.rz(0.633000, qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.rz(0.936000, qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.rz(param_1, 1)
		with else_1:
			main_circ.barrier(2)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(param_1, 0)
				main_circ.cz(2,0)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(0.362000, 3)
				main_circ.rz(0.649000, 2)
				main_circ.cz(3,0)
				main_circ.rx(param_1, 1)
			with case_1(1):
				main_circ.rz(param_1, 3)
				main_circ.cx(0,2)
				main_circ.cx(1,0)
				main_circ.cx(0,1)
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(3,1)
				main_circ.rz(param_0, 1)
				main_circ.rz(-0.688000, 0)
				main_circ.rz(param_0, 1)
			with case_1(1):
				main_circ.cx(0,2)
				main_circ.cz(2,1)
				main_circ.cx(3,2)
				main_circ.rz(0.363000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rx(-0.319000, 0)
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cz(3,1)
				main_circ.rx(param_1, 2)
				main_circ.rz(param_1, 2)
				main_circ.rz(param_1, 3)
			with case_1(1):
				main_circ.cx(1,2)
				main_circ.cz(0,3)
				main_circ.rx(-0.443000, 1)
				main_circ.rx(0.469000, 2)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cz(3,0)
						main_circ.rz(-0.151000, 1)
						main_circ.rz(param_1, 1)
						main_circ.id(2)
					with case_1(1):
						main_circ.rz(0.854000, 1)
						main_circ.rx(0.609000, 3)
						main_circ.barrier(2)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.rz(param_0, 0)
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.rx(-0.599000, 2)
				main_circ.rz(param_0, 3)
				main_circ.cx(1,3)
	with case_3(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.rx(0.617000, 2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.rx(param_1, 2)
					main_circ.rz(0.901000, 3)
					main_circ.barrier(2)
				with else_1:
					main_circ.id(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cx(0,2)
					main_circ.barrier(2)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.rz(-0.639000, 0)
						main_circ.rz(-0.638000, 0)
						main_circ.barrier(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.id(2)
bindings = {param_0: -0.326000, param_1: 0.496000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1854", "Collect1qRuns")
