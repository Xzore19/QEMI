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
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_2[1])
subcirc0.u(0,0,0.609000, qreg_2[0])
subcirc0.u(pi/2,0.472000,-0.063000, qreg_2[0])
subcirc0.u(pi/2,-0.203000,-0.532000, qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.069000,-0.922000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1.u(pi/2,0.739000,0.808000, qreg_0[1])
subcirc1.u(0,0,-0.170000, qreg_0[2])
subcirc1.u(pi/2,0.763000,0.870000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.cx(qreg_2[0],qreg_2[1])
subcirc2.u(0,0,0.438000, qreg_2[0])
subcirc2.u(pi/2,0.543000,-0.128000, qreg_1[0])
subcirc2.u(0,0,-0.447000, qreg_0[0])
subcirc2.u(0,0,0.851000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(0,0,0.218000, qreg_2[0])
subcirc3.u(0,0,0.226000, qreg_0[0])
subcirc3.cx(qreg_2[1],qreg_0[0])
subcirc3.cx(qreg_1[0],qreg_2[0])
subcirc3.cx(qreg_1[0],qreg_2[0])
subcirc3.cx(qreg_0[0],qreg_2[1])

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")

main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
with else_1:
	main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(qreg_0[0])
	main_circ.y(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0]])
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
with else_1:
	main_circ.cx(qreg_2[0],qreg_0[1])
	main_circ.u(param_1,0,param_2, qreg_0[0])
	main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],qreg_3[0],qreg_0[1]])
bindings = {param_1: 0.326000, param_2: 0.093000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "927")
