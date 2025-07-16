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
subcirc0.rx(0.552000, qreg_1[1])
subcirc0.u(pi/2,-0.631000,0.916000, qreg_1[2])
subcirc0.u(0,0,-0.617000, qreg_1[0])
subcirc0.u(-0.663000,0.600000,-0.073000, qreg_1[0])
subcirc0.u(0,0,-0.734000, qreg_1[2])
subcirc0.u(pi/2,0.805000,-0.550000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.692000,-0.325000, qreg_3[0])
subcirc1.u(0.516000,-0.795000,0.190000, qreg_0[1])
subcirc1.rx(0.980000, qreg_0[1])
subcirc1.u(pi/2,-0.938000,0.144000, qreg_2[0])
subcirc1.u(pi/2,0.880000,0.729000, qreg_2[0])
subcirc1.u(pi/2,-0.620000,0.627000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.578000, qreg_1[0])
subcirc2.u(pi/2,0.440000,-0.940000, qreg_3[0])
subcirc2.rx(-0.218000, qreg_1[0])
subcirc2.u(0,0,-0.850000, qreg_1[1])
subcirc2.u(pi/2,-0.019000,0.273000, qreg_1[1])
subcirc2.u(-0.119000,-0.427000,0.666000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.876000,0.275000,-0.547000, qreg_0[2])
subcirc3.rx(-0.155000, qreg_0[0])
subcirc3.u(pi/2,-0.562000,0.771000, qreg_0[2])
subcirc3.u(pi/2,0.183000,-0.064000, qreg_0[0])
subcirc3.u(0,0,0.622000, qreg_0[1])
subcirc3.u(pi/2,-0.496000,-0.894000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.u(pi/2,-0.483000,-0.140000, qreg_1[1])
subcirc4.u(pi/2,-0.882000,-0.508000, qreg_1[1])
subcirc4.u(0.913000,-0.753000,0.924000, qreg_1[2])
subcirc4.rx(0.592000, qreg_1[2])
subcirc4.rx(0.524000, qreg_0[0])
subcirc4.rx(0.987000, qreg_1[0])
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
param_5 = Parameter("param_5")

main_circ.append(subcirc3,[1,2,3,0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(0)
		main_circ.rx(-0.542000, 2)
		main_circ.rx(param_1, 3)
	main_circ.append(subcirc1,[0,1,3,2])
main_circ.append(subcirc1,[1,2,0,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.u(0,param_1,param_1, 3)
with else_3:
	main_circ.id(2)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0,0,0.413000, 3)
					main_circ.rx(0.715000, 3)
					main_circ.append(subcirc1,[0,1,3,2])
			with case_2(1):
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.append(subcirc1,[2,0,1,3])
				with else_1:
					main_circ.barrier(2)
	with case_3(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.rx(param_0, 3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_0,0,-0.591000, 2)
				main_circ.append(subcirc1,[1,0,2,3])
			with else_1:
				main_circ.u(pi/2,-0.909000,0.008000, 2)
				main_circ.append(subcirc3,[1,2,3,0])
		with else_2:
			main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.003000,-0.726000,param_2, 0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.barrier(1)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_0,-0.352000,-0.877000, 2)
				main_circ.id(0)
			with else_1:
				main_circ.id(3)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.id(0)
	main_circ.barrier(1)
with else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(2)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(2)
		main_circ.id(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.id(3)
			main_circ.barrier(1)
		with case_2(1):
			main_circ.id(0)
	main_circ.id(2)
bindings = {param_0: 0.322000, param_1: -0.194000, param_2: 0.202000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "374", "ElidePermutations")
