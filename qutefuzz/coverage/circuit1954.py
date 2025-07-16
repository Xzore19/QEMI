from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.ry(-0.649000, qreg_0[1])
subcirc0.s(qreg_0[3])
subcirc0.cy(qreg_0[2],qreg_0[3])
subcirc0.u(0,0,-0.938000, qreg_0[1])
subcirc0.s(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.617000, qreg_2[1])
subcirc1.s(qreg_0[1])
subcirc1.ry(-1.000000, qreg_2[0])
subcirc1.ry(-0.234000, qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_2[1])
subcirc1.ry(0.779000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0,0,-0.319000, qreg_0[1])
subcirc2.ry(-0.659000, qreg_2[1])
subcirc2.u(0,0,0.164000, qreg_2[0])
subcirc2.ry(-0.670000, qreg_0[0])
subcirc2.ry(-0.761000, qreg_2[0])
subcirc2.s(qreg_2[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.ry(0.269000, qreg_0[3])
subcirc3.u(0,0,-0.202000, qreg_0[2])
subcirc3.s(qreg_0[0])
subcirc3.cy(qreg_0[0],qreg_0[2])
subcirc3.u(0,0,0.173000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0,0,-0.910000, qreg_0[1])
subcirc4.cy(qreg_0[1],qreg_0[3])
subcirc4.cy(qreg_0[1],qreg_0[3])
subcirc4.s(qreg_0[2])
subcirc4.s(qreg_0[2])
subcirc4.cy(qreg_0[2],qreg_0[1])

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
param_2 = Parameter("param_2")

main_circ.ry(param_1, qreg_0[0])
main_circ.ry(0.405000, qreg_0[1])
main_circ.s(qreg_3[0])
main_circ.append(subcirc4,[qreg_0[0],1,qreg_0[2],qreg_3[0]])
main_circ.u(0,0,param_2, qreg_0[2])
main_circ.s(qreg_3[0])
main_circ.append(subcirc4,[qreg_3[0],0,qreg_0[2],qreg_0[1]])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.u(0,param_1,param_0, 0)
main_circ.u(param_0,param_2,param_1, 0)
main_circ.append(subcirc4,[qreg_0[2],1,qreg_0[0],0])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[2],0,1])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cy(1,qreg_0[2])
main_circ.cy(qreg_0[1],0)
main_circ.u(param_0,param_0,-0.614000, qreg_0[0])
main_circ.cy(1,qreg_0[1])
main_circ.append(subcirc4,[0,1,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc4,[0,qreg_3[0],qreg_0[2],1])
main_circ.append(subcirc4,[1,qreg_0[0],0,qreg_0[1]])
main_circ.s(0)
main_circ.u(0,param_0,-0.975000, 0)
main_circ.ry(param_2, qreg_0[0])
main_circ.ry(-0.673000, qreg_3[0])
main_circ.s(qreg_0[0])
bindings = {param_0: -0.146000, param_1: 0.141000, param_2: 0.049000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
