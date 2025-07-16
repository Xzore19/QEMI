from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.rx(-0.039000, qreg_0[3])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.rz(-0.024000, qreg_0[3])
subcirc0.u(0.676000,0.173000,0.963000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.392000, qreg_0[3])
subcirc1.rx(-0.350000, qreg_0[0])
subcirc1.rz(-0.989000, qreg_0[2])
subcirc1.rx(0.940000, qreg_0[3])
subcirc1.u(0.524000,-0.603000,-0.751000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[2,1,qreg_0[0],0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_1, 3)
		main_circ.rz(param_1, 3)
		main_circ.append(subcirc1,[0,2,3,qreg_0[0]])
	with case_1(1):
		main_circ.u(param_0,0.886000,0.500000, qreg_0[0])
		main_circ.rx(-0.357000, 3)
		main_circ.append(subcirc1,[3,1,0,2])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[0],1,2,0])
with else_1:
	main_circ.rx(param_1, 3)
	main_circ.y(0)
	main_circ.rx(param_0, 0)
	main_circ.id(1)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_1,param_1,param_0, qreg_0[0])
	main_circ.barrier(2)
with else_1:
	main_circ.u(param_1,param_1,param_1, 2)
	main_circ.rx(param_1, 0)
	main_circ.append(subcirc1,[0,qreg_0[0],1,3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.id(3)
main_circ.y(qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.u(param_1,-0.803000,param_1, 1)
	main_circ.rz(0.354000, 2)
	main_circ.rz(0.467000, 2)
bindings = {param_0: 0.384000, param_1: 0.202000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "131", "OptimizeCliffords")
