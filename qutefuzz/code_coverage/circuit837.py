from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cx(qreg_1[0],qreg_2[0])
subcirc0.u(0.515000,-0.171000,-0.020000, qreg_2[0])
subcirc0.u(pi/2,0.329000,-0.024000, qreg_2[0])
subcirc0.u(pi/2,0.904000,-0.497000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.119000,-0.942000,0.187000, qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[2])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.u(pi/2,0.016000,0.564000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_3[0],qreg_1[0])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[0])
subcirc2.u(pi/2,0.561000,0.328000, qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.235000,0.209000,0.639000, qreg_0[0])
subcirc3.cz(qreg_3[0],qreg_0[2])
subcirc3.u(pi/2,0.674000,-0.173000, qreg_0[1])
subcirc3.cz(qreg_0[2],qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cx(qreg_0[3],qreg_0[0])
subcirc4.u(pi/2,-0.342000,-0.671000, qreg_0[1])
subcirc4.u(0.633000,-0.133000,-0.692000, qreg_0[3])
subcirc4.cz(qreg_0[3],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,0.640000,param_0, 0)
		main_circ.cx(1,0)
		main_circ.append(subcirc3,[2,1,0,3])
	with case_1(1):
		main_circ.id(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc2,[3,0,2,1])
	main_circ.cz(3,0)
with else_1:
	main_circ.cx(0,2)
	main_circ.id(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(2)
with else_1:
	main_circ.u(param_0,param_0,param_0, 2)
	main_circ.u(pi/2,param_0,param_0, 2)
	main_circ.id(2)
main_circ.cz(1,0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc2,[2,1,0,3])
with else_1:
	main_circ.append(subcirc2,[1,3,2,0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(3,0)
		main_circ.append(subcirc3,[0,2,3,1])
	with case_1(1):
		main_circ.u(param_0,0.319000,param_0, 0)
		main_circ.append(subcirc2,[0,2,3,1])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(1,3)
with else_1:
	main_circ.u(0.726000,param_0,param_0, 2)
	main_circ.barrier(1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc3,[2,1,0,3])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(0)
with else_1:
	main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.barrier(3)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(0)
	with case_1(1):
		main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(3,0)
		main_circ.barrier(1)
	with case_1(1):
		main_circ.barrier(0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(pi/2,0.378000,0.205000, 1)
bindings = {param_0: 0.328000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "837")
