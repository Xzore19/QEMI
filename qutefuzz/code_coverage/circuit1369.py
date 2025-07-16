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
subcirc0.u(-0.727000,-0.104000,-0.854000, qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.097000,-0.818000,0.781000, qreg_0[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.cz(qreg_2[0],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cx(qreg_0[3],qreg_0[2])
subcirc2.cx(qreg_0[0],qreg_0[3])
subcirc2.z(qreg_0[3])
subcirc2.cx(qreg_0[3],qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3.z(qreg_0[2])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.z(qreg_0[3])
subcirc4.u(-0.017000,0.357000,0.049000, qreg_0[0])
subcirc4.cz(qreg_0[1],qreg_0[2])
subcirc4.u(0.264000,0.166000,-0.917000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,-0.951000,param_0, 3)
	main_circ.append(subcirc4,[1,0,qreg_0[1],qreg_0[0],2,3])
with else_1:
	main_circ.append(subcirc4,[3,2,0,1,qreg_0[0],qreg_0[1]])
main_circ.z(2)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(qreg_0[0])
	main_circ.u(param_1,param_1,0.395000, 0)
	main_circ.z(qreg_0[0])
with else_1:
	main_circ.u(param_0,param_1,param_1, 2)
	main_circ.append(subcirc4,[qreg_0[0],0,3,qreg_0[1],2,1])
main_circ.append(subcirc3,[2,0,1,qreg_0[0]])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(2,0)
	main_circ.append(subcirc0,[qreg_0[0],1,0,2,qreg_0[1],3])
with else_1:
	main_circ.append(subcirc4,[0,1,3,qreg_0[0],qreg_0[1],2])
main_circ.append(subcirc3,[qreg_0[1],0,1,qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(3,1)
	main_circ.cz(qreg_0[0],0)
	main_circ.cx(1,3)
	main_circ.cx(qreg_0[0],qreg_0[1])
	main_circ.append(subcirc3,[qreg_0[1],2,3,0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,-0.017000,param_0, 2)
	main_circ.cx(qreg_0[0],1)
	main_circ.id(0)
with else_1:
	main_circ.id(3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(1)
bindings = {param_0: -0.728000, param_1: -0.613000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1369")
