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
subcirc0.rz(-0.780000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.rz(-0.677000, qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.rz(0.926000, qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.rz(0.435000, qreg_0[2])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.603000, qreg_0[0])
subcirc2.x(qreg_0[2])
subcirc2.rz(0.455000, qreg_0[1])
subcirc2.rz(-0.564000, qreg_0[2])
subcirc2.z(qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rz(param_2, qreg_0[0])
main_circ.cy(1,qreg_0[2])
main_circ.cy(1,qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.append(subcirc2,[0,qreg_0[1],1,qreg_0[0]])
main_circ.x(qreg_3[0])
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.z(1)
main_circ.append(subcirc2,[0,1,qreg_0[2],qreg_3[0]])
main_circ.rz(param_3, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],0,qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],1])
main_circ.cy(qreg_0[1],1)
main_circ.cy(qreg_0[2],0)
main_circ.rz(param_3, qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.cy(qreg_0[2],0)
main_circ.cy(qreg_0[1],0)
main_circ.cy(0,qreg_0[1])
main_circ.cy(qreg_3[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cy(1,qreg_3[0])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.cy(1,qreg_3[0])
main_circ.cy(0,qreg_3[0])
main_circ.cy(0,qreg_0[1])
main_circ.cy(0,qreg_3[0])
main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[0],0)
bindings = {param_2: -0.688000, param_3: -0.231000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
