from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.ry(param_4, qreg_0[2])
main_circ.s(0)
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_0,-0.726000,0.604000, qreg_0[2])
			with else_1:
				main_circ.u(param_0,0,param_1, qreg_0[1])
				main_circ.s(qreg_0[3])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.ry(-0.452000, qreg_0[1])
						main_circ.u(param_5,param_3,param_2, 1)
						main_circ.ry(param_3, 0)
						main_circ.s(qreg_0[0])
					with case_1(1):
						main_circ.s(qreg_0[0])
						main_circ.u(param_4,param_3,-0.837000, qreg_0[0])
						main_circ.s(qreg_0[2])
						main_circ.u(param_3,-0.495000,-0.252000, qreg_0[0])
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(1)
						main_circ.s(0)
						main_circ.u(pi/2,param_1,param_0, qreg_0[2])
						main_circ.u(param_3,param_5,0.844000, 1)
					with case_1(1):
						main_circ.ry(0.095000, qreg_0[3])
						main_circ.ry(0.840000, 0)
						main_circ.s(qreg_0[2])
						main_circ.ry(param_1, qreg_0[2])
	with case_3(1):
		main_circ.s(qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.s(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_1,param_0,0.440000, qreg_0[3])
			main_circ.s(qreg_0[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.ry(0.912000, qreg_0[2])
					main_circ.u(pi/2,-0.916000,-0.318000, qreg_0[2])
					main_circ.ry(-0.037000, qreg_0[0])
					main_circ.ry(param_4, 0)
				with case_1(1):
					main_circ.u(param_4,param_2,-0.309000, qreg_0[0])
					main_circ.u(param_2,param_5,-0.633000, 1)
					main_circ.u(param_0,param_1,-0.483000, qreg_0[3])
					main_circ.s(qreg_0[1])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(0,0,param_1, qreg_0[0])
			main_circ.u(param_1,param_3,-0.636000, qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(qreg_0[1])
				main_circ.u(pi/2,param_4,param_0, qreg_0[0])
				main_circ.u(0,param_5,param_2, qreg_0[0])
				main_circ.s(qreg_0[1])
			with else_1:
				main_circ.u(pi/2,param_4,-0.167000, qreg_0[0])
				main_circ.u(0,param_2,0.727000, qreg_0[1])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, qreg_0[1])
				main_circ.u(pi/2,param_1,-0.272000, qreg_0[3])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(pi/2,param_2,param_1, qreg_0[2])
				main_circ.ry(param_5, qreg_0[3])
			with else_1:
				main_circ.u(0,0,param_5, 1)
				main_circ.s(1)
				main_circ.ry(param_5, qreg_0[3])
				main_circ.ry(-0.798000, qreg_0[3])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(pi/2,param_1,0.966000, 1)
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(0)
			with case_2(1):
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.id(qreg_0[3])
		main_circ.id(qreg_0[2])
bindings = {param_0: -0.746000, param_1: -0.351000, param_2: 0.283000, param_3: -0.795000, param_4: 0.298000, param_5: 0.421000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "790")
