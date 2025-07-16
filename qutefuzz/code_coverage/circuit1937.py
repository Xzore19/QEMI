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
subcirc0.rz(0.612000, qreg_0[2])
subcirc0.rx(-0.999000, qreg_0[0])
subcirc0.u(0,0,0.877000, qreg_0[0])
subcirc0.rz(-0.576000, qreg_0[1])
subcirc0.rz(0.477000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rx(0.490000, 2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0,0,0.137000, 0)
	main_circ.cz(3,0)
	main_circ.u(param_0,0,-0.196000, 3)
with else_1:
	main_circ.rz(-0.856000, 2)
	main_circ.rx(param_0, 2)
	main_circ.rx(-0.105000, 2)
main_circ.append(subcirc0,[3,0,1,qreg_0[0]])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(0.870000, 1)
		main_circ.append(subcirc0,[0,1,2,qreg_0[0]])
	with case_1(1):
		main_circ.rz(0.582000, 3)
		main_circ.cz(1,2)
		main_circ.append(subcirc0,[2,0,qreg_0[0],3])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rz(param_0, 0)
	main_circ.u(param_0,0,-0.902000, 1)
with else_1:
	main_circ.rx(0.846000, 0)
main_circ.cz(0,1)
main_circ.rx(param_0, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(2,0)
	main_circ.cz(2,1)
	main_circ.cz(1,qreg_0[0])
with else_1:
	main_circ.cz(qreg_0[0],3)
	main_circ.cz(3,qreg_0[0])
	main_circ.cz(qreg_0[0],3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(0,1)
	main_circ.cz(0,qreg_0[0])
	main_circ.cz(3,1)
	main_circ.cz(3,qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(0,1)
		main_circ.cz(3,qreg_0[0])
		main_circ.barrier(2)
	with case_1(1):
		main_circ.id(3)
bindings = {param_0: 0.684000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1937")
