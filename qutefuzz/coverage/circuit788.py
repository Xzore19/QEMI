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
subcirc0.u(-0.941000,0.923000,-0.649000, qreg_1[1])
subcirc0.cz(qreg_1[1],qreg_1[2])
subcirc0.cz(qreg_1[2],qreg_1[0])
subcirc0.u(0.076000,-0.720000,-0.923000, qreg_1[1])
subcirc0.s(qreg_1[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.x(qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.u(0.908000,-0.899000,0.283000, qreg_0[1])
subcirc1.u(-0.537000,-0.995000,-0.357000, qreg_2[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],1,0,qreg_2[1],qreg_0[0]])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.append(subcirc0,[1,qreg_0[1],0,qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_2[1],0,qreg_2[0],qreg_0[0],1,qreg_0[1]])
main_circ.u(param_5,param_0,-0.572000, 0)
main_circ.append(subcirc1,[1,qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.u(0.998000,param_3,param_5, 0)
main_circ.x(1)
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.s(qreg_2[0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0],0,1])
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.x(1)
main_circ.u(param_5,-0.054000,param_2, 0)
main_circ.x(qreg_0[0])
main_circ.cz(0,1)
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],0])
main_circ.s(qreg_0[1])
main_circ.append(subcirc1,[0,qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.u(-0.956000,param_3,param_3, qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[0])
bindings = {param_0: 0.423000, param_2: 0.456000, param_3: 0.504000, param_5: -0.261000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
