from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cx(qreg_1[1],qreg_3[0])
subcirc0.rx(0.256000, qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cx(2,1)
	main_circ.ry(0.294000, qreg_0[0])
	main_circ.ry(param_2, 3)
	main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(0)
	main_circ.append(subcirc0,[1,qreg_0[0],2,3,0,qreg_0[1]])
with else_1:
	main_circ.rx(0.874000, 2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.458000, 0)
	main_circ.cx(1,2)
	main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[3,0,qreg_0[1],2,1,qreg_0[0]])
	with case_1(1):
		main_circ.ry(-0.048000, qreg_0[1])
		main_circ.cx(2,0)
		main_circ.ry(param_0, qreg_0[1])
		main_circ.y(qreg_0[1])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(3)
		main_circ.cx(2,1)
		main_circ.cx(0,qreg_0[1])
		main_circ.cx(3,2)
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],3,1,0,2])
main_circ.append(subcirc0,[qreg_0[0],2,3,0,qreg_0[1],1])
main_circ.cx(2,0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(0,1)
	main_circ.y(qreg_0[0])
	main_circ.rx(-0.747000, qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[1,0,qreg_0[0],2,qreg_0[1],3])
	with case_1(1):
		main_circ.rx(0.844000, 1)
		main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.856000, param_2: 0.969000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1429", "ResetAfterMeasureSimplification")
