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
subcirc0.rz(0.120000, qreg_0[0])
subcirc0.ry(0.452000, qreg_1[2])
subcirc0.ry(-0.785000, qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,-0.394000,-0.535000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.426000, qreg_2[0])
subcirc1.u(pi/2,-0.991000,0.903000, qreg_0[0])
subcirc1.u(pi/2,0.618000,-0.519000, qreg_3[0])
subcirc1.rz(-0.210000, qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_1[1])
subcirc2.rz(0.111000, qreg_0[0])
subcirc2.y(qreg_0[0])
subcirc2.u(pi/2,0.435000,0.810000, qreg_0[0])
subcirc2.u(pi/2,0.058000,0.764000, qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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
param_5 = Parameter("param_5")

main_circ.append(subcirc2,[0,2,qreg_0[0],3])
main_circ.y(0)
main_circ.u(pi/2,param_5,-0.642000, qreg_0[1])
main_circ.append(subcirc1,[0,1,qreg_0[0],2,3])
main_circ.append(subcirc1,[3,qreg_0[0],2,0,qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[0],3,qreg_0[1],0,1])
main_circ.u(param_5,param_3,0.772000, 0)
main_circ.ry(param_0, 0)
main_circ.u(param_0,param_2,0.327000, 0)
main_circ.append(subcirc2,[qreg_0[1],3,0,1])
main_circ.u(param_2,-0.333000,0.292000, 2)
main_circ.append(subcirc2,[0,1,2,3])
main_circ.rz(0.367000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],2,0,3])
main_circ.rz(0.993000, qreg_0[1])
main_circ.ry(param_0, 0)
main_circ.append(subcirc1,[1,qreg_0[1],2,qreg_0[0],0])
main_circ.ry(0.213000, 3)
main_circ.ry(param_2, 2)
main_circ.rz(param_4, qreg_0[0])
main_circ.y(3)
bindings = {param_0: -0.196000, param_2: 0.309000, param_3: -0.994000, param_4: -0.983000, param_5: 0.815000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
