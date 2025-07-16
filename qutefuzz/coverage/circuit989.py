from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(pi/2,0.150000,0.777000, qreg_1[1])
subcirc0.y(qreg_1[0])
subcirc0.ry(0.358000, qreg_1[1])
subcirc0.u(0,0,0.009000, qreg_1[0])
subcirc0.ry(0.465000, qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.247000, qreg_2[0])
subcirc1.u(pi/2,0.301000,0.850000, qreg_2[1])
subcirc1.u(pi/2,0.393000,-0.880000, qreg_2[1])
subcirc1.u(pi/2,0.803000,0.303000, qreg_2[0])
subcirc1.u(pi/2,-0.336000,0.093000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.543000, qreg_1[1])
subcirc2.y(qreg_3[0])
subcirc2.ry(-0.876000, qreg_3[0])
subcirc2.ry(-0.843000, qreg_3[0])
subcirc2.u(pi/2,0.740000,0.938000, qreg_3[0])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc0,[3,0,1,2])
main_circ.ry(0.437000, 3)
main_circ.ry(-0.108000, 1)
main_circ.ry(param_6, 3)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.u(0,param_6,param_2, 3)
main_circ.append(subcirc0,[3,1,2,0])
main_circ.y(2)
main_circ.u(pi/2,-0.499000,param_4, 1)
main_circ.y(0)
main_circ.y(2)
main_circ.ry(param_6, 0)
main_circ.y(2)
main_circ.u(param_6,param_5,-0.945000, 3)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.append(subcirc2,[0,2,3,1])
main_circ.u(param_6,param_1,param_3, 3)
main_circ.append(subcirc2,[3,1,0,2])
main_circ.append(subcirc0,[3,1,2,0])
main_circ.y(1)
main_circ.y(2)
main_circ.append(subcirc0,[3,2,1,0])
bindings = {param_1: -0.620000, param_2: -0.976000, param_3: 0.523000, param_4: 0.365000, param_5: -0.377000, param_6: 0.913000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
