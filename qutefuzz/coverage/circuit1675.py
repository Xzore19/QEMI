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
subcirc0.x(qreg_3[0])
subcirc0.u(0,0,0.912000, qreg_0[1])
subcirc0.u(pi/2,0.957000,0.946000, qreg_0[0])
subcirc0.rz(0.729000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.u(0,0,-0.890000, qreg_0[0])
subcirc1.x(qreg_2[0])
subcirc1.rz(-0.797000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.675000, qreg_0[0])
subcirc2.u(pi/2,0.157000,-0.850000, qreg_3[0])
subcirc2.x(qreg_3[0])
subcirc2.u(0,0,-0.636000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0,0,0.022000, qreg_0[2])
subcirc3.u(pi/2,0.919000,0.390000, qreg_0[2])
subcirc3.u(pi/2,0.604000,0.026000, qreg_0[0])
subcirc3.x(qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.970000, qreg_0[2])
subcirc4.u(0,0,0.633000, qreg_0[2])
subcirc4.x(qreg_0[2])
subcirc4.u(0,0,0.056000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.u(param_3,0,param_2, qreg_1[0])
main_circ.rz(param_1, qreg_0[0])
main_circ.append(subcirc4,[2,0,qreg_1[0],3,qreg_0[0],1])
main_circ.append(subcirc3,[3,0,qreg_1[0],1])
main_circ.rz(-0.528000, 0)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.append(subcirc3,[1,qreg_0[0],qreg_1[0],0])
main_circ.append(subcirc4,[2,qreg_1[0],0,qreg_0[0],1,3])
main_circ.rz(param_0, 0)
main_circ.rz(param_2, qreg_1[0])
main_circ.append(subcirc3,[1,3,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc3,[1,2,0,qreg_1[0]])
main_circ.u(param_3,0,-0.968000, 3)
main_circ.append(subcirc0,[2,3,0,1,qreg_0[0]])
main_circ.append(subcirc1,[1,qreg_0[0],0,3,qreg_1[0],2])
main_circ.rz(param_2, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],3,qreg_1[0],2,1])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],3,1])
main_circ.append(subcirc0,[3,qreg_0[0],0,1,2])
main_circ.x(qreg_0[0])
main_circ.u(param_3,0.486000,param_1, 0)
main_circ.u(0,0,param_1, 0)
main_circ.x(0)
main_circ.u(0,0,0.272000, 1)
bindings = {param_0: 0.066000, param_1: 0.519000, param_2: -0.247000, param_3: -0.155000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
