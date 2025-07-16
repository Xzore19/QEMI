from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.s(qreg_1[1])
subcirc0.rx(-0.653000, qreg_1[1])
subcirc0.rx(-0.063000, qreg_1[2])
subcirc0.cx(qreg_1[0],qreg_1[1])
subcirc0.u(pi/2,0.841000,0.692000, qreg_1[1])
subcirc0.cx(qreg_1[2],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.934000, qreg_0[3])
subcirc1.s(qreg_0[3])
subcirc1.s(qreg_0[1])
subcirc1.u(pi/2,-0.830000,0.502000, qreg_0[3])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[2],qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cx(qreg_1[0],qreg_1[1])
subcirc2.s(qreg_0[0])
subcirc2.u(pi/2,0.635000,0.199000, qreg_1[0])
subcirc2.u(pi/2,-0.037000,0.424000, qreg_1[2])
subcirc2.u(pi/2,0.541000,-0.326000, qreg_1[2])
subcirc2.s(qreg_1[2])

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

main_circ.cx(2,3)
main_circ.append(subcirc2,[qreg_0[0],1,0,3])
main_circ.s(0)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.u(param_0,0.455000,param_0, qreg_0[0])
main_circ.cx(1,2)
main_circ.u(param_1,-0.920000,param_2, 1)
main_circ.rx(-0.544000, qreg_0[0])
main_circ.rx(0.711000, 3)
main_circ.u(pi/2,param_2,param_0, 1)
main_circ.cx(1,3)
main_circ.cx(0,qreg_0[0])
main_circ.rx(0.521000, 0)
main_circ.append(subcirc0,[3,1,qreg_0[0],0])
main_circ.rx(-0.867000, 0)
main_circ.rx(param_1, 1)
main_circ.append(subcirc2,[3,2,qreg_0[0],0])
main_circ.append(subcirc2,[2,0,1,3])
main_circ.cx(2,1)
main_circ.cx(3,1)
main_circ.cx(1,qreg_0[0])
main_circ.cx(1,qreg_0[0])
main_circ.cx(3,2)
main_circ.cx(3,0)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.u(pi/2,param_0,param_1, 0)
main_circ.rx(0.127000, 0)
main_circ.cx(qreg_0[0],2)
main_circ.cx(1,3)
bindings = {param_0: -0.522000, param_1: 0.992000, param_2: 0.264000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "168")
