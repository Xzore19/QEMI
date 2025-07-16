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
subcirc0.h(qreg_2[0])
subcirc0.cz(qreg_2[1],qreg_2[0])
subcirc0.u(-0.286000,-0.423000,0.966000, qreg_0[1])
subcirc0.u(-0.394000,0.140000,-0.748000, qreg_2[1])
subcirc0.u(-0.988000,0.075000,-0.689000, qreg_0[0])

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

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0.308000,param_0,param_0, 0)
	main_circ.ry(param_0, qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.141000,param_0,param_0, 2)
	main_circ.append(subcirc0,[qreg_0[0],2,3,0])
with else_1:
	main_circ.h(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.943000,-0.615000,param_0, qreg_0[0])
	main_circ.append(subcirc0,[1,3,0,qreg_1[0]])
main_circ.append(subcirc0,[1,qreg_0[0],3,0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.986000,-0.468000,0.771000, qreg_0[0])
	main_circ.h(0)
with else_1:
	main_circ.append(subcirc0,[1,qreg_1[0],qreg_0[0],2])
main_circ.ry(param_0, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(0.607000, 1)
	main_circ.append(subcirc0,[2,0,qreg_1[0],1])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.h(qreg_1[0])
	main_circ.append(subcirc0,[qreg_0[0],0,qreg_1[0],3])
with else_1:
	main_circ.cz(1,2)
	main_circ.cz(qreg_1[0],qreg_0[0])
	main_circ.cz(1,qreg_0[0])
	main_circ.cz(0,1)
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(3,0)
		main_circ.cz(qreg_1[0],2)
		main_circ.cz(0,qreg_1[0])
		main_circ.cz(qreg_0[0],2)
	with case_1(1):
		main_circ.cz(0,2)
		main_circ.cz(qreg_0[0],0)
		main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,param_0,param_0, 3)
with else_1:
	main_circ.id(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[0])
	main_circ.id(2)
bindings = {param_0: 0.151000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "672")
