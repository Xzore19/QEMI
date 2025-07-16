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
subcirc0.h(qreg_0[1])
subcirc0.z(qreg_0[3])
subcirc0.rz(-0.022000, qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[3])

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

main_circ.z(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.z(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(2)
						main_circ.append(subcirc0,[0,qreg_0[0],2,1])
					with case_1(1):
						main_circ.append(subcirc0,[0,3,2,1])
			with case_2(1):
				main_circ.append(subcirc0,[qreg_0[0],3,2,1])
with else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(3)
					main_circ.append(subcirc0,[qreg_0[0],0,1,3])
				with else_1:
					main_circ.rz(param_0, 2)
					main_circ.append(subcirc0,[2,1,3,0])
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.z(3)
					main_circ.cz(1,3)
				with else_1:
					main_circ.cz(qreg_0[0],1)
					main_circ.cz(qreg_0[0],1)
					main_circ.cz(2,0)
					main_circ.cz(1,2)
		with case_3(1):
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.cz(3,qreg_0[0])
						main_circ.cz(qreg_0[0],0)
						main_circ.cz(qreg_0[0],0)
						main_circ.cz(qreg_0[0],3)
				with case_2(1):
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.cz(0,qreg_0[0])
							main_circ.cz(qreg_0[0],2)
							main_circ.cz(0,1)
							main_circ.cz(qreg_0[0],1)
						with case_1(1):
							main_circ.barrier(0)
bindings = {param_0: -0.774000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1806", "Optimize1qGatesDecomposition")
