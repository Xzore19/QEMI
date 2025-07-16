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
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.rx(0.716000, qreg_0[2])
subcirc0.cz(qreg_0[3],qreg_0[0])
subcirc0.u(0,0,-0.942000, qreg_0[0])
subcirc0.u(0,0,0.105000, qreg_0[2])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")
param_8 = Parameter("param_8")

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(1,2)
	main_circ.append(subcirc0,[2,3,qreg_0[1],0,1])
with else_1:
	main_circ.rx(param_1, 3)
	main_circ.cz(3,qreg_0[1])
	main_circ.u(0,param_1,-0.998000, qreg_0[1])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0,param_1,param_0, 1)
	main_circ.cz(2,3)
	main_circ.u(param_1,0,-0.538000, 0)
with else_1:
	main_circ.cz(qreg_0[0],3)
	main_circ.rx(0.956000, 1)
	main_circ.append(subcirc0,[2,1,qreg_0[1],3,0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_4,param_2,0.957000, 1)
	main_circ.u(0,0,param_3, 3)
	main_circ.rx(0.481000, 3)
	main_circ.cz(qreg_0[0],3)
	main_circ.cz(2,0)
with else_1:
	main_circ.u(param_4,0,-0.478000, 3)
	main_circ.rx(param_0, qreg_0[1])
	main_circ.u(param_0,param_5,-0.807000, 3)
	main_circ.append(subcirc0,[0,2,qreg_0[0],1,3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.665000, qreg_0[0])
	main_circ.append(subcirc0,[2,1,0,qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_7,param_6,-0.805000, 0)
	main_circ.rx(param_4, 1)
	main_circ.rx(param_4, 2)
	main_circ.u(param_6,-0.230000,param_4, 3)
	main_circ.u(0,param_1,param_6, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rx(-0.624000, 0)
	main_circ.append(subcirc0,[0,2,qreg_0[1],qreg_0[0],1])
with else_1:
	main_circ.cz(0,qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0,0,param_7, 1)
	main_circ.id(3)
bindings = {param_0: 0.064000, param_1: -0.250000, param_2: 0.844000, param_3: -0.407000, param_4: 0.974000, param_5: 0.110000, param_6: -0.562000, param_7: -0.434000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1784", "InverseCancellation")
