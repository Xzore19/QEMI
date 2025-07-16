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
subcirc0.rx(0.943000, qreg_0[0])
subcirc0.rx(0.407000, qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.u(0.638000,0.239000,0.978000, qreg_0[0])
subcirc0.u(-0.679000,0.967000,0.243000, qreg_2[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rx(0.405000, 3)
	main_circ.z(3)
with else_1:
	main_circ.z(3)
	main_circ.z(qreg_0[0])
	main_circ.append(subcirc0,[qreg_0[1],3,1,2])
main_circ.u(param_2,param_3,param_5, 0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[3,1,qreg_0[1],0])
	with case_1(1):
		main_circ.u(param_5,-0.866000,-0.158000, 2)
		main_circ.rx(-0.336000, 1)
		main_circ.rx(-0.909000, qreg_0[1])
		main_circ.append(subcirc0,[3,qreg_0[0],2,0])
main_circ.cy(qreg_0[0],2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(param_3, 1)
with else_1:
	main_circ.u(param_5,param_3,-0.844000, qreg_0[0])
	main_circ.append(subcirc0,[3,qreg_0[0],0,qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(0,3)
with else_1:
	main_circ.append(subcirc0,[0,qreg_0[1],2,3])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(0,qreg_0[1])
	main_circ.cy(1,qreg_0[1])
	main_circ.cy(qreg_0[1],1)
	main_circ.cy(qreg_0[0],qreg_0[1])
	main_circ.cy(qreg_0[0],3)
with else_1:
	main_circ.cy(qreg_0[0],3)
	main_circ.cy(2,3)
	main_circ.cy(1,qreg_0[1])
	main_circ.cy(0,qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,param_3,param_4, 3)
	main_circ.rx(param_3, 2)
	main_circ.cy(3,0)
	main_circ.z(2)
with else_1:
	main_circ.rx(param_0, 3)
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.393000, param_2: 0.684000, param_3: 0.648000, param_4: -0.699000, param_5: 0.281000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1820")
