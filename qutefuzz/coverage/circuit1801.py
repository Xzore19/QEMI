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
subcirc0.ry(-0.261000, qreg_2[0])
subcirc0.u(-0.787000,-0.111000,0.626000, qreg_2[1])
subcirc0.ry(0.726000, qreg_0[0])
subcirc0.u(0,0,0.732000, qreg_2[1])
subcirc0.u(-0.980000,0.393000,0.056000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(-0.069000, qreg_0[0])
subcirc1.ry(0.135000, qreg_0[0])
subcirc1.ry(0.220000, qreg_2[0])
subcirc1.z(qreg_2[1])
subcirc1.u(0,0,0.325000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.u(0,0,-0.505000, qreg_3[0])
subcirc2.z(qreg_0[2])
subcirc2.ry(0.159000, qreg_3[0])
subcirc2.u(0,0,-0.361000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.978000, qreg_3[0])
subcirc3.u(0,0,-0.990000, qreg_1[0])
subcirc3.u(0,0,-0.684000, qreg_3[0])
subcirc3.ry(0.743000, qreg_2[0])
subcirc3.u(0,0,0.701000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.ry(param_2, 1)
main_circ.append(subcirc1,[1,3,0,2])
main_circ.append(subcirc1,[3,2,1,0])
main_circ.ry(param_2, 3)
main_circ.u(param_0,param_1,0.685000, 1)
main_circ.u(param_0,0,param_0, 2)
main_circ.u(param_1,-0.315000,param_2, 3)
main_circ.append(subcirc2,[2,3,0,1])
main_circ.u(param_1,param_1,param_1, 3)
main_circ.u(param_1,param_1,param_2, 1)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.ry(-0.328000, 2)
main_circ.u(param_2,param_0,param_1, 0)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.ry(param_2, 1)
main_circ.append(subcirc1,[2,1,3,0])
main_circ.u(param_1,param_0,0.744000, 1)
main_circ.u(param_0,0,param_1, 2)
bindings = {param_0: 0.053000, param_1: -0.239000, param_2: 0.514000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
