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
subcirc0.u(pi/2,-0.523000,-0.993000, qreg_0[2])
subcirc0.u(0.035000,0.077000,-0.389000, qreg_0[2])
subcirc0.u(pi/2,0.457000,0.715000, qreg_0[1])
subcirc0.u(0.523000,-0.546000,-0.174000, qreg_0[1])
subcirc0.s(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.239000, qreg_0[1])
subcirc1.rz(0.746000, qreg_3[0])
subcirc1.u(pi/2,0.264000,0.936000, qreg_0[1])
subcirc1.u(0.568000,0.885000,-0.076000, qreg_0[2])
subcirc1.rz(0.280000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.415000,-1.000000,0.699000, qreg_0[2])
subcirc2.u(pi/2,0.637000,-0.924000, qreg_0[2])
subcirc2.s(qreg_3[0])
subcirc2.u(-0.355000,-0.186000,0.660000, qreg_0[0])
subcirc2.u(pi/2,-0.867000,0.332000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,0.384000,-0.355000, qreg_0[2])
subcirc3.s(qreg_0[0])
subcirc3.rz(-0.848000, qreg_0[2])
subcirc3.u(pi/2,0.890000,-0.659000, qreg_0[0])
subcirc3.u(pi/2,0.456000,0.841000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(3)
		main_circ.u(param_2,param_0,0.511000, 1)
		main_circ.barrier(1)
	with case_1(1):
		main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.464000,0.811000,param_1, 3)
	main_circ.append(subcirc3,[0,3,1,2,qreg_0[0]])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[1,qreg_0[0],0,qreg_1[0]])
	with case_1(1):
		main_circ.s(3)
		main_circ.u(param_2,0.912000,-0.426000, 1)
		main_circ.u(param_3,-0.564000,param_0, 1)
		main_circ.u(0.493000,0.222000,0.314000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,0.309000,-0.350000, qreg_0[0])
	main_circ.id(0)
with else_1:
	main_circ.append(subcirc3,[qreg_0[0],1,3,0,2])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.192000,-0.156000,-0.527000, 3)
with else_1:
	main_circ.rz(0.489000, 1)
	main_circ.rz(param_1, 3)
	main_circ.append(subcirc1,[qreg_0[0],3,0,qreg_1[0]])
main_circ.u(param_3,0.036000,0.480000, 1)
main_circ.u(0.389000,-0.387000,param_0, 0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(1)
	with case_1(1):
		main_circ.u(-0.345000,-0.474000,0.748000, qreg_0[0])
		main_circ.rz(param_0, 1)
		main_circ.id(qreg_0[0])
main_circ.u(-0.836000,param_0,0.844000, 3)
main_circ.rz(param_3, 1)
main_circ.u(param_0,0.577000,param_0, qreg_1[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_2,param_0,param_2, 2)
	main_circ.append(subcirc3,[2,3,1,qreg_1[0],qreg_0[0]])
with else_1:
	main_circ.u(pi/2,-0.758000,param_1, qreg_1[0])
	main_circ.append(subcirc3,[3,2,1,qreg_0[0],0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.s(0)
	main_circ.u(pi/2,param_2,param_3, 0)
	main_circ.append(subcirc3,[0,qreg_0[0],2,1,3])
with else_1:
	main_circ.u(param_2,param_3,-0.852000, 2)
	main_circ.rz(0.372000, qreg_1[0])
bindings = {param_0: 0.741000, param_1: 0.238000, param_2: 0.655000, param_3: 0.972000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1776", "Collect2qBlocks")
