from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rx(0.219000, qreg_2[1])
subcirc0.u(0,0,0.105000, qreg_0[1])
subcirc0.u(0,0,-0.576000, qreg_0[1])
subcirc0.u(pi/2,-0.840000,-0.542000, qreg_0[0])
subcirc0.u(0,0,0.884000, qreg_2[0])

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
param_5 = Parameter("param_5")

main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc0,[0,3,2,1])
			with else_1:
				main_circ.u(0,param_4,0.641000, 2)
				main_circ.ry(0.635000, 2)
				main_circ.u(param_0,0,-0.520000, 0)
	with case_3(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_2, 2)
					main_circ.rx(param_3, 3)
				main_circ.append(subcirc0,[0,1,3,2])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,param_2,param_3, 2)
						main_circ.append(subcirc0,[1,3,2,0])
					with case_1(1):
						main_circ.u(param_5,0,0.180000, 0)
						main_circ.append(subcirc0,[2,1,3,0])
main_circ.u(0,0,0.185000, 2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(-0.538000, 2)
				main_circ.append(subcirc0,[1,2,3,0])
			with case_1(1):
				main_circ.u(param_3,param_2,0.982000, 0)
				main_circ.ry(param_4, 0)
				main_circ.append(subcirc0,[1,2,0,3])
	with else_2:
		main_circ.rx(param_0, 3)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.ry(0.438000, 2)
			main_circ.ry(param_4, 1)
			main_circ.rx(param_1, 0)
			main_circ.u(param_4,param_0,0.647000, 1)
			main_circ.rx(0.111000, 2)
		with else_1:
			main_circ.barrier(3)
bindings = {param_0: -0.343000, param_1: -0.056000, param_2: -0.407000, param_3: -0.846000, param_4: 0.373000, param_5: -0.261000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1824")
