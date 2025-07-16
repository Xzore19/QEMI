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
subcirc0.u(-0.594000,0.463000,-0.746000, qreg_3[0])
subcirc0.rx(-0.352000, qreg_3[0])
subcirc0.u(pi/2,-0.458000,0.288000, qreg_3[0])
subcirc0.rz(-0.541000, qreg_0[1])
subcirc0.u(0.056000,-0.959000,-0.058000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0.343000,-0.351000,0.692000, qreg_0[0])
subcirc1.u(0.742000,-0.578000,0.554000, qreg_1[2])
subcirc1.u(pi/2,0.839000,-0.547000, qreg_1[1])
subcirc1.u(-0.482000,-0.029000,0.168000, qreg_1[1])
subcirc1.u(-0.674000,-0.047000,0.029000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.497000,0.579000, qreg_0[0])
subcirc2.u(pi/2,0.553000,-0.479000, qreg_0[0])
subcirc2.u(pi/2,-0.187000,-0.313000, qreg_3[0])
subcirc2.u(-0.826000,0.246000,0.086000, qreg_0[2])
subcirc2.u(pi/2,-0.382000,0.160000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,-0.167000,-0.224000, qreg_1[0])
subcirc3.u(0.460000,-0.052000,-0.261000, qreg_2[0])
subcirc3.u(pi/2,0.534000,0.483000, qreg_1[0])
subcirc3.u(pi/2,0.811000,-0.165000, qreg_3[0])
subcirc3.rx(-0.195000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.rz(-0.289000, qreg_1[0])
subcirc4.u(-0.110000,0.436000,-0.645000, qreg_1[2])
subcirc4.rx(-0.573000, qreg_0[0])
subcirc4.rz(-0.326000, qreg_0[0])
subcirc4.u(-0.096000,0.034000,0.849000, qreg_1[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.u(pi/2,param_1,0.016000, qreg_3[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],0,1])
	with case_3(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc3,[qreg_0[1],1,qreg_0[2],qreg_0[0]])
				with else_1:
					main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[2],0])
			with case_2(1):
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc3,[0,qreg_0[0],1,qreg_0[1]])
					with case_1(1):
						main_circ.rz(param_0, 0)
						main_circ.rz(0.245000, qreg_0[0])
						main_circ.rx(-0.921000, qreg_3[0])
						main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],1,qreg_0[2]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.u(-0.849000,param_1,0.232000, 0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(-0.878000, qreg_0[2])
				main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],1,qreg_3[0]])
			with else_1:
				main_circ.rz(param_0, qreg_0[2])
				main_circ.append(subcirc0,[1,qreg_0[2],0,qreg_3[0]])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.u(pi/2,param_0,param_1, qreg_0[1])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc0,[1,qreg_0[2],0,qreg_0[0]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.rx(-0.793000, qreg_3[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rz(0.727000, qreg_0[0])
					main_circ.u(0.214000,-0.407000,param_0, 1)
					main_circ.id(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(pi/2,-0.730000,param_1, qreg_0[2])
					main_circ.id(1)
			with case_2(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.rx(-0.208000, qreg_0[2])
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.id(1)
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[2])
	with case_3(1):
		main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.959000, param_1: 0.766000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1971")
