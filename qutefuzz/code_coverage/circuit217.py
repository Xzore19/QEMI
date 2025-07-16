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
subcirc0.u(0.459000,0.207000,0.799000, qreg_0[1])
subcirc0.rz(-0.658000, qreg_2[1])
subcirc0.rz(-0.943000, qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_2[1])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.922000,-0.192000,0.122000, qreg_0[1])
subcirc1.rz(0.234000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.rz(-0.451000, qreg_0[2])
subcirc1.u(0.869000,0.283000,-0.824000, qreg_0[2])
subcirc1.rz(0.613000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cx(qreg_2[1],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_2[1])
subcirc2.rz(0.563000, qreg_0[1])
subcirc2.cx(qreg_2[1],qreg_0[0])
subcirc2.rz(-0.308000, qreg_2[1])
subcirc2.rz(0.549000, qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[0],qreg_1[1])
		main_circ.u(param_0,0.912000,0.908000, qreg_1[0])
		main_circ.barrier(qreg_1[1])
	with case_1(1):
		main_circ.id(qreg_1[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(qreg_1[0],qreg_0[0])
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_1[1])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.barrier(qreg_1[2])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_1[2],qreg_1[1])
		main_circ.u(param_0,param_0,-0.858000, qreg_1[0])
		main_circ.u(param_0,param_0,param_0, qreg_0[0])
		main_circ.barrier(qreg_1[2])
	with case_1(1):
		main_circ.id(qreg_1[2])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(0.573000, qreg_1[0])
		main_circ.id(qreg_1[0])
	with case_1(1):
		main_circ.cz(qreg_1[2],qreg_1[1])
		main_circ.u(param_0,0.276000,param_0, qreg_1[0])
		main_circ.cz(qreg_0[0],qreg_1[2])
		main_circ.u(param_0,0.725000,param_0, qreg_1[2])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_1[0],qreg_0[0])
	main_circ.cx(qreg_1[1],qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_0[0],qreg_1[1])
	main_circ.id(qreg_0[0])
main_circ.rz(-0.923000, qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,0.669000,param_0, qreg_1[2])
	main_circ.cx(qreg_1[2],qreg_1[1])
	main_circ.cz(qreg_0[0],qreg_1[2])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(qreg_1[0],qreg_1[1])
	main_circ.append(subcirc1,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_1[0])
main_circ.cx(qreg_1[1],qreg_0[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_1[2])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_0, qreg_1[0])
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
with else_1:
	main_circ.u(0.534000,-0.615000,-0.073000, qreg_1[1])
	main_circ.cx(qreg_0[0],qreg_1[2])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_1[2])
with else_1:
	main_circ.u(param_0,param_0,-0.458000, qreg_1[2])
	main_circ.append(subcirc1,[qreg_1[2],qreg_0[0],qreg_1[0],qreg_1[1]])
bindings = {param_0: 0.607000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "217", "OptimizeCliffords")
