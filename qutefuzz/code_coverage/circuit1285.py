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
subcirc0.x(qreg_0[0])
subcirc0.u(0.161000,0.084000,0.616000, qreg_3[0])
subcirc0.rx(-0.491000, qreg_0[2])
subcirc0.s(qreg_0[1])
subcirc0.u(0.571000,-0.763000,-0.929000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.u(-0.378000,-0.137000,0.676000, qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.s(qreg_0[2])
subcirc1.u(0.703000,0.311000,0.974000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.278000, qreg_0[1])
subcirc2.x(qreg_2[0])
subcirc2.u(-0.435000,-0.795000,0.875000, qreg_2[0])
subcirc2.rx(-0.576000, qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

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
param_4 = Parameter("param_4")

main_circ.s(1)
main_circ.x(1)
main_circ.u(-0.979000,-0.956000,param_1, 2)
main_circ.append(subcirc1,[3,0,2,qreg_0[0]])
main_circ.x(1)
main_circ.u(0.288000,0.074000,param_4, 2)
main_circ.x(1)
main_circ.s(1)
main_circ.u(0.468000,param_4,param_0, 0)
main_circ.u(param_1,param_0,param_0, 0)
main_circ.u(0.455000,param_4,0.787000, 3)
main_circ.x(qreg_0[0])
main_circ.append(subcirc1,[3,qreg_0[0],1,2])
main_circ.x(1)
main_circ.u(param_0,-0.964000,param_3, 0)
main_circ.u(-0.178000,-0.477000,param_3, 3)
main_circ.rx(-0.448000, 0)
main_circ.x(0)
main_circ.rx(param_2, 1)
main_circ.append(subcirc1,[2,qreg_0[0],0,1])
main_circ.u(-0.310000,-0.700000,0.648000, 2)
main_circ.append(subcirc1,[0,1,3,qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],2,3,0])
main_circ.x(3)
main_circ.x(2)
main_circ.x(qreg_0[0])
bindings = {param_0: 0.609000, param_1: -0.008000, param_2: -0.348000, param_3: -0.582000, param_4: 0.134000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
