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
subcirc0.ry(0.707000, qreg_0[3])
subcirc0.ry(-0.382000, qreg_0[3])
subcirc0.rx(0.063000, qreg_0[0])
subcirc0.s(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(-0.501000,-0.243000,-0.842000, qreg_0[1])
subcirc1.u(0.895000,0.165000,-0.968000, qreg_0[0])
subcirc1.ry(-0.851000, qreg_2[0])
subcirc1.ry(0.351000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.s(qreg_0[1])
subcirc2.u(-0.765000,-0.508000,-0.969000, qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rx(0.542000, qreg_0[3])
subcirc3.u(-0.829000,-0.420000,0.503000, qreg_0[2])
subcirc3.s(qreg_0[3])
subcirc3.u(-0.022000,0.104000,0.048000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.s(qreg_0[1])
subcirc4.ry(0.259000, qreg_0[2])
subcirc4.ry(-0.055000, qreg_0[0])
subcirc4.s(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(0)
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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(-0.037000, qreg_0[2])
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.rx(param_3, qreg_0[0])
		main_circ.u(0.964000,-0.314000,0.922000, qreg_0[0])
		main_circ.ry(param_2, qreg_0[1])
		main_circ.ry(-0.289000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
	main_circ.rx(param_4, qreg_0[2])
main_circ.u(-0.283000,0.564000,-0.671000, qreg_0[0])
main_circ.rx(-0.295000, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[1])
		main_circ.rx(-0.603000, qreg_0[2])
		main_circ.u(param_5,param_3,param_5, qreg_3[0])
		main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
	with case_1(1):
		main_circ.u(param_3,0.531000,param_2, qreg_3[0])
		main_circ.u(-0.829000,0.174000,param_0, qreg_0[1])
		main_circ.ry(param_4, qreg_3[0])
		main_circ.u(param_2,-0.997000,param_6, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[2])
main_circ.u(param_3,param_3,param_3, qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
	with case_1(1):
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.852000, param_2: 0.115000, param_3: -0.636000, param_4: -0.576000, param_5: 0.205000, param_6: -0.975000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "609")
