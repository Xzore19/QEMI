from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.rz(-0.396000, qreg_0[0])
subcirc0.ry(-0.262000, qreg_3[0])
subcirc0.u(-0.254000,-0.101000,-0.649000, qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_2[0])
subcirc0.rz(-0.954000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.691000, qreg_1[1])
subcirc1.ry(0.500000, qreg_0[0])
subcirc1.u(-0.505000,-0.280000,-0.718000, qreg_1[0])
subcirc1.rz(0.654000, qreg_1[0])
subcirc1.u(-0.049000,-0.087000,0.496000, qreg_1[0])
subcirc1.ry(-0.647000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.738000,-0.484000,-0.212000, qreg_3[0])
subcirc2.rz(-0.354000, qreg_0[1])
subcirc2.u(-0.222000,-0.528000,0.091000, qreg_0[0])
subcirc2.cx(qreg_3[0],qreg_0[0])
subcirc2.rz(0.182000, qreg_0[1])
subcirc2.cx(qreg_3[0],qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(0.909000, qreg_2[0])
subcirc3.rz(0.359000, qreg_2[0])
subcirc3.cx(qreg_2[0],qreg_0[0])
subcirc3.cx(qreg_1[0],qreg_2[0])
subcirc3.rz(-0.135000, qreg_1[0])
subcirc3.ry(0.380000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.726000, qreg_0[1])
subcirc4.ry(0.665000, qreg_0[1])
subcirc4.cx(qreg_0[1],qreg_3[0])
subcirc4.rz(0.258000, qreg_3[0])
subcirc4.u(-0.870000,0.778000,-0.594000, qreg_3[0])
subcirc4.u(-0.832000,0.354000,0.150000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc4,[1,qreg_0[3],qreg_0[1],0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_0[0],1)
	main_circ.rz(param_0, qreg_0[2])
	main_circ.u(param_0,-0.139000,-0.107000, qreg_0[1])
	main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],1,qreg_0[1],qreg_0[2]])
main_circ.rz(param_0, 1)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc4,[qreg_0[2],qreg_0[0],0,1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(0.692000, qreg_0[0])
	main_circ.append(subcirc1,[qreg_0[0],1,qreg_0[1],qreg_0[3],0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.rz(param_0, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc4,[qreg_0[0],qreg_0[3],qreg_0[2],1])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_0, qreg_0[2])
	main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],0,qreg_0[3],qreg_0[0]])
with else_1:
	main_circ.cx(qreg_0[1],0)
	main_circ.cx(qreg_0[3],qreg_0[1])
	main_circ.cx(0,1)
	main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(1,qreg_0[2])
	main_circ.cx(qreg_0[3],qreg_0[0])
	main_circ.cx(0,qreg_0[2])
	main_circ.cx(qreg_0[0],1)
main_circ.cx(0,qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.cx(qreg_0[0],qreg_0[3])
		main_circ.cx(1,0)
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.u(param_0,0.527000,param_0, qreg_0[1])
		main_circ.id(qreg_0[2])
bindings = {param_0: 0.795000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "187", "ConsolidateBlocks")
