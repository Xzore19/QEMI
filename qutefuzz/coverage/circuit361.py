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
subcirc0.u(pi/2,0.752000,-0.496000, qreg_2[1])
subcirc0.u(pi/2,-0.240000,0.410000, qreg_2[1])
subcirc0.u(pi/2,-0.131000,0.398000, qreg_2[0])
subcirc0.u(pi/2,-0.921000,-0.041000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_3[0])
subcirc2.u(pi/2,-0.702000,0.075000, qreg_3[0])
subcirc2.u(pi/2,-0.158000,0.464000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(pi/2,-0.582000,-0.767000, qreg_0[1])
subcirc3.x(qreg_2[0])
subcirc3.y(qreg_0[0])
subcirc3.x(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cy(qreg_0[0],qreg_0[2])
subcirc4.y(qreg_0[1])
subcirc4.u(pi/2,0.573000,0.535000, qreg_0[2])
subcirc4.u(pi/2,0.870000,0.287000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,param_0,0.104000, qreg_3[0])
	main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_1[1],qreg_0[0]])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_0,-0.097000, qreg_1[1])
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_1[0],qreg_1[1]])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_3[0],qreg_1[0]])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(qreg_1[0])
	main_circ.u(param_2,-0.709000,param_1, qreg_3[0])
with else_1:
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc2,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc2,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_3[0]])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_3[0]])
	with case_1(1):
		main_circ.cy(qreg_3[0],qreg_1[1])
		main_circ.cy(qreg_1[1],qreg_0[0])
		main_circ.cy(qreg_3[0],qreg_1[1])
		main_circ.cy(qreg_1[1],qreg_1[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_1[0])
	with case_1(1):
		main_circ.id(qreg_3[0])
main_circ.y(qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_3[0]])
with else_1:
	main_circ.cy(qreg_1[1],qreg_0[0])
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.barrier(qreg_1[1])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_1[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_1[1])
	with case_1(1):
		main_circ.cy(qreg_1[0],qreg_1[1])
		main_circ.id(qreg_1[1])
bindings = {param_0: 0.369000, param_1: 0.363000, param_2: 0.899000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "361", "Optimize1qGatesSimpleCommutation")
