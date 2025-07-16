from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(0.349000, qreg_1[0])
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.ry(0.408000, qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_1[0])
subcirc0.rx(0.662000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.427000, qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[1])
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
subcirc2.cy(qreg_3[0],qreg_1[1])
subcirc2.rx(0.238000, qreg_1[0])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.rx(0.259000, qreg_3[0])
subcirc2.rx(0.055000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.ry(param_2, 3)
main_circ.rx(param_2, 0)
main_circ.ry(0.118000, 1)
main_circ.rx(-0.229000, 2)
main_circ.append(subcirc0,[2,1,qreg_0[0],3])
main_circ.append(subcirc0,[0,3,qreg_0[0],1])
main_circ.cx(1,qreg_0[0])
main_circ.rx(-0.010000, 1)
main_circ.cx(2,1)
main_circ.append(subcirc1,[0,1,qreg_0[0],3,2])
main_circ.append(subcirc1,[1,2,3,qreg_0[0],0])
main_circ.append(subcirc1,[3,2,qreg_0[0],1,0])
main_circ.append(subcirc0,[qreg_0[0],3,0,1])
main_circ.append(subcirc0,[0,3,2,1])
main_circ.ry(0.714000, 3)
main_circ.cx(3,2)
main_circ.ry(-0.620000, 3)
main_circ.cy(1,0)
bindings = {param_2: -0.625000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
