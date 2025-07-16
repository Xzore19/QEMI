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
subcirc0.u(0,0,-0.405000, qreg_0[1])
subcirc0.u(0,0,-0.704000, qreg_0[1])
subcirc0.z(qreg_0[2])
subcirc0.u(0,0,0.916000, qreg_3[0])
subcirc0.rz(0.905000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.600000, qreg_1[0])
subcirc1.cx(qreg_3[0],qreg_1[0])
subcirc1.z(qreg_3[0])
subcirc1.u(0,0,0.070000, qreg_1[0])
subcirc1.z(qreg_1[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_2[0],qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2.rz(0.568000, qreg_2[0])
subcirc2.u(0,0,0.171000, qreg_3[0])
subcirc2.rz(0.748000, qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_1[1],qreg_0[0])
subcirc3.rz(0.692000, qreg_0[0])
subcirc3.u(0,0,0.834000, qreg_3[0])
subcirc3.cx(qreg_1[0],qreg_3[0])
subcirc3.rz(-0.644000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(0)
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
param_3 = Parameter("param_3")

main_circ.u(param_3,param_0,param_0, qreg_0[2])
main_circ.z(qreg_0[2])
main_circ.rz(0.509000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.rz(param_2, qreg_3[0])
main_circ.u(0,0,-0.658000, qreg_0[1])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.rz(0.385000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.rz(param_0, qreg_3[0])
main_circ.rz(-0.214000, qreg_0[1])
main_circ.u(param_2,param_1,param_3, qreg_3[0])
main_circ.rz(param_2, qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.u(0,param_1,param_1, qreg_0[1])
main_circ.rz(-0.760000, qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.u(param_0,param_2,0.447000, qreg_0[1])
main_circ.rz(param_2, qreg_0[0])
main_circ.u(0,0,param_2, qreg_0[1])
main_circ.u(param_2,param_2,param_0, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(qreg_0[2],qreg_0[1])
bindings = {param_0: -0.916000, param_1: -0.829000, param_2: 0.174000, param_3: -0.048000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
