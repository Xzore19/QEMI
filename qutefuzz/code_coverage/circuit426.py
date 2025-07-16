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
subcirc0.u(0.728000,0.716000,0.639000, qreg_0[0])
subcirc0.u(-0.423000,0.309000,-0.801000, qreg_2[0])
subcirc0.ry(0.674000, qreg_0[0])
subcirc0.ry(-0.200000, qreg_2[0])
subcirc0.rz(-0.670000, qreg_2[0])
subcirc0.cz(qreg_2[0],qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.ry(-0.769000, qreg_0[3])
subcirc1.ry(0.372000, qreg_0[2])
subcirc1.rz(-0.592000, qreg_0[0])
subcirc1.ry(0.059000, qreg_0[2])
subcirc1.ry(0.956000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.285000, qreg_3[0])
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.ry(0.671000, qreg_0[2])
subcirc2.rz(0.857000, qreg_0[2])
subcirc2.ry(0.142000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.314000,-0.325000,0.843000, qreg_0[0])
subcirc3.u(0.112000,0.903000,-0.048000, qreg_3[0])
subcirc3.rz(0.135000, qreg_3[0])
subcirc3.ry(0.201000, qreg_0[1])
subcirc3.rz(0.347000, qreg_0[2])
subcirc3.cz(qreg_0[0],qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.rz(-0.403000, qreg_1[2])
subcirc4.rz(0.023000, qreg_1[0])
subcirc4.rz(-0.392000, qreg_1[1])
subcirc4.ry(0.064000, qreg_1[2])
subcirc4.cz(qreg_1[1],qreg_1[0])
subcirc4.cz(qreg_0[0],qreg_1[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_3[0])
with else_1:
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.ry(param_2, qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
	with case_1(1):
		main_circ.ry(-0.119000, qreg_0[2])
		main_circ.u(-0.832000,param_1,param_3, qreg_0[0])
		main_circ.cz(qreg_0[1],qreg_0[2])
		main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[2])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[2],qreg_0[1])
		main_circ.cz(qreg_0[2],qreg_0[1])
		main_circ.cz(qreg_0[1],qreg_0[2])
		main_circ.cz(qreg_0[0],qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc3,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
bindings = {param_1: 0.296000, param_2: 0.189000, param_3: 0.060000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "426")
