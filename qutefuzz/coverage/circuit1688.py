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
subcirc0.rz(-0.205000, qreg_1[0])
subcirc0.rz(-0.465000, qreg_1[2])
subcirc0.u(pi/2,0.323000,0.847000, qreg_1[2])
subcirc0.rz(0.435000, qreg_1[1])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rz(-0.506000, qreg_2[0])
subcirc1.rz(-0.891000, qreg_0[1])
subcirc1.rz(0.476000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.u(pi/2,-0.528000,-0.264000, qreg_0[1])
subcirc1.x(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.352000, qreg_0[2])
subcirc2.x(qreg_0[0])
subcirc2.u(pi/2,0.500000,-0.194000, qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[1])
subcirc2.u(pi/2,0.053000,-0.074000, qreg_0[2])
subcirc2.x(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.837000,-0.762000, qreg_3[0])
subcirc3.rz(0.352000, qreg_3[0])
subcirc3.cz(qreg_0[1],qreg_2[0])
subcirc3.rz(0.819000, qreg_3[0])
subcirc3.cz(qreg_2[0],qreg_0[1])
subcirc3.u(pi/2,-0.420000,0.468000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cz(qreg_0[2],qreg_0[0])
subcirc4.u(pi/2,0.505000,0.121000, qreg_0[3])
subcirc4.rz(0.203000, qreg_0[1])
subcirc4.u(pi/2,-0.962000,-0.847000, qreg_0[1])
subcirc4.x(qreg_0[2])
subcirc4.cz(qreg_0[3],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rz(param_0, 1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.id(3)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[1,3,qreg_0[0],0])
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc3,[0,qreg_0[0],qreg_1[0],2,3,1])
with else_1:
	main_circ.cz(qreg_0[0],qreg_1[0])
	main_circ.append(subcirc2,[1,qreg_0[0],qreg_1[0],0,2])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.u(param_0,0.906000,param_0, 2)
		main_circ.id(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[1,qreg_0[0],3,0])
main_circ.append(subcirc2,[1,3,0,2,qreg_1[0]])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_0, qreg_1[0])
		main_circ.cz(2,3)
		main_circ.cz(1,qreg_1[0])
		main_circ.cz(qreg_0[0],0)
	with case_1(1):
		main_circ.cz(2,qreg_0[0])
		main_circ.cz(qreg_1[0],1)
		main_circ.cz(2,0)
		main_circ.cz(0,qreg_1[0])
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.u(param_0,0.096000,param_0, 0)
		main_circ.cz(1,2)
		main_circ.barrier(2)
	with case_1(1):
		main_circ.id(qreg_1[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.barrier(2)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,param_0,-0.292000, 1)
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.barrier(3)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(3)
	main_circ.rz(-0.417000, 3)
	main_circ.x(qreg_0[0])
with else_1:
	main_circ.barrier(1)
bindings = {param_0: 0.815000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1688")
