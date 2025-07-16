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
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0.ry(-0.807000, qreg_0[2])
subcirc0.ry(0.380000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_1[1])
subcirc1.u(0.786000,-0.673000,-0.696000, qreg_1[1])
subcirc1.z(qreg_1[0])
subcirc1.h(qreg_1[1])
subcirc1.z(qreg_1[1])
subcirc1.ry(0.532000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.h(qreg_1[0])
subcirc2.ry(0.924000, qreg_2[1])
subcirc2.u(0.555000,0.110000,-0.078000, qreg_2[1])
subcirc2.z(qreg_1[0])
subcirc2.u(0.624000,-0.990000,0.064000, qreg_1[0])
subcirc2.u(0.933000,0.746000,0.500000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

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

main_circ.ry(-0.157000, qreg_0[0])
main_circ.h(0)
main_circ.z(2)
main_circ.ry(param_1, 0)
main_circ.u(param_1,0.723000,param_0, 1)
main_circ.u(param_1,param_0,param_0, 3)
main_circ.z(1)
main_circ.u(-0.292000,param_0,param_0, 1)
main_circ.ry(param_1, 0)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.h(0)
main_circ.h(0)
main_circ.h(2)
main_circ.z(1)
main_circ.append(subcirc0,[qreg_0[0],2,3,1])
main_circ.z(1)
main_circ.u(0.450000,0.179000,param_0, 2)
main_circ.z(0)
main_circ.z(2)
main_circ.append(subcirc0,[3,2,1,0])
main_circ.h(2)
main_circ.z(0)
main_circ.u(-0.655000,0.150000,0.242000, 0)
main_circ.u(-0.746000,param_1,-0.821000, 2)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.z(2)
main_circ.u(param_1,param_0,0.877000, qreg_0[0])
bindings = {param_0: -0.794000, param_1: 0.601000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
