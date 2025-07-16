from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(-0.855000,-0.820000,-0.451000, qreg_0[0])
subcirc0.ry(-0.172000, qreg_3[0])
subcirc0.y(qreg_1[0])
subcirc0.u(0.572000,-0.287000,0.906000, qreg_0[0])
subcirc0.u(-0.494000,0.906000,0.388000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.297000,-0.765000,0.125000, qreg_3[0])
subcirc1.ry(-0.521000, qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.u(0.228000,0.486000,-0.951000, qreg_0[1])
subcirc1.ry(-0.066000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,-0.891000,0.693000, qreg_0[1])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[3])
main_circ.x(1)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(qreg_0[1])
		main_circ.u(param_0,param_0,param_0, qreg_0[1])
		main_circ.x(qreg_0[3])
		main_circ.u(param_0,param_0,param_0, qreg_0[1])
	with case_1(1):
		main_circ.u(0.275000,-0.178000,param_0, qreg_0[1])
		main_circ.barrier(1)
main_circ.ry(-0.866000, qreg_0[1])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.546000,param_0,param_0, qreg_0[2])
with else_1:
	main_circ.u(-0.838000,param_0,param_0, qreg_0[0])
	main_circ.y(qreg_0[1])
	main_circ.ry(param_0, qreg_0[2])
	main_circ.u(param_0,-0.775000,param_0, 0)
	main_circ.ry(0.624000, 1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(0)
with else_1:
	main_circ.barrier(1)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.584000,0.398000,-0.107000, qreg_0[0])
	main_circ.u(param_0,param_0,-0.570000, qreg_0[0])
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.x(qreg_0[0])
	main_circ.barrier(qreg_0[3])
main_circ.x(qreg_0[3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0.464000,0.218000,-0.866000, qreg_0[1])
	main_circ.u(param_0,param_0,-0.062000, qreg_0[3])
	main_circ.id(qreg_0[3])
main_circ.ry(-0.386000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(0)
		main_circ.ry(param_0, qreg_0[0])
		main_circ.id(qreg_0[3])
	with case_1(1):
		main_circ.ry(param_0, 0)
		main_circ.id(qreg_0[1])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(qreg_0[3])
		main_circ.y(qreg_0[3])
		main_circ.x(qreg_0[3])
		main_circ.ry(0.436000, 0)
	with case_1(1):
		main_circ.x(0)
		main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.u(param_0,0.567000,param_0, qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.y(qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_0, qreg_0[3])
	main_circ.y(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.856000,-0.552000,param_0, qreg_0[1])
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.ry(param_0, qreg_0[2])
	main_circ.ry(0.739000, qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.x(qreg_0[1])
		main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(0.939000, qreg_0[0])
	main_circ.u(param_0,param_0,0.079000, qreg_0[3])
	main_circ.id(qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_0[2])
with else_1:
	main_circ.x(qreg_0[2])
	main_circ.x(1)
	main_circ.id(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(-0.372000,-0.746000,-0.553000, 1)
	main_circ.ry(0.180000, 1)
	main_circ.ry(0.768000, qreg_0[2])
with else_1:
	main_circ.ry(-0.318000, qreg_0[0])
	main_circ.barrier(qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(qreg_0[0])
		main_circ.barrier(qreg_0[3])
	with case_1(1):
		main_circ.barrier(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(qreg_0[1])
with else_1:
	main_circ.x(0)
	main_circ.x(0)
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.124000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "438")
