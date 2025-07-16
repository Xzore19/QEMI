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
subcirc0.rz(-0.053000, qreg_0[0])
subcirc0.s(qreg_0[2])
subcirc0.rz(-0.356000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_3[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(-0.093000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[1])
subcirc1.rz(0.067000, qreg_0[0])
subcirc1.z(qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1.s(qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cx(qreg_0[1],qreg_0[2])
subcirc2.rz(-0.755000, qreg_0[2])
subcirc2.cx(qreg_0[3],qreg_0[0])
subcirc2.rz(0.517000, qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.cx(qreg_0[3],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cx(qreg_0[0],qreg_0[3])
subcirc3.cx(qreg_0[1],qreg_0[3])
subcirc3.rz(-0.616000, qreg_0[3])
subcirc3.cx(qreg_0[0],qreg_0[3])
subcirc3.rz(-0.909000, qreg_0[2])
subcirc3.cx(qreg_0[3],qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.s(qreg_0[1])
subcirc4.cx(qreg_0[0],qreg_0[1])
subcirc4.rz(-0.812000, qreg_3[0])
subcirc4.rz(-0.242000, qreg_0[1])
subcirc4.rz(0.728000, qreg_0[0])
subcirc4.z(qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[0],0])
main_circ.s(0)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[qreg_0[0],qreg_3[0],0,qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc4,[qreg_0[2],qreg_0[0],0,qreg_0[1]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_3[0])
	main_circ.append(subcirc3,[0,qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],0)
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.cx(qreg_0[2],qreg_3[0])
		main_circ.append(subcirc1,[qreg_3[0],0,qreg_0[2],qreg_0[0]])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.rz(-0.590000, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_3[0])
		main_circ.append(subcirc3,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
	with case_1(1):
		main_circ.z(qreg_0[1])
		main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.rz(param_2, qreg_0[1])
bindings = {param_2: 0.264000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "716")
