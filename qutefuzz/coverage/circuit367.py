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
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[2])
subcirc0.y(qreg_0[2])
subcirc0.rz(0.000000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_2[0])
subcirc1.y(qreg_2[0])
subcirc1.h(qreg_1[0])
subcirc1.rz(-0.767000, qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.208000, qreg_0[2])
subcirc2.h(qreg_0[2])
subcirc2.y(qreg_3[0])
subcirc2.cy(qreg_0[1],qreg_0[0])
subcirc2.rz(-0.345000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.h(qreg_2[1])
subcirc3.rz(0.723000, qreg_2[0])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_2[0])
subcirc3.y(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.cy(qreg_0[0],qreg_1[2])
subcirc4.h(qreg_1[1])
subcirc4.y(qreg_0[0])
subcirc4.y(qreg_1[0])
subcirc4.cy(qreg_1[0],qreg_1[1])

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

main_circ.append(subcirc4,[3,2,0,qreg_0[0]])
main_circ.append(subcirc2,[2,0,1,3])
main_circ.append(subcirc1,[1,2,3,qreg_0[0]])
main_circ.h(2)
main_circ.y(2)
main_circ.append(subcirc2,[qreg_0[0],3,2,0])
main_circ.rz(param_1, 0)
main_circ.y(1)
main_circ.append(subcirc4,[3,2,qreg_0[0],0])
main_circ.y(2)
main_circ.y(qreg_0[0])
main_circ.rz(0.177000, 0)
main_circ.rz(0.774000, 0)
main_circ.append(subcirc1,[1,2,qreg_0[0],0])
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[0],3)
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_0[0],1)
main_circ.cy(2,1)
main_circ.cy(3,qreg_0[0])
main_circ.cy(0,2)
main_circ.append(subcirc1,[2,0,qreg_0[0],3])
bindings = {param_1: -0.584000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
