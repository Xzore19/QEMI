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
subcirc0.u(0,0,-0.549000, qreg_0[2])
subcirc0.y(qreg_0[1])
subcirc0.u(-0.877000,0.555000,-0.046000, qreg_0[2])
subcirc0.u(0,0,0.185000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.574000,-0.111000,0.525000, qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.y(qreg_0[1])
subcirc1.u(-0.176000,0.147000,-0.210000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.478000, qreg_0[3])
subcirc2.y(qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[3])
subcirc2.u(0,0,0.424000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.cy(1,3)
main_circ.append(subcirc2,[1,3,2,0,qreg_0[0]])
main_circ.cy(1,3)
main_circ.y(0)
main_circ.u(0,0,param_0, 0)
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_1[0],2])
main_circ.y(3)
main_circ.y(qreg_0[0])
main_circ.u(-0.206000,param_1,param_0, 0)
main_circ.append(subcirc2,[0,qreg_1[0],2,3,1])
main_circ.y(0)
main_circ.u(0.737000,param_1,0.877000, 3)
main_circ.u(0.768000,0.596000,param_0, 2)
main_circ.y(2)
main_circ.u(0,param_0,param_1, qreg_0[0])
main_circ.y(3)
main_circ.y(qreg_0[0])
main_circ.u(-0.410000,0.860000,0.276000, 0)
main_circ.u(0,param_1,param_1, 0)
main_circ.cy(2,0)
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.cy(1,qreg_0[0])
main_circ.cy(0,qreg_1[0])
main_circ.cy(0,2)
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.cy(2,1)
main_circ.cy(1,qreg_1[0])
main_circ.cy(2,qreg_0[0])
main_circ.u(param_0,param_1,param_0, 1)
main_circ.cy(1,qreg_1[0])
main_circ.u(param_1,-0.584000,param_1, 1)
bindings = {param_0: 0.130000, param_1: -0.950000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
