from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rx(0.043000, qreg_0[0])
subcirc0.rx(-0.813000, qreg_2[0])
subcirc0.ry(-0.956000, qreg_2[0])
subcirc0.cz(qreg_1[0],qreg_2[1])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cx(0,1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.ry(-0.080000, 1)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(1,3)
						main_circ.barrier(2)
					with case_1(1):
						main_circ.rx(param_0, 0)
						main_circ.cx(2,3)
						main_circ.ry(param_0, 3)
						main_circ.cz(1,2)
			with case_2(1):
				main_circ.id(1)
	with else_3:
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.ry(param_0, 3)
					main_circ.rx(0.953000, 2)
					main_circ.cz(2,1)
					main_circ.ry(param_0, 1)
				with case_1(1):
					main_circ.cz(0,2)
					main_circ.ry(param_0, 3)
					main_circ.cz(3,1)
					main_circ.cx(2,0)
		with else_2:
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.rx(-0.286000, 2)
				main_circ.cx(1,3)
				main_circ.barrier(1)
			main_circ.rx(-0.614000, 0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(1,2)
			with else_1:
				main_circ.barrier(1)
with else_4:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.ry(param_0, 2)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(3,0)
			with else_1:
				main_circ.id(2)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.ry(param_0, 2)
	with else_3:
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(0,1)
				main_circ.cx(3,2)
				main_circ.rx(-0.880000, 2)
			with else_1:
				main_circ.rx(param_0, 0)
				main_circ.rx(0.321000, 1)
				main_circ.cx(3,1)
				main_circ.cx(2,3)
		with else_2:
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cz(0,1)
					main_circ.barrier(2)
				with case_1(1):
					main_circ.ry(param_0, 0)
					main_circ.rx(-0.652000, 3)
					main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(2)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cx(3,2)
					main_circ.barrier(1)
				with case_1(1):
					main_circ.cx(0,3)
					main_circ.rx(-0.151000, 0)
					main_circ.cx(1,3)
					main_circ.id(0)
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.cz(1,2)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.ry(-0.025000, 0)
					main_circ.cz(2,3)
					main_circ.cx(2,3)
					main_circ.id(3)
			with else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(param_0, 0)
					main_circ.id(3)
				main_circ.ry(param_0, 2)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(2,1)
						main_circ.id(0)
					with case_1(1):
						main_circ.id(3)
		with case_3(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(2)
				main_circ.id(1)
			with else_2:
				main_circ.barrier(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.id(2)
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.id(2)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.barrier(2)
				with case_2(1):
					main_circ.barrier(1)
			main_circ.id(2)
with else_4:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.id(3)
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.barrier(2)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.barrier(2)
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.barrier(2)
		with else_2:
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.barrier(2)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(0)
				main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.barrier(2)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.id(1)
		main_circ.barrier(2)
	with else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.id(3)
			with case_2(1):
				main_circ.id(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.id(3)
			main_circ.barrier(1)
		main_circ.id(1)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.barrier(0)
		with else_2:
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.id(2)
		main_circ.id(2)
	main_circ.id(2)
bindings = {param_0: 0.540000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "139")
