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
subcirc0.s(qreg_0[2])
subcirc0.u(-0.470000,-0.555000,0.291000, qreg_0[1])
subcirc0.u(0,0,-0.264000, qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.535000,0.219000,-0.046000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc1,[1,qreg_0[0],0,3])
main_circ.s(3)
main_circ.s(3)
main_circ.s(3)
main_circ.s(3)
main_circ.u(param_4,0.896000,-0.314000, 0)
main_circ.u(0,0,-0.690000, 1)
main_circ.u(param_6,-0.782000,param_4, 3)
main_circ.u(param_1,-0.913000,-0.059000, qreg_0[0])
main_circ.s(0)
main_circ.cx(1,3)
main_circ.append(subcirc1,[2,qreg_0[0],1,3])
main_circ.cx(0,1)
main_circ.cx(3,2)
main_circ.u(0,0,param_2, qreg_0[0])
main_circ.cx(1,0)
main_circ.cx(3,2)
main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
main_circ.u(param_6,-0.718000,param_3, 2)
main_circ.s(qreg_0[0])
main_circ.s(1)
main_circ.append(subcirc1,[3,1,qreg_0[0],2])
main_circ.u(param_1,0.659000,param_5, 1)
main_circ.u(0,0,-0.264000, 1)
main_circ.append(subcirc1,[3,qreg_0[0],2,0])
main_circ.append(subcirc1,[qreg_0[0],3,0,2])
main_circ.u(param_2,param_3,param_6, 2)
bindings = {param_1: -0.152000, param_2: 0.371000, param_3: 0.592000, param_4: -0.337000, param_5: -0.255000, param_6: 0.459000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
