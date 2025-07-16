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
subcirc0.u(0,0,0.999000, qreg_1[0])
subcirc0.u(pi/2,-0.108000,0.534000, qreg_1[0])
subcirc0.u(pi/2,-0.289000,0.515000, qreg_1[1])
subcirc0.y(qreg_1[0])
subcirc0.u(0,0,-0.692000, qreg_1[1])
subcirc0.z(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.685000, qreg_0[0])
subcirc1.u(0,0,0.004000, qreg_0[2])
subcirc1.u(pi/2,0.124000,0.643000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.u(0,0,0.889000, qreg_0[1])
subcirc1.u(pi/2,-0.036000,0.033000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[2])
subcirc2.u(0,0,-0.265000, qreg_0[2])
subcirc2.u(pi/2,0.672000,0.082000, qreg_0[0])
subcirc2.y(qreg_0[1])
subcirc2.u(0,0,0.366000, qreg_0[2])
subcirc2.u(pi/2,-0.633000,0.293000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.y(qreg_0[0])
main_circ.u(0,param_2,param_2, 1)
main_circ.append(subcirc1,[2,1,qreg_0[0],3])
main_circ.u(pi/2,param_3,-0.768000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],0,2,1])
main_circ.u(param_0,-0.498000,-0.033000, 0)
main_circ.append(subcirc1,[0,qreg_0[0],3,2])
main_circ.y(3)
main_circ.u(param_1,0.728000,param_0, 1)
main_circ.u(param_2,param_3,-0.336000, 2)
main_circ.append(subcirc0,[qreg_0[0],0,3,1])
main_circ.u(param_1,param_2,param_0, 3)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.u(param_4,param_0,0.313000, 3)
main_circ.u(pi/2,0.444000,-0.660000, 0)
main_circ.y(2)
main_circ.u(0,0,-0.052000, 2)
main_circ.append(subcirc1,[1,3,qreg_0[0],2])
main_circ.u(0,param_2,0.046000, 1)
main_circ.y(3)
main_circ.y(2)
main_circ.u(param_3,0,param_2, 0)
main_circ.y(1)
bindings = {param_0: 0.098000, param_1: -0.043000, param_2: 0.896000, param_3: 0.161000, param_4: 0.709000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
