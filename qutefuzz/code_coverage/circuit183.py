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
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rz(0.904000, qreg_0[0])
subcirc0.u(0.165000,0.579000,-0.414000, qreg_3[0])
subcirc0.h(qreg_2[0])
subcirc0.u(0.312000,0.894000,0.608000, qreg_0[0])
subcirc0.h(qreg_0[0])

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
subcirc1.u(-0.873000,0.761000,-0.149000, qreg_3[0])
subcirc1.rz(-0.038000, qreg_3[0])
subcirc1.u(-0.132000,0.413000,0.056000, qreg_1[0])
subcirc1.u(0.965000,0.761000,0.733000, qreg_0[0])
subcirc1.h(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.h(qreg_1[2])
subcirc2.h(qreg_1[1])
subcirc2.h(qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc2,[0,3,qreg_0[0],1,2])
main_circ.u(-0.102000,0.025000,-0.503000, 2)
main_circ.append(subcirc2,[0,1,3,qreg_0[0],2])
main_circ.x(3)
main_circ.append(subcirc0,[1,3,2,qreg_0[0]])
main_circ.append(subcirc1,[1,0,2,qreg_0[0]])
main_circ.h(0)
main_circ.x(2)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.u(-0.598000,-0.095000,param_0, qreg_0[0])
main_circ.rz(-0.530000, qreg_0[0])
main_circ.u(0.252000,param_0,param_0, 2)
main_circ.append(subcirc0,[3,qreg_0[0],1,0])
main_circ.append(subcirc2,[qreg_0[0],1,0,2,3])
bindings = {param_0: -0.902000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
