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
subcirc0.rz(0.965000, qreg_2[1])
subcirc0.rz(-0.281000, qreg_0[1])
subcirc0.u(pi/2,-0.195000,0.403000, qreg_2[0])
subcirc0.cy(qreg_2[1],qreg_0[0])
subcirc0.cy(qreg_2[1],qreg_0[1])
subcirc0.cy(qreg_2[0],qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.520000, qreg_0[0])
subcirc1.u(-0.464000,0.358000,-0.693000, qreg_0[3])
subcirc1.u(pi/2,0.593000,0.286000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.u(-0.373000,0.282000,-0.284000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.664000,0.398000, qreg_1[1])
subcirc2.u(pi/2,0.055000,-0.089000, qreg_0[0])
subcirc2.u(0.487000,-0.689000,-0.453000, qreg_3[0])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.cy(qreg_1[0],qreg_0[0])
subcirc2.u(pi/2,0.986000,-0.075000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[1,2,0,3])
main_circ.u(pi/2,-0.740000,0.149000, 1)
main_circ.append(subcirc2,[3,2,0,1])
main_circ.u(param_1,param_0,0.736000, 0)
main_circ.u(param_2,0.576000,param_0, 2)
main_circ.cy(1,2)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.cy(0,1)
main_circ.cy(3,2)
main_circ.rz(-0.490000, 0)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.append(subcirc0,[2,3,0,1])
main_circ.cy(1,2)
main_circ.u(pi/2,param_1,-0.448000, 1)
main_circ.cy(0,3)
bindings = {param_0: 0.240000, param_1: -0.327000, param_2: -0.841000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "383")
