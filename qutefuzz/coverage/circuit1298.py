from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.u(0,0,0.041000, qreg_1[0])
subcirc0.u(0,0,0.037000, qreg_1[0])
subcirc0.u(0,0,0.307000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.ry(0.907000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1.ry(-0.196000, qreg_0[0])
subcirc1.u(0,0,-0.157000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_3[0])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.cy(qreg_0[2],qreg_3[0])
subcirc2.ry(0.298000, qreg_3[0])
subcirc2.ry(0.726000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc2,[1,0,2,3])
main_circ.u(0,param_0,0.736000, 3)
main_circ.ry(-0.106000, 3)
main_circ.cy(0,1)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.cy(1,2)
main_circ.u(0,0,param_0, 3)
main_circ.cy(2,1)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.cy(3,0)
main_circ.cy(2,3)
main_circ.u(param_2,param_0,0.663000, 1)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.cz(1,2)
main_circ.ry(param_1, 1)
main_circ.ry(0.766000, 1)
main_circ.u(0,0,0.824000, 3)
main_circ.ry(-0.340000, 3)
main_circ.cy(2,1)
main_circ.cz(3,2)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.append(subcirc2,[1,3,2,0])
main_circ.u(param_2,param_0,param_2, 1)
bindings = {param_0: 0.250000, param_1: 0.021000, param_2: -0.441000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
