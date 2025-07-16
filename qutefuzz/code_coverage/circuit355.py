from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.452000,-0.404000, qreg_2[0])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_2[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.y(qreg_2[0])
subcirc1.z(qreg_1[0])
subcirc1.u(pi/2,0.991000,-0.948000, qreg_2[0])
subcirc1.y(qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.870000,0.437000, qreg_1[1])
subcirc2.u(pi/2,0.007000,0.472000, qreg_3[0])
subcirc2.u(pi/2,-0.282000,0.712000, qreg_1[0])
subcirc2.y(qreg_1[1])
subcirc2.u(pi/2,0.931000,0.603000, qreg_1[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_5 = Parameter("param_5")

main_circ.y(0)
main_circ.y(qreg_2[0])
main_circ.u(param_2,param_5,param_2, 1)
main_circ.u(0.807000,0.856000,param_3, 1)
main_circ.u(param_0,param_5,0.169000, qreg_2[1])
main_circ.y(qreg_0[1])
main_circ.u(pi/2,-0.997000,param_0, qreg_2[1])
main_circ.u(0.515000,param_2,0.036000, qreg_0[1])
main_circ.u(param_4,param_2,-0.816000, qreg_0[0])
main_circ.z(0)
main_circ.append(subcirc2,[0,qreg_0[1],1,qreg_2[1]])
main_circ.u(param_1,0.725000,param_0, qreg_2[1])
main_circ.z(qreg_2[1])
main_circ.u(param_0,param_3,param_3, qreg_0[1])
main_circ.u(param_1,param_5,param_1, qreg_2[1])
main_circ.z(1)
main_circ.u(pi/2,param_5,param_0, qreg_0[0])
main_circ.z(qreg_2[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_2[1],0])
main_circ.y(qreg_2[1])
main_circ.u(pi/2,0.189000,param_3, qreg_2[1])
main_circ.u(param_1,-0.733000,-0.809000, qreg_2[0])
main_circ.u(-0.097000,param_0,0.199000, qreg_2[0])
main_circ.y(qreg_0[1])
main_circ.u(param_2,0.410000,param_3, qreg_0[0])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],1,0])
main_circ.z(0)
main_circ.y(qreg_2[1])
bindings = {param_0: 0.703000, param_1: -0.493000, param_2: -0.845000, param_3: 0.746000, param_4: -0.793000, param_5: 0.256000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
