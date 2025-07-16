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
subcirc0.u(0.112000,-0.661000,0.890000, qreg_0[0])
subcirc0.u(0,0,0.550000, qreg_0[2])
subcirc0.u(-0.321000,-0.747000,0.131000, qreg_0[2])
subcirc0.u(-0.227000,-0.541000,-0.600000, qreg_0[0])
subcirc0.u(0,0,0.775000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.u(0,0,-0.644000, qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.u(0,0,-0.342000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.298000, qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.u(0.511000,0.917000,-0.373000, qreg_1[0])
subcirc2.u(0,0,-0.435000, qreg_1[0])
subcirc2.u(-0.716000,-0.937000,0.429000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.965000, qreg_3[0])
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.cz(qreg_0[2],qreg_0[1])
subcirc3.u(-0.727000,0.961000,0.825000, qreg_0[1])
subcirc3.u(0.889000,0.352000,0.572000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(1,0)
		main_circ.u(0,param_3,0.972000, 3)
		main_circ.append(subcirc3,[3,1,2,0])
	with case_1(1):
		main_circ.cz(0,2)
		main_circ.append(subcirc3,[2,0,1,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(0,2)
	main_circ.barrier(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_3,param_3,-0.445000, 3)
		main_circ.cz(3,0)
		main_circ.u(0,0,0.541000, 3)
		main_circ.cz(2,0)
	with case_1(1):
		main_circ.u(param_1,0,-0.504000, 2)
		main_circ.barrier(1)
main_circ.cz(2,1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0,0,param_2, 0)
	main_circ.barrier(2)
with else_1:
	main_circ.append(subcirc3,[0,3,2,1])
main_circ.cx(2,0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,param_1,param_0, 0)
	main_circ.cz(1,2)
	main_circ.u(0,0,0.859000, 2)
	main_circ.barrier(3)
with else_1:
	main_circ.barrier(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_0,param_2,0.651000, 2)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(2,3)
		main_circ.id(0)
	with case_1(1):
		main_circ.u(0.122000,param_0,-0.971000, 2)
		main_circ.u(param_2,0.642000,-0.431000, 3)
		main_circ.u(param_3,0,-0.855000, 0)
		main_circ.cx(2,0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,0,param_1, 1)
	main_circ.append(subcirc3,[3,0,1,2])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[2,0,1,3])
	with case_1(1):
		main_circ.id(2)
bindings = {param_0: 0.299000, param_1: 0.796000, param_2: -0.218000, param_3: -0.040000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1381", "OptimizeAnnotated")
