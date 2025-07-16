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
subcirc0.s(qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.h(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_2[1])
subcirc1.u(0,0,0.822000, qreg_0[0])
subcirc1.u(0,0,0.870000, qreg_2[0])
subcirc1.u(0,0,-0.506000, qreg_2[0])
subcirc1.u(0,0,0.768000, qreg_0[0])
subcirc1.u(0,0,-0.260000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.append(subcirc0,[qreg_0[1],0,qreg_2[0],1])
main_circ.cx(qreg_2[0],0)
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],0,qreg_2[1],qreg_2[0]])
main_circ.cx(0,1)
main_circ.cx(qreg_2[1],qreg_2[0])
main_circ.u(0,0,0.849000, qreg_2[0])
main_circ.append(subcirc1,[qreg_0[0],1,0,qreg_2[1],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_2[1],1,0])
main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_2[1],qreg_0[1]])
main_circ.append(subcirc0,[qreg_2[0],1,0,qreg_0[0]])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_2[1],qreg_0[1],1])
main_circ.cx(1,0)
main_circ.cx(qreg_2[0],qreg_0[0])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.cx(qreg_0[0],1)
main_circ.cx(1,qreg_2[0])
main_circ.cx(0,qreg_0[1])
main_circ.cx(1,0)
main_circ.cx(qreg_2[1],qreg_0[0])
main_circ.cx(0,1)
main_circ.cx(0,qreg_2[0])
main_circ.s(qreg_2[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
