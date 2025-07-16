from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.ry(0.586000, qreg_2[0])
subcirc0.z(qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_1[1])
subcirc1.cx(qreg_0[0],qreg_1[1])
subcirc1.ry(0.034000, qreg_1[0])
subcirc1.h(qreg_1[0])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_2[0])
subcirc2.ry(-0.098000, qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.107000, qreg_3[0])
subcirc3.ry(0.762000, qreg_0[2])
subcirc3.ry(0.881000, qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_3[0])
subcirc3.z(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.cx(3,0)
main_circ.z(3)
main_circ.h(1)
main_circ.ry(param_3, 1)
main_circ.ry(param_5, 0)
main_circ.ry(param_4, 1)
main_circ.h(1)
main_circ.h(2)
main_circ.ry(0.803000, 3)
main_circ.z(3)
main_circ.append(subcirc0,[0,3,2,1])
main_circ.append(subcirc1,[0,3,1,2])
main_circ.z(3)
main_circ.append(subcirc1,[3,1,2,0])
main_circ.append(subcirc1,[3,2,1,0])
main_circ.h(2)
main_circ.cx(0,2)
main_circ.cx(0,3)
main_circ.cx(2,1)
main_circ.cx(3,1)
main_circ.cx(0,2)
main_circ.cx(1,2)
main_circ.cx(3,0)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.ry(param_0, 3)
main_circ.ry(0.668000, 2)
bindings = {param_0: 0.920000, param_3: 0.461000, param_4: -0.845000, param_5: 0.206000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
