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
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.ry(-0.081000, qreg_0[1])
subcirc0.u(pi/2,-0.792000,-0.149000, qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[2])
subcirc0.u(pi/2,-0.176000,-0.455000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.282000,0.872000, qreg_0[0])
subcirc1.u(pi/2,-0.231000,0.980000, qreg_0[3])
subcirc1.ry(-0.197000, qreg_0[3])
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.ry(-0.094000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.994000,0.223000, qreg_0[0])
subcirc2.ry(-0.501000, qreg_0[0])
subcirc2.ry(0.980000, qreg_0[1])
subcirc2.ry(-0.629000, qreg_0[2])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.ry(-0.110000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(0.163000, qreg_0[0])
subcirc3.u(pi/2,-0.510000,0.188000, qreg_0[1])
subcirc3.ry(0.548000, qreg_0[2])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.ry(-0.590000, qreg_0[3])
subcirc3.cz(qreg_0[2],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_6 = Parameter("param_6")

main_circ.append(subcirc1,[0,qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.ry(0.123000, qreg_0[0])
main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.append(subcirc2,[0,qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[1],qreg_2[0],0])
main_circ.ry(-0.041000, qreg_0[1])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.append(subcirc2,[qreg_2[0],0,qreg_2[1],qreg_0[0]])
main_circ.ry(param_0, qreg_2[1])
main_circ.ry(param_4, qreg_0[1])
main_circ.cz(qreg_2[1],qreg_2[0])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.append(subcirc2,[qreg_2[0],qreg_2[1],qreg_0[1],0])
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.cy(qreg_0[1],qreg_2[1])
bindings = {param_0: -0.592000, param_4: 0.320000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
