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
subcirc0.ry(0.119000, qreg_3[0])
subcirc0.u(-0.139000,-0.831000,0.556000, qreg_3[0])
subcirc0.ry(-0.751000, qreg_0[0])
subcirc0.y(qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0.u(-0.156000,-0.687000,-0.490000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.110000,-0.991000,-0.588000, qreg_0[1])
subcirc1.ry(0.256000, qreg_2[0])
subcirc1.x(qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_0[0])
subcirc1.ry(0.223000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.x(qreg_1[2])
subcirc2.x(qreg_0[0])
subcirc2.u(-0.498000,0.940000,-0.194000, qreg_0[0])
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.713000,-0.821000,-0.204000, qreg_3[0])
subcirc3.y(qreg_0[1])
subcirc3.y(qreg_0[1])
subcirc3.u(-0.438000,0.495000,-0.273000, qreg_2[0])
subcirc3.y(qreg_3[0])
subcirc3.y(qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.append(subcirc3,[0,qreg_0[2],qreg_0[3],1])
	with else_1:
		main_circ.ry(param_1, 1)
		main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[3],1])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc1,[1,qreg_0[1],qreg_0[2],qreg_0[3]])
	with else_1:
		main_circ.append(subcirc3,[qreg_0[2],0,qreg_0[3],qreg_0[1]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_2,0.848000,0.242000, qreg_0[0])
	with else_1:
		main_circ.y(1)
	main_circ.append(subcirc2,[0,qreg_0[2],qreg_0[0],qreg_0[3]])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc0,[qreg_0[3],0,1,qreg_0[0]])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[2],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(0)
		main_circ.append(subcirc0,[0,1,qreg_0[0],qreg_0[3]])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(1)
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.ry(param_3, qreg_0[3])
		main_circ.barrier(qreg_0[1])
	with else_1:
		main_circ.barrier(1)
bindings = {param_1: 0.968000, param_2: 0.176000, param_3: -0.365000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1981")
