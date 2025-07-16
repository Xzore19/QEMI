from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.u(0.230000,0.658000,-0.348000, qreg_0[1])
subcirc0.ry(0.917000, qreg_0[0])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.628000, qreg_0[1])
subcirc1.u(-0.318000,0.448000,0.923000, qreg_0[1])
subcirc1.h(qreg_2[1])
subcirc1.u(0.702000,0.276000,-0.108000, qreg_0[0])
subcirc1.u(-0.075000,-0.828000,-0.403000, qreg_0[1])
subcirc1.u(-0.338000,-0.816000,-0.982000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.262000,0.436000,-0.070000, qreg_0[3])
subcirc2.ry(-0.729000, qreg_0[2])
subcirc2.z(qreg_0[3])
subcirc2.z(qreg_0[3])
subcirc2.h(qreg_0[1])
subcirc2.z(qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.350000, qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[1])
subcirc3.z(qreg_0[1])
subcirc3.u(0.806000,-0.720000,-0.392000, qreg_3[0])
subcirc3.h(qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[1])
	main_circ.append(subcirc2,[3,1,qreg_0[1],0])
main_circ.append(subcirc3,[0,3,qreg_0[1],qreg_0[0],1,2])
main_circ.h(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.445000,-0.075000,param_7, 1)
	main_circ.u(0.007000,param_4,0.894000, 0)
	main_circ.u(0.852000,0.150000,0.344000, 1)
	main_circ.ry(-0.702000, qreg_0[1])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[0,2,3,1])
	with case_1(1):
		main_circ.h(0)
		main_circ.h(qreg_0[0])
		main_circ.ry(0.109000, 1)
		main_circ.append(subcirc2,[1,3,qreg_0[1],qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(qreg_0[0])
with else_1:
	main_circ.append(subcirc0,[3,qreg_0[0],0,1,2,qreg_0[1]])
main_circ.ry(0.180000, qreg_0[1])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(2)
	main_circ.u(0.626000,0.817000,0.845000, qreg_0[1])
	main_circ.u(param_5,0.940000,0.316000, 1)
	main_circ.h(3)
with else_1:
	main_circ.u(0.921000,-0.002000,param_5, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(2)
main_circ.ry(param_0, qreg_0[1])
bindings = {param_0: 0.426000, param_4: -0.700000, param_5: 0.044000, param_7: -0.217000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1257")
