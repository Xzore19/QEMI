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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.u(0.836000,0.345000,0.131000, qreg_0[2])
subcirc0.x(qreg_0[2])
subcirc0.u(-0.994000,-0.523000,-0.970000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_1,param_0,0.141000, 2)
	main_circ.append(subcirc0,[1,qreg_0[0],2,qreg_1[0],0])
with else_1:
	main_circ.cx(2,3)
	main_circ.cx(2,1)
	main_circ.append(subcirc0,[qreg_0[0],3,1,0,qreg_1[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(1)
	main_circ.u(param_1,0.522000,param_0, 1)
	main_circ.u(param_2,param_2,0.381000, 3)
main_circ.h(0)
main_circ.cx(qreg_0[0],3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[2,qreg_0[0],0,qreg_1[0],3])
with else_1:
	main_circ.cx(2,qreg_0[0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_0,param_1,0.198000, 3)
	main_circ.h(2)
	main_circ.u(param_1,param_0,-0.267000, qreg_0[0])
with else_1:
	main_circ.cx(2,qreg_0[0])
	main_circ.u(param_2,-0.915000,param_0, 1)
	main_circ.append(subcirc0,[1,qreg_0[0],qreg_1[0],0,2])
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_1[0],0,3,1,qreg_0[0]])
	with case_1(1):
		main_circ.id(3)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,0.742000,param_1, 0)
	main_circ.u(param_0,param_1,0.455000, 3)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(2,0)
	main_circ.id(qreg_1[0])
with else_1:
	main_circ.barrier(3)
bindings = {param_0: 0.266000, param_1: -0.690000, param_2: -0.910000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1064")
