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
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.u(-0.410000,0.255000,-0.203000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0.025000,-0.325000,-0.895000, qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.u(0.107000,0.476000,-0.264000, qreg_2[0])
subcirc1.u(-0.666000,0.233000,0.186000, qreg_0[1])
subcirc1.z(qreg_2[0])
subcirc1.u(-0.417000,0.214000,-0.906000, qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_1[0])
subcirc2.x(qreg_1[0])
subcirc2.x(qreg_1[1])
subcirc2.u(-0.477000,-0.138000,0.158000, qreg_3[0])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.u(-0.216000,-0.254000,-0.002000, qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.u(-0.040000,0.665000,-0.477000, qreg_0[0])
subcirc3.cy(qreg_0[3],qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.x(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0.255000,0.664000,param_2, qreg_0[0])
	main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_0[1]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(-0.611000,param_1,param_2, qreg_2[1])
		main_circ.x(qreg_2[0])
		main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_2[1],qreg_0[0]])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
	with case_1(1):
		main_circ.u(param_2,param_2,-0.254000, qreg_2[1])
		main_circ.u(0.778000,0.620000,param_1, qreg_2[1])
		main_circ.cy(qreg_2[1],qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(qreg_0[1],qreg_2[0])
	main_circ.cy(qreg_2[0],qreg_0[0])
	main_circ.cy(qreg_2[0],qreg_2[1])
	main_circ.cy(qreg_0[0],qreg_2[1])
with else_1:
	main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_2[0],qreg_0[1])
	main_circ.cy(qreg_2[1],qreg_0[1])
	main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,param_0,param_0, qreg_0[0])
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],qreg_2[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.cy(qreg_0[0],qreg_2[1])
		main_circ.u(0.467000,param_0,param_2, qreg_2[0])
		main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.469000, param_1: -0.531000, param_2: -0.259000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "503", "ConsolidateBlocks")
