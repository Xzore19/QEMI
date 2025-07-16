from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(-0.288000, qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.ry(0.401000, qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.x(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(-0.341000,-0.771000,0.587000, qreg_0[0])
subcirc1.s(qreg_1[2])
subcirc1.u(-0.616000,0.859000,0.261000, qreg_1[0])
subcirc1.ry(0.659000, qreg_0[0])
subcirc1.x(qreg_1[2])
subcirc1 = subcirc1.to_gate().control(1)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(0.101000,-0.509000,-0.433000, 2)
main_circ.append(subcirc0,[3,1,qreg_0[0],2])
main_circ.x(3)
main_circ.append(subcirc0,[0,qreg_0[0],3,2])
main_circ.x(2)
main_circ.ry(param_2, 0)
main_circ.append(subcirc0,[3,qreg_0[0],2,1])
main_circ.ry(param_1, qreg_0[0])
main_circ.u(-0.156000,param_1,-0.233000, qreg_0[0])
main_circ.append(subcirc1,[1,3,qreg_0[0],0,2])
main_circ.u(param_3,0.214000,param_0, 2)
main_circ.append(subcirc0,[1,2,qreg_0[0],3])
main_circ.append(subcirc1,[qreg_0[0],0,1,2,3])
main_circ.append(subcirc0,[0,2,3,1])
main_circ.u(param_1,0.133000,0.069000, qreg_0[0])
main_circ.s(1)
main_circ.s(3)
bindings = {param_0: -0.407000, param_1: -0.908000, param_2: 0.074000, param_3: 0.767000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
