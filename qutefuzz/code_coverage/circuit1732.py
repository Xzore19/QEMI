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
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.z(qreg_0[3])
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.z(qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.h(qreg_0[2])
subcirc1.h(qreg_0[3])
subcirc1.s(qreg_0[3])
subcirc1.u(-0.483000,0.133000,0.190000, qreg_0[3])
subcirc1.h(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.751000,-0.918000,0.849000, qreg_0[3])
subcirc2.u(0.440000,-0.345000,-0.796000, qreg_0[0])
subcirc2.h(qreg_0[3])
subcirc2.z(qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2.h(qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[2])
subcirc3.h(qreg_0[2])
subcirc3.z(qreg_0[1])
subcirc3.s(qreg_3[0])
subcirc3.u(0.186000,-0.397000,0.993000, qreg_0[1])
subcirc3.s(qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.h(qreg_0[2])
subcirc4.u(0.616000,-0.153000,-0.446000, qreg_0[0])
subcirc4.u(-0.085000,-0.002000,0.301000, qreg_0[1])
subcirc4.s(qreg_0[0])
subcirc4.z(qreg_0[0])
subcirc4.s(qreg_0[3])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(0)
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(0)
			main_circ.append(subcirc1,[1,qreg_0[1],qreg_0[0],0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.append(subcirc2,[2,3,1,qreg_0[1]])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.u(param_1,param_1,param_1, 1)
			main_circ.barrier(3)
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[2,0,qreg_0[1],3])
			with else_1:
				main_circ.append(subcirc4,[qreg_0[1],2,0,1,3,qreg_0[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,0.902000,0.560000, 3)
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.append(subcirc1,[qreg_0[0],1,3,0])
with else_3:
	main_circ.append(subcirc0,[3,2,qreg_0[0],1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc0,[3,qreg_0[0],qreg_0[1],1])
	with else_2:
		main_circ.id(0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.barrier(2)
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.barrier(1)
		with else_2:
			main_circ.h(0)
			main_circ.s(3)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.h(3)
					main_circ.z(qreg_0[1])
					main_circ.barrier(2)
				with case_1(1):
					main_circ.id(3)
bindings = {param_1: 0.336000, param_2: -0.583000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1732")
