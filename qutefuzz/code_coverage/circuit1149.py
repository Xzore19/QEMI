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
subcirc0.rz(0.325000, qreg_0[1])
subcirc0.u(0,0,-0.288000, qreg_0[3])
subcirc0.rz(0.272000, qreg_0[2])
subcirc0.rz(-0.019000, qreg_0[0])
subcirc0.u(0,0,0.287000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_3, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(1)
with else_1:
	main_circ.u(param_0,param_0,0.290000, 3)
	main_circ.ry(param_2, 2)
	main_circ.barrier(2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_2, 0)
	main_circ.rz(param_0, 1)
	main_circ.ry(param_0, 1)
	main_circ.u(param_1,0,0.751000, 0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(0.718000, 1)
	main_circ.rz(param_2, 3)
	main_circ.id(3)
with else_1:
	main_circ.u(0,param_2,0.947000, 2)
	main_circ.ry(-0.294000, 0)
	main_circ.ry(param_5, 3)
	main_circ.ry(param_3, 1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_0, 3)
		main_circ.u(param_2,param_2,param_0, 0)
		main_circ.rz(-0.133000, 2)
		main_circ.ry(param_2, 0)
	with case_1(1):
		main_circ.id(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,0,-0.748000, 2)
	main_circ.id(0)
with else_1:
	main_circ.u(param_2,param_2,param_2, 3)
	main_circ.u(0,0,param_4, 0)
	main_circ.u(-0.827000,param_5,0.089000, 0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_4, 1)
		main_circ.u(-0.965000,-0.481000,-0.937000, 3)
		main_circ.rz(-0.683000, 0)
		main_circ.u(param_0,0.666000,-0.936000, 2)
	with case_1(1):
		main_circ.barrier(0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(0)
with else_1:
	main_circ.ry(-0.733000, 3)
	main_circ.rz(param_2, 3)
	main_circ.ry(param_4, 0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.968000, 3)
		main_circ.rz(-0.798000, 3)
		main_circ.u(-0.189000,param_0,0.213000, 2)
		main_circ.ry(-0.769000, 3)
	with case_1(1):
		main_circ.u(param_5,param_5,-0.324000, 0)
		main_circ.ry(-0.719000, 1)
		main_circ.rz(param_5, 3)
		main_circ.u(0,param_1,param_1, 0)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0.468000,param_4,0.304000, 0)
		main_circ.u(0,0,0.672000, 2)
		main_circ.id(3)
	with case_1(1):
		main_circ.u(-0.097000,param_0,0.272000, 1)
		main_circ.u(0,param_4,0.986000, 1)
		main_circ.u(param_5,0,0.631000, 2)
		main_circ.u(param_5,0,0.314000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.u(-0.597000,param_4,param_0, 0)
main_circ.rz(0.025000, 1)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(3)
	with case_1(1):
		main_circ.u(param_2,0,param_2, 2)
		main_circ.u(param_4,param_2,0.153000, 1)
		main_circ.ry(-0.811000, 2)
		main_circ.barrier(1)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rz(0.963000, 0)
		main_circ.u(0.671000,param_0,param_3, 1)
		main_circ.barrier(1)
	with case_1(1):
		main_circ.id(2)
bindings = {param_0: 0.600000, param_1: -0.704000, param_2: -0.797000, param_3: 0.331000, param_4: -0.248000, param_5: -0.439000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1149")
