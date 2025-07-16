from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0.194000,-0.460000,param_0, qreg_0[0])
		main_circ.cy(qreg_3[0],qreg_0[2])
		main_circ.rz(-0.326000, qreg_0[1])
		main_circ.u(-0.126000,param_1,-0.546000, qreg_0[0])
	with case_1(1):
		main_circ.u(0.687000,param_1,-0.934000, qreg_0[2])
		main_circ.s(qreg_0[2])
		main_circ.u(param_1,-0.822000,0.109000, qreg_0[1])
		main_circ.u(param_0,-0.454000,param_0, qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_1,param_1, qreg_0[0])
		main_circ.cy(qreg_3[0],qreg_0[1])
		main_circ.cy(qreg_0[2],qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_3[0])
	with case_1(1):
		main_circ.u(0.757000,0.512000,param_0, qreg_0[0])
		main_circ.u(param_1,param_1,param_1, qreg_0[2])
		main_circ.rz(0.352000, qreg_0[0])
		main_circ.u(param_1,-0.190000,param_1, qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_0[2],qreg_0[1])
	main_circ.cy(qreg_0[1],qreg_3[0])
	main_circ.cy(qreg_3[0],qreg_0[1])
	main_circ.u(param_0,-0.181000,param_0, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.s(qreg_0[1])
	main_circ.u(-0.631000,-0.989000,0.548000, qreg_0[2])
	main_circ.cy(qreg_0[1],qreg_0[0])
	main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0.260000,param_0,0.040000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[2])
		main_circ.s(qreg_0[1])
		main_circ.s(qreg_0[2])
		main_circ.cy(qreg_0[2],qreg_0[1])
	with case_1(1):
		main_circ.cy(qreg_0[1],qreg_0[2])
		main_circ.cy(qreg_0[2],qreg_3[0])
		main_circ.cy(qreg_0[0],qreg_0[2])
		main_circ.u(-0.662000,param_0,param_1, qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_3[0],qreg_0[0])
	main_circ.s(qreg_0[2])
	main_circ.s(qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_3[0],qreg_0[1])
	main_circ.s(qreg_0[0])
	main_circ.rz(param_1, qreg_3[0])
	main_circ.u(param_0,param_0,0.962000, qreg_0[2])
bindings = {param_0: 0.247000, param_1: 0.895000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1231", "ElidePermutations")
