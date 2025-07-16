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
subcirc0.s(qreg_2[1])
subcirc0.s(qreg_0[1])
subcirc0.rz(-0.760000, qreg_0[0])
subcirc0.rz(-0.907000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.461000, qreg_0[3])
subcirc1.rz(0.791000, qreg_0[3])
subcirc1.rz(-0.511000, qreg_0[2])
subcirc1.u(-0.599000,0.121000,0.542000, qreg_0[1])
subcirc1.rz(0.288000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.488000,0.270000,-0.830000, qreg_0[2])
subcirc2.s(qreg_0[1])
subcirc2.rz(-0.098000, qreg_0[2])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[1])
subcirc3.rz(0.578000, qreg_0[1])
subcirc3.rz(-0.202000, qreg_0[0])
subcirc3.ry(-0.810000, qreg_3[0])
subcirc3.u(0.876000,0.647000,-0.402000, qreg_0[2])

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
param_1 = Parameter("param_1")

main_circ.s(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(3)
	main_circ.append(subcirc1,[3,2,0,qreg_1[0]])
main_circ.s(qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[1,2,0,qreg_1[0]])
	with case_1(1):
		main_circ.append(subcirc0,[0,2,qreg_1[0],qreg_0[0],1,3])
main_circ.ry(0.703000, 1)
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],2,3])
main_circ.u(param_0,param_1,param_0, 2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,0.107000,param_0, 3)
		main_circ.s(qreg_0[0])
		main_circ.append(subcirc1,[3,1,qreg_0[0],2])
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.324000, qreg_1[0])
		main_circ.s(1)
		main_circ.id(0)
	with case_1(1):
		main_circ.ry(param_1, 3)
		main_circ.s(2)
		main_circ.append(subcirc3,[3,2,qreg_1[0],0])
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.s(2)
		main_circ.id(2)
	with case_1(1):
		main_circ.u(-0.078000,-0.458000,0.318000, 2)
		main_circ.barrier(3)
bindings = {param_0: -0.448000, param_1: 0.974000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1588", "CollectLinearFunctions")
