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
subcirc0.u(-0.746000,-0.946000,-0.562000, qreg_0[0])
subcirc0.u(0.212000,0.415000,0.210000, qreg_2[1])
subcirc0.cz(qreg_0[1],qreg_2[0])
subcirc0.cz(qreg_0[1],qreg_2[1])
subcirc0.u(-0.099000,0.350000,-0.605000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.178000, qreg_0[2])
subcirc1.u(0.507000,-0.052000,0.349000, qreg_0[0])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.u(-0.664000,-0.798000,-0.785000, qreg_0[0])
subcirc1.z(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_2[0])
subcirc2.cz(qreg_2[0],qreg_3[0])
subcirc2.z(qreg_2[0])
subcirc2.z(qreg_0[1])
subcirc2.u(0,0,-0.728000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0.716000,-0.024000,-0.577000, qreg_0[2])
subcirc3.u(-0.776000,0.348000,-0.261000, qreg_0[2])
subcirc3.u(-0.180000,0.052000,0.784000, qreg_0[3])
subcirc3.u(-0.897000,-0.058000,0.435000, qreg_0[0])
subcirc3.u(-0.102000,-0.489000,0.027000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_3[0],qreg_2[0])
subcirc4.u(-0.652000,-0.014000,-0.481000, qreg_2[0])
subcirc4.u(0.823000,0.799000,0.799000, qreg_2[0])
subcirc4.z(qreg_0[1])
subcirc4.z(qreg_3[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(param_3,-0.883000,0.321000, 2)
					main_circ.append(subcirc0,[qreg_0[0],0,1,2])
				with case_1(1):
					main_circ.append(subcirc2,[qreg_0[0],2,1,0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(qreg_0[0],0)
				with else_1:
					main_circ.u(0.946000,-0.260000,0.692000, 1)
					main_circ.u(param_0,0,-0.833000, 2)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cz(3,0)
						main_circ.append(subcirc3,[0,2,1,3,qreg_0[0]])
					with case_1(1):
						main_circ.append(subcirc3,[3,0,2,qreg_0[0],1])
		with else_3:
			main_circ.z(0)
			main_circ.append(subcirc1,[1,qreg_0[0],2,3])
	with case_4(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.append(subcirc2,[1,qreg_0[0],3,2])
		with else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(1,2)
					main_circ.cz(3,1)
					main_circ.cz(qreg_0[0],2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(3,1)
					main_circ.cz(0,1)
					main_circ.cz(3,qreg_0[0])
					main_circ.cz(3,qreg_0[0])
				with else_1:
					main_circ.cz(0,qreg_0[0])
					main_circ.cz(0,1)
			with else_2:
				main_circ.z(3)
				main_circ.u(param_4,param_3,0.808000, 1)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[2,3,1,qreg_0[0]])
					with case_1(1):
						main_circ.u(param_1,param_4,param_2, 0)
						main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.659000, param_1: 0.269000, param_2: -0.588000, param_3: 0.128000, param_4: -0.926000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1997", "Collect2qBlocks")
