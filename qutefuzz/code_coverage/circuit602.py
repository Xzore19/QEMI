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
subcirc0.cx(qreg_1[2],qreg_1[1])
subcirc0.u(pi/2,-0.888000,0.149000, qreg_1[0])
subcirc0.cx(qreg_1[0],qreg_1[1])
subcirc0.ry(-0.619000, qreg_1[1])
subcirc0.ry(0.822000, qreg_1[2])
subcirc0.u(pi/2,0.224000,-0.982000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[3])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.ry(-0.719000, qreg_0[1])
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.ry(-0.205000, qreg_0[1])
subcirc1.u(pi/2,0.865000,-0.050000, qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cy(qreg_1[1],0)
main_circ.append(subcirc1,[qreg_0[0],qreg_1[2],0,qreg_1[0]])
main_circ.u(param_0,param_1,-0.938000, qreg_1[0])
main_circ.ry(-0.546000, qreg_1[0])
main_circ.u(param_0,0.430000,0.153000, qreg_1[0])
main_circ.u(param_0,0.758000,param_2, qreg_1[2])
main_circ.append(subcirc1,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
main_circ.ry(param_1, 0)
main_circ.ry(param_2, qreg_1[1])
main_circ.append(subcirc1,[qreg_1[1],0,qreg_0[0],qreg_1[0]])
main_circ.cx(0,qreg_1[1])
main_circ.ry(-0.251000, 0)
main_circ.ry(0.170000, qreg_0[0])
main_circ.cx(qreg_1[2],qreg_1[0])
main_circ.ry(0.959000, qreg_1[1])
main_circ.u(pi/2,param_2,-0.962000, qreg_1[2])
main_circ.u(param_2,param_2,param_2, qreg_1[0])
main_circ.cx(qreg_1[2],qreg_1[1])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.u(param_0,0.537000,param_0, qreg_1[1])
main_circ.cx(qreg_1[1],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[2])
main_circ.append(subcirc1,[qreg_1[2],0,qreg_1[0],qreg_1[1]])
main_circ.u(param_2,param_0,-0.124000, qreg_1[2])
main_circ.cy(qreg_1[2],0)
main_circ.cx(qreg_1[1],qreg_0[0])
main_circ.u(pi/2,0.428000,param_1, qreg_0[0])
main_circ.ry(param_0, qreg_1[0])
main_circ.u(param_2,param_1,param_2, qreg_0[0])
main_circ.u(param_1,param_0,-0.358000, qreg_0[0])
bindings = {param_0: -0.709000, param_1: -0.201000, param_2: 0.849000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
