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
subcirc0.u(pi/2,-0.505000,-0.939000, qreg_0[0])
subcirc0.rz(-0.292000, qreg_0[1])
subcirc0.ry(-0.253000, qreg_0[3])
subcirc0.u(-0.400000,-0.124000,-0.937000, qreg_0[1])
subcirc0.u(0.116000,-0.126000,-0.083000, qreg_0[1])
subcirc0.rz(0.889000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.351000,0.796000,0.835000, qreg_0[1])
subcirc1.u(pi/2,0.736000,-0.071000, qreg_0[1])
subcirc1.ry(0.573000, qreg_0[1])
subcirc1.rz(-0.011000, qreg_0[0])
subcirc1.rz(-0.777000, qreg_0[1])
subcirc1.u(0.050000,0.724000,0.018000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

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

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,0.172000,-0.351000, 2)
		main_circ.u(param_1,0.033000,param_1, qreg_1[0])
		main_circ.u(pi/2,0.635000,param_0, 0)
		main_circ.append(subcirc0,[1,2,3,qreg_1[0]])
	with case_1(1):
		main_circ.append(subcirc1,[0,qreg_0[0],3,qreg_1[0],1])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(0.258000, qreg_1[0])
	main_circ.u(param_1,param_1,param_0, 2)
with else_1:
	main_circ.u(param_1,param_0,-0.697000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],2,1,qreg_1[0],3])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],2,3,1,0])
	with case_1(1):
		main_circ.rz(param_0, 3)
		main_circ.ry(-0.754000, qreg_1[0])
		main_circ.u(pi/2,param_0,-0.104000, 0)
		main_circ.append(subcirc1,[qreg_1[0],0,3,1,2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.605000,param_0,-0.487000, 2)
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,param_0,-0.264000, 2)
with else_1:
	main_circ.u(param_0,param_0,-0.329000, 3)
bindings = {param_0: 0.822000, param_1: -0.565000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1079", "ResetAfterMeasureSimplification")
