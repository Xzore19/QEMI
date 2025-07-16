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
subcirc0.ry(-0.614000, qreg_1[0])
subcirc0.x(qreg_1[2])
subcirc0.x(qreg_1[2])
subcirc0.ry(0.424000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_1[1],qreg_1[2])
subcirc1.ry(-0.095000, qreg_1[0])
subcirc1.cz(qreg_1[1],qreg_1[2])
subcirc1.x(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_0[0],3,0,2,1])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.cz(3,0)
		main_circ.append(subcirc0,[3,0,2,qreg_0[0],1])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[0],3,0,1,2])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.cy(2,3)
		main_circ.ry(-0.975000, 1)
		main_circ.barrier(3)
	with case_1(1):
		main_circ.append(subcirc0,[0,2,1,3,qreg_0[0]])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[0,qreg_0[0],1,3,2])
	with case_1(1):
		main_circ.cy(3,qreg_0[0])
		main_circ.cz(qreg_0[0],2)
		main_circ.append(subcirc0,[0,2,1,qreg_0[0],3])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.x(1)
	main_circ.ry(param_0, 3)
	main_circ.ry(0.099000, qreg_0[0])
	main_circ.append(subcirc0,[2,qreg_0[0],0,3,1])
with else_1:
	main_circ.cy(0,1)
	main_circ.cy(0,2)
	main_circ.cy(0,3)
	main_circ.cz(qreg_0[0],0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(0,3)
		main_circ.cz(3,0)
		main_circ.cy(0,1)
		main_circ.cz(qreg_0[0],2)
	with case_1(1):
		main_circ.cy(qreg_0[0],3)
		main_circ.cy(3,0)
		main_circ.cz(3,0)
		main_circ.barrier(0)
bindings = {param_0: 0.522000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1758")
