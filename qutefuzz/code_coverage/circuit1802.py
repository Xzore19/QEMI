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
subcirc0.u(pi/2,0.183000,-0.497000, qreg_0[1])
subcirc0.u(pi/2,-0.877000,-0.660000, qreg_0[1])
subcirc0.cz(qreg_3[0],qreg_0[2])
subcirc0.ry(0.787000, qreg_0[2])
subcirc0.ry(-0.956000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.ry(-0.627000, qreg_1[0])
subcirc1.cx(qreg_1[1],qreg_1[0])
subcirc1.u(pi/2,0.759000,-0.525000, qreg_0[0])
subcirc1.u(pi/2,-0.078000,-0.464000, qreg_0[0])
subcirc1.ry(-0.185000, qreg_1[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_2[1],qreg_0[0],0,qreg_2[0]])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_2[0],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],0,qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_3,param_2,param_1, qreg_2[1])
with else_1:
	main_circ.cx(qreg_0[1],0)
	main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_0[1],0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(qreg_0[0],qreg_2[1])
	main_circ.ry(param_1, qreg_0[0])
	main_circ.u(pi/2,param_2,param_1, qreg_2[0])
	main_circ.u(pi/2,-0.832000,0.596000, 0)
	main_circ.cx(qreg_2[0],0)
with else_1:
	main_circ.append(subcirc1,[qreg_2[1],0,qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[1],qreg_2[0])
	main_circ.cx(qreg_2[1],0)
	main_circ.cz(0,qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.cx(0,qreg_0[1])
		main_circ.cz(0,qreg_0[0])
		main_circ.cx(qreg_2[1],qreg_0[1])
	with case_1(1):
		main_circ.cx(qreg_0[1],0)
		main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_2[1],0])
bindings = {param_1: 0.716000, param_2: 0.773000, param_3: 0.622000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1802", "NormalizeRXAngle")
