from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.091000,-0.891000, qreg_0[2])
subcirc0.rx(0.130000, qreg_0[0])
subcirc0.rx(-0.729000, qreg_0[0])
subcirc0.u(pi/2,0.757000,0.693000, qreg_0[2])
subcirc0.u(pi/2,0.082000,0.822000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[3])
subcirc1.u(0.701000,1.000000,-0.313000, qreg_0[1])
subcirc1.u(0.265000,0.447000,-0.650000, qreg_0[3])
subcirc1.u(-0.750000,0.695000,-0.632000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.590000,-0.037000,0.887000, qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[3])
subcirc2.u(0.710000,0.776000,-0.087000, qreg_0[0])
subcirc2.rx(0.327000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_3[0])
subcirc3.x(qreg_3[0])
subcirc3.rx(-0.110000, qreg_0[0])
subcirc3.u(pi/2,0.601000,0.403000, qreg_1[1])
subcirc3.u(pi/2,-0.781000,0.476000, qreg_1[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(pi/2,0.947000,-0.559000, qreg_0[1])
subcirc4.rx(0.418000, qreg_0[2])
subcirc4.u(pi/2,0.656000,0.342000, qreg_0[3])
subcirc4.u(-0.657000,0.247000,-0.980000, qreg_0[1])
subcirc4.rx(-0.325000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc3,[qreg_0[1],1,qreg_2[0],0,qreg_3[0],qreg_0[0]])
	with case_1(1):
		main_circ.x(1)
		main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[1,qreg_2[0],0,qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc3,[0,qreg_0[0],qreg_0[1],qreg_3[0],1,qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_0[1]])
	with case_1(1):
		main_circ.u(-0.399000,-0.683000,0.431000, qreg_0[1])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_0,-0.161000,param_1, qreg_3[0])
	main_circ.id(1)
main_circ.rx(param_0, qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.x(qreg_0[1])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.u(param_1,param_0,0.280000, qreg_0[1])
		main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,param_0,param_1, qreg_0[1])
		main_circ.append(subcirc3,[1,qreg_0[1],qreg_2[0],0,qreg_0[0],qreg_3[0]])
	with case_1(1):
		main_circ.rx(param_1, 0)
		main_circ.u(param_1,-0.019000,-0.127000, qreg_0[0])
		main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[0,qreg_3[0],1,qreg_2[0],qreg_0[0]])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],0,1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.x(qreg_0[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.id(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[0],0,1])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0.588000,0.384000,param_0, qreg_0[0])
		main_circ.append(subcirc2,[1,qreg_0[0],0,qreg_2[0],qreg_3[0]])
	with case_1(1):
		main_circ.x(1)
		main_circ.id(qreg_2[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.x(0)
with else_1:
	main_circ.u(param_1,0.993000,param_1, qreg_3[0])
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.737000, param_1: -0.991000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "662", "RemoveResetInZeroState")
