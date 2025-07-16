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
subcirc0.u(0.982000,0.154000,0.211000, qreg_1[0])
subcirc0.rz(0.602000, qreg_1[0])
subcirc0.cx(qreg_1[0],qreg_1[2])
subcirc0.h(qreg_1[1])
subcirc0.rz(0.485000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.rz(0.553000, qreg_0[1])
subcirc1.u(0.813000,-0.804000,0.052000, qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.u(0.950000,-0.112000,0.709000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(-0.955000,0.502000,-0.649000, qreg_1[0])
subcirc2.u(-0.706000,-0.569000,-0.199000, qreg_1[0])
subcirc2.u(0.386000,0.400000,0.055000, qreg_1[2])
subcirc2.rz(-0.956000, qreg_1[0])
subcirc2.u(-0.374000,-0.898000,-0.635000, qreg_1[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(0.727000, qreg_0[0])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_0[0])
subcirc3.rz(0.185000, qreg_0[0])
subcirc3.u(0.732000,-0.183000,0.938000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(-0.196000, qreg_1[1])
subcirc4.u(-0.204000,-0.207000,0.980000, qreg_1[1])
subcirc4.u(0.558000,0.248000,-0.025000, qreg_3[0])
subcirc4.h(qreg_0[0])
subcirc4.cx(qreg_0[0],qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.h(0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0.447000,-0.901000,param_3, 0)
		main_circ.append(subcirc0,[2,qreg_1[0],0,qreg_0[0],1])
	with case_1(1):
		main_circ.append(subcirc4,[qreg_0[0],1,qreg_1[0],3])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[3,qreg_1[0],1,qreg_0[0],0,2])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[0],2)
		main_circ.h(3)
		main_circ.cx(qreg_1[0],2)
		main_circ.cx(1,3)
	with case_1(1):
		main_circ.u(param_4,param_3,param_4, qreg_1[0])
		main_circ.u(param_4,param_0,-0.579000, 1)
		main_circ.append(subcirc4,[3,1,qreg_0[0],0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[qreg_0[0],3,qreg_1[0],0,1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(3,qreg_0[0])
	main_circ.cx(qreg_1[0],2)
	main_circ.cx(2,0)
	main_circ.cx(qreg_1[0],1)
	main_circ.cx(qreg_0[0],0)
with else_1:
	main_circ.cx(qreg_1[0],1)
main_circ.cx(0,3)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_4, 2)
with else_1:
	main_circ.u(param_3,0.525000,0.393000, 2)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,-0.369000,0.518000, 0)
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.u(param_3,param_4,param_2, qreg_0[0])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rz(-0.847000, 1)
		main_circ.id(1)
	with case_1(1):
		main_circ.rz(-0.448000, 2)
		main_circ.id(3)
bindings = {param_0: -0.603000, param_2: -0.972000, param_3: 0.115000, param_4: 0.028000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "649", "InverseCancellation")
