from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_1,0,0.010000, 1)
		main_circ.u(0,0,-0.950000, qreg_0[0])
		main_circ.u(0,param_0,param_0, 2)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rx(-0.305000, qreg_0[0])
			main_circ.rx(param_1, 3)
			main_circ.rz(-0.247000, 2)
			main_circ.rz(0.375000, 2)
		with else_1:
			main_circ.ry(param_0, 2)
main_circ.rx(-0.698000, 3)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(0.588000, 3)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_0,param_1,param_1, 2)
			main_circ.rx(-0.640000, qreg_0[0])
		with else_1:
			main_circ.rx(param_0, 3)
			main_circ.rx(0.066000, 0)
		main_circ.rx(param_1, 3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.u(param_1,param_1,0.523000, 3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(0.632000, 3)
					main_circ.rz(0.801000, qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_1, 1)
					main_circ.rx(-0.811000, 1)
					main_circ.rz(0.609000, 1)
					main_circ.u(0,param_1,param_1, 1)
					main_circ.u(0,0,-0.699000, 1)
			with case_2(1):
				main_circ.rx(-0.890000, 1)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(0,param_0,-0.873000, 3)
						main_circ.rx(0.818000, 3)
						main_circ.rz(-0.588000, 2)
						main_circ.rz(param_0, 0)
					with case_1(1):
						main_circ.rz(param_0, 3)
						main_circ.rx(0.461000, 2)
						main_circ.rz(-0.895000, 2)
						main_circ.ry(param_1, 2)
	with case_3(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(param_0, 3)
				main_circ.rz(0.353000, 0)
				main_circ.rx(0.662000, 0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(param_0, qreg_0[0])
				main_circ.rx(0.748000, 2)
			with else_1:
				main_circ.rz(-0.231000, 1)
				main_circ.rz(param_0, 1)
				main_circ.ry(param_1, 1)
				main_circ.rx(0.124000, 2)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(0.746000, 1)
					main_circ.rx(param_1, qreg_0[0])
					main_circ.rx(param_0, 1)
					main_circ.ry(-0.331000, qreg_0[0])
				with case_1(1):
					main_circ.rz(param_0, 0)
					main_circ.ry(param_1, qreg_0[0])
					main_circ.u(param_1,param_1,0.956000, 2)
					main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.559000, param_1: 0.302000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1018")
