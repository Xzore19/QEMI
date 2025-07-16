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
subcirc0.u(0,0,0.396000, qreg_0[2])
subcirc0.ry(0.772000, qreg_0[3])
subcirc0.u(pi/2,-0.162000,0.443000, qreg_0[2])
subcirc0.u(0,0,-0.114000, qreg_0[2])
subcirc0.rx(-0.196000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.318000, qreg_0[0])
subcirc1.ry(0.196000, qreg_0[0])
subcirc1.ry(-0.612000, qreg_2[1])
subcirc1.ry(-0.094000, qreg_2[0])
subcirc1.u(0,0,0.218000, qreg_2[1])
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
subcirc2.ry(-0.568000, qreg_1[1])
subcirc2.ry(-0.526000, qreg_1[1])
subcirc2.u(pi/2,-0.681000,-0.276000, qreg_1[1])
subcirc2.u(pi/2,0.864000,-0.304000, qreg_1[0])
subcirc2.u(pi/2,-0.721000,0.175000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(0,0,0.078000, qreg_1[0])
subcirc3.u(pi/2,-0.730000,-0.026000, qreg_1[2])
subcirc3.u(0,0,-0.725000, qreg_1[2])
subcirc3.u(pi/2,-0.802000,-0.955000, qreg_1[2])
subcirc3.u(0,0,-0.016000, qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,0.828000,-0.344000, qreg_0[0])
subcirc4.rx(-0.466000, qreg_0[0])
subcirc4.u(pi/2,0.717000,0.675000, qreg_3[0])
subcirc4.ry(0.190000, qreg_3[0])
subcirc4.ry(-0.354000, qreg_1[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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
param_4 = Parameter("param_4")

main_circ.rx(param_1, qreg_1[1])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_1[1],qreg_3[0]])
main_circ.ry(0.782000, qreg_1[1])
main_circ.ry(-0.477000, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
main_circ.ry(param_1, qreg_0[0])
main_circ.rx(-0.047000, qreg_1[1])
main_circ.ry(param_4, qreg_1[0])
main_circ.u(param_4,0.802000,-0.957000, qreg_0[0])
main_circ.rx(param_2, qreg_1[1])
main_circ.u(pi/2,0.679000,param_2, qreg_0[0])
main_circ.u(param_3,param_1,0.964000, qreg_1[1])
main_circ.ry(-0.134000, qreg_0[0])
main_circ.rx(0.730000, qreg_3[0])
main_circ.u(param_1,0,param_1, qreg_0[0])
main_circ.u(param_4,param_4,param_1, qreg_0[0])
main_circ.u(param_3,0,-0.177000, qreg_3[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_1[1],qreg_3[0]])
main_circ.u(0,param_1,param_4, qreg_1[1])
main_circ.u(0,0,param_3, qreg_1[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
main_circ.rx(param_2, qreg_3[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.u(pi/2,0.249000,param_2, qreg_1[1])
main_circ.rx(0.220000, qreg_1[1])
bindings = {param_1: -0.454000, param_2: 0.994000, param_3: -0.839000, param_4: 0.376000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
