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
subcirc0.s(qreg_0[2])
subcirc0.u(0,0,-0.238000, qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.896000, qreg_2[1])
subcirc1.u(0,0,-0.453000, qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.s(qreg_2[1])
subcirc1.u(0.922000,0.953000,-0.138000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.cy(qreg_0[0],qreg_0[3])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.u(0.720000,0.524000,-0.726000, qreg_0[2])
subcirc2.s(qreg_0[3])
subcirc2.u(0.141000,-0.609000,0.581000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[0],qreg_1[1],qreg_0[0]])
main_circ.cy(qreg_1[2],qreg_1[1])
main_circ.u(param_2,0,0.755000, qreg_1[1])
main_circ.cy(qreg_1[2],qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
main_circ.u(-0.577000,param_2,0.092000, qreg_1[1])
main_circ.u(param_0,param_1,param_0, qreg_1[0])
main_circ.s(qreg_1[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.cy(qreg_0[0],qreg_1[2])
main_circ.u(0.541000,-0.156000,-0.506000, qreg_1[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.u(param_0,-0.583000,0.840000, qreg_1[2])
main_circ.u(0,param_0,0.017000, qreg_1[1])
main_circ.u(-0.419000,param_0,-0.756000, qreg_1[2])
main_circ.cy(qreg_1[2],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.u(param_0,0.462000,param_0, qreg_0[0])
main_circ.u(param_0,param_2,param_1, qreg_1[2])
main_circ.u(param_1,param_0,-0.470000, qreg_1[0])
bindings = {param_0: 0.174000, param_1: 0.696000, param_2: 0.235000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
