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
subcirc0.x(qreg_2[0])
subcirc0.u(0,0,-0.172000, qreg_2[0])
subcirc0.u(0,0,-0.315000, qreg_2[1])
subcirc0.rz(-0.647000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.u(0,0,0.058000, qreg_2[0])
subcirc1.rx(-0.898000, qreg_3[0])
subcirc1.u(0,0,0.754000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.365000, qreg_0[1])
subcirc2.x(qreg_2[0])
subcirc2.rz(0.640000, qreg_2[0])
subcirc2.rz(0.766000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rx(0.365000, qreg_0[3])
subcirc3.x(qreg_0[3])
subcirc3.x(qreg_0[3])
subcirc3.u(0,0,-0.387000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.rx(-0.811000, qreg_0[0])
subcirc4.rx(-0.578000, qreg_1[2])
subcirc4.u(0,0,0.611000, qreg_1[1])
subcirc4.x(qreg_1[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc2,[0,qreg_2[0],qreg_0[0],qreg_0[1]])
with else_1:
	main_circ.id(qreg_2[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_2, qreg_0[1])
	main_circ.u(0,0,param_1, qreg_3[0])
	main_circ.rx(-0.189000, qreg_0[0])
	main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(-0.804000, qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_3[0])
with else_1:
	main_circ.rz(-0.150000, 0)
	main_circ.u(0,0,param_2, qreg_2[0])
	main_circ.rx(param_1, qreg_2[0])
	main_circ.x(qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(qreg_0[1])
	main_circ.rz(-0.859000, 0)
	main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_2[0]])
with else_1:
	main_circ.rx(param_2, qreg_3[0])
	main_circ.rx(0.307000, qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,qreg_3[0]])
with else_1:
	main_circ.id(qreg_3[0])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc2,[0,qreg_3[0],qreg_2[0],qreg_0[0]])
with else_1:
	main_circ.x(qreg_2[0])
	main_circ.barrier(qreg_0[0])
bindings = {param_1: 0.058000, param_2: -0.796000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1871", "CXCancellation")
