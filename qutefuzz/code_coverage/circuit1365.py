from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(pi/2,0.931000,-0.681000, qreg_0[0])
subcirc0.u(-0.115000,0.752000,-0.400000, qreg_1[0])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.x(qreg_1[2])
subcirc1.u(-0.883000,0.908000,-0.620000, qreg_0[0])
subcirc1.x(qreg_1[2])
subcirc1.u(-0.191000,-0.286000,0.527000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.108000,-0.162000, qreg_0[2])
subcirc2.u(-0.875000,0.173000,0.639000, qreg_3[0])
subcirc2.u(pi/2,0.899000,0.665000, qreg_0[0])
subcirc2.x(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_3[0])
subcirc3.x(qreg_0[2])
subcirc3.h(qreg_0[1])
subcirc3.u(pi/2,0.349000,0.923000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(1)
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
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,0.936000,param_0, qreg_2[0])
	main_circ.x(0)
	main_circ.x(qreg_0[1])
	main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_0[1],0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(qreg_0[0])
	main_circ.u(param_1,param_0,param_0, qreg_0[0])
	main_circ.x(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_2[0],0,qreg_0[1],qreg_0[0]])
	with case_1(1):
		main_circ.u(param_2,param_0,-0.334000, qreg_2[0])
		main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],0,qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(0)
	main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_2[0],0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_0[0],0])
	with case_1(1):
		main_circ.x(qreg_2[0])
		main_circ.h(qreg_3[0])
		main_circ.u(pi/2,param_1,0.398000, qreg_2[0])
		main_circ.append(subcirc3,[0,qreg_3[0],qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],0,qreg_0[1]])
	with case_1(1):
		main_circ.u(-0.005000,0.105000,param_0, qreg_0[1])
		main_circ.u(-0.402000,0.150000,param_0, qreg_3[0])
		main_circ.x(qreg_3[0])
		main_circ.append(subcirc2,[qreg_3[0],qreg_2[0],0,qreg_0[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[1])
		main_circ.h(qreg_0[0])
		main_circ.x(qreg_3[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.059000, param_1: -0.326000, param_2: -0.682000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1365", "TemplateOptimization")
