from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_3[0])
subcirc0.x(qreg_2[0])
subcirc0.u(pi/2,-0.877000,0.356000, qreg_3[0])
subcirc0.u(pi/2,-0.576000,-0.695000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.395000, qreg_0[2])
subcirc2.u(pi/2,-0.632000,-0.860000, qreg_0[0])
subcirc2.rx(-0.010000, qreg_0[1])
subcirc2.u(pi/2,0.009000,-0.381000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_3[0])
subcirc3.rx(0.957000, qreg_2[0])
subcirc3.x(qreg_0[0])
subcirc3.x(qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_0[1])
subcirc4.h(qreg_0[2])
subcirc4.x(qreg_0[1])
subcirc4.h(qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc3,[1,qreg_1[2],qreg_0[0],0])
main_circ.append(subcirc4,[qreg_1[2],qreg_1[0],1,qreg_1[1]])
main_circ.append(subcirc2,[qreg_1[2],qreg_0[0],qreg_1[1],qreg_1[0],1])
main_circ.append(subcirc2,[qreg_1[1],qreg_1[0],qreg_0[0],qreg_1[2],1])
main_circ.rx(-0.957000, qreg_1[2])
main_circ.h(qreg_1[2])
main_circ.rx(param_2, 0)
main_circ.append(subcirc4,[qreg_1[2],1,qreg_1[1],0])
main_circ.append(subcirc4,[qreg_1[2],qreg_1[0],qreg_0[0],1])
main_circ.u(pi/2,0.004000,param_0, qreg_1[0])
main_circ.append(subcirc3,[1,qreg_0[0],qreg_1[1],qreg_1[0]])
main_circ.h(qreg_1[2])
main_circ.x(qreg_1[0])
main_circ.append(subcirc3,[0,1,qreg_0[0],qreg_1[0]])
main_circ.rx(param_1, qreg_1[0])
main_circ.h(qreg_0[0])
main_circ.rx(param_1, qreg_1[0])
main_circ.append(subcirc4,[qreg_0[0],0,1,qreg_1[2]])
main_circ.append(subcirc3,[qreg_1[1],qreg_1[0],qreg_1[2],qreg_0[0]])
bindings = {param_0: -0.171000, param_1: 0.679000, param_2: 0.485000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
