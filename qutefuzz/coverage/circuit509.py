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
subcirc0.u(pi/2,0.751000,-0.470000, qreg_0[2])
subcirc0.u(pi/2,-0.485000,-0.430000, qreg_0[1])
subcirc0.u(pi/2,0.349000,0.268000, qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.u(pi/2,-0.393000,0.245000, qreg_0[1])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_2[0])
subcirc1.u(pi/2,-0.671000,-0.465000, qreg_0[0])
subcirc1.cz(qreg_2[0],qreg_0[0])
subcirc1.y(qreg_2[0])
subcirc1.u(pi/2,-0.702000,-0.613000, qreg_2[0])
subcirc1.z(qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,-0.051000,0.371000, qreg_2[1])
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_2[1])
subcirc2.cz(qreg_2[1],qreg_1[0])
subcirc2.u(pi/2,-0.948000,-0.558000, qreg_1[0])
subcirc2.u(pi/2,-0.301000,0.481000, qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[0])
subcirc3.z(qreg_0[3])
subcirc3.u(pi/2,0.758000,-0.117000, qreg_0[0])
subcirc3.y(qreg_0[3])
subcirc3.y(qreg_0[2])
subcirc3.u(pi/2,0.967000,-0.323000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(pi/2,-0.518000,-0.342000, qreg_0[1])
subcirc4.cz(qreg_0[1],qreg_0[2])
subcirc4.y(qreg_0[3])
subcirc4.z(qreg_0[2])
subcirc4.cz(qreg_0[0],qreg_0[1])
subcirc4.z(qreg_0[0])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.z(qreg_0[0])
			main_circ.z(0)
			main_circ.id(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.z(0)
			main_circ.u(param_3,param_4,param_0, qreg_1[0])
			main_circ.id(0)
		with else_1:
			main_circ.y(2)
			main_circ.append(subcirc0,[2,0,qreg_1[0],3,1,qreg_0[0]])
	with case_2(1):
		main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],1,0,2,3])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],3,1])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.cz(0,qreg_1[0])
		main_circ.append(subcirc2,[qreg_0[0],2,qreg_1[0],0,1,3])
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cz(0,qreg_0[0])
			main_circ.cz(0,3)
			main_circ.cz(qreg_1[0],qreg_0[0])
			main_circ.cz(1,qreg_1[0])
			main_circ.cz(0,1)
		with else_1:
			main_circ.cz(3,1)
			main_circ.cz(1,0)
			main_circ.cz(2,0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(0)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.y(0)
		main_circ.id(qreg_1[0])
	with else_1:
		main_circ.cz(1,2)
		main_circ.id(3)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.barrier(3)
bindings = {param_0: -0.379000, param_3: -0.831000, param_4: 0.807000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "509")
