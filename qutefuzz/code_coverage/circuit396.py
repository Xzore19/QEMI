from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(0,3)
	main_circ.y(1)
	main_circ.cz(2,1)
	main_circ.y(qreg_0[1])
	main_circ.h(qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(qreg_0[1],0)
	main_circ.y(3)
	main_circ.cz(qreg_0[1],3)
	main_circ.cz(2,qreg_0[1])
	main_circ.cx(1,3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(1,qreg_0[1])
		main_circ.y(2)
		main_circ.h(2)
		main_circ.cz(qreg_0[1],2)
	with case_1(1):
		main_circ.cx(1,qreg_0[1])
		main_circ.y(0)
		main_circ.cx(2,3)
		main_circ.h(qreg_0[0])
main_circ.h(3)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[0])
		main_circ.y(1)
		main_circ.cx(qreg_0[0],0)
		main_circ.h(qreg_0[0])
	with case_1(1):
		main_circ.cx(1,qreg_0[1])
		main_circ.h(2)
		main_circ.cz(qreg_0[0],0)
		main_circ.h(qreg_0[1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(2)
	main_circ.cz(0,1)
	main_circ.cx(1,qreg_0[0])
	main_circ.cz(1,0)
	main_circ.y(2)
main_circ.cx(0,qreg_0[0])
main_circ.y(1)
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cz(1,3)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],2)
		main_circ.cz(qreg_0[1],1)
		main_circ.y(1)
		main_circ.y(0)
	with case_1(1):
		main_circ.h(3)
		main_circ.cz(3,0)
		main_circ.h(qreg_0[1])
		main_circ.cz(2,qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(2,0)
	main_circ.cx(qreg_0[1],2)
	main_circ.y(3)
	main_circ.cx(3,2)
	main_circ.y(qreg_0[1])
with else_1:
	main_circ.barrier(qreg_0[1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "396")
