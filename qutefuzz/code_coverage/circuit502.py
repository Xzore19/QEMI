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
subcirc0.u(pi/2,-0.844000,-0.100000, qreg_3[0])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.u(0.489000,-0.663000,-0.675000, qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.813000,-0.586000,-0.772000, qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[2])
subcirc1.rz(-0.538000, qreg_0[0])
subcirc1.cx(qreg_0[2],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.891000,-0.204000, qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.u(-0.766000,-0.998000,0.802000, qreg_0[0])
subcirc2.u(pi/2,-0.624000,0.857000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.584000,0.738000,0.442000, qreg_0[1])
subcirc3.rz(0.384000, qreg_0[0])
subcirc3.u(-0.017000,-0.735000,0.392000, qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_2[0])

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

main_circ.u(-0.202000,param_3,param_2, 0)
main_circ.u(pi/2,0.249000,param_1, 1)
main_circ.rz(param_2, 1)
main_circ.append(subcirc3,[2,1,0,3])
main_circ.append(subcirc0,[2,3,1,0])
main_circ.append(subcirc0,[2,3,1,0])
main_circ.cx(1,2)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.rz(param_0, 2)
main_circ.u(0.101000,param_2,param_0, 0)
main_circ.u(param_1,param_0,param_0, 3)
main_circ.append(subcirc3,[3,2,0,1])
main_circ.u(param_0,-0.339000,0.907000, 0)
main_circ.append(subcirc3,[0,2,3,1])
main_circ.u(-0.986000,param_1,0.246000, 2)
main_circ.u(param_2,param_0,param_0, 3)
main_circ.append(subcirc3,[1,2,3,0])
main_circ.cx(1,0)
main_circ.cx(3,1)
main_circ.cx(3,0)
main_circ.cx(0,2)
main_circ.rz(0.429000, 1)
main_circ.append(subcirc3,[3,2,1,0])
main_circ.u(pi/2,param_1,0.487000, 1)
main_circ.u(pi/2,0.291000,0.949000, 1)
main_circ.rz(param_3, 1)
bindings = {param_0: 0.715000, param_1: 0.114000, param_2: 0.406000, param_3: 0.051000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
