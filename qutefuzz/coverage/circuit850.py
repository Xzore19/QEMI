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
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.u(0,0,0.357000, qreg_0[3])
subcirc0.cy(qreg_0[0],qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
with else_1:
	main_circ.cx(qreg_1[1],qreg_0[0])
	main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[0],qreg_1[1]])
main_circ.rx(-0.707000, qreg_1[1])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(0.311000, qreg_1[0])
	main_circ.rx(-0.051000, qreg_0[0])
	main_circ.u(0,0,param_0, qreg_0[0])
	main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
	with case_1(1):
		main_circ.rx(-0.085000, qreg_0[0])
		main_circ.u(0,param_0,-0.758000, qreg_1[1])
		main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[1],qreg_1[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0,0,param_0, qreg_0[0])
	main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
with else_1:
	main_circ.cy(qreg_0[0],qreg_1[0])
	main_circ.u(param_0,param_0,0.341000, qreg_1[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(qreg_3[0],qreg_1[1])
	main_circ.rx(param_0, qreg_3[0])
	main_circ.u(0,param_1,param_1, qreg_0[0])
with else_1:
	main_circ.rx(param_1, qreg_0[0])
	main_circ.append(subcirc0,[qreg_3[0],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cy(qreg_0[0],qreg_3[0])
	main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
with else_1:
	main_circ.rx(param_0, qreg_1[0])
	main_circ.cy(qreg_1[1],qreg_3[0])
	main_circ.id(qreg_3[0])
bindings = {param_0: 0.584000, param_1: -0.038000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "850", "NormalizeRXAngle")
