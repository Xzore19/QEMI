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
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.u(0,0,-0.175000, qreg_0[1])
subcirc0.ry(-0.729000, qreg_0[0])
subcirc0.ry(-0.860000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_3[0])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.u(0,0,0.324000, qreg_3[0])
subcirc1.u(0,0,0.396000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.351000, qreg_0[2])
subcirc2.u(0,0,-0.383000, qreg_0[2])
subcirc2.cx(qreg_0[0],qreg_0[1])
subcirc2.u(0,0,-0.683000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.270000, qreg_2[0])
subcirc3.ry(0.804000, qreg_2[0])
subcirc3.u(0,0,-0.281000, qreg_3[0])
subcirc3.ry(0.319000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.216000,-0.496000, qreg_0[1])
subcirc4.u(pi/2,0.125000,-0.528000, qreg_2[0])
subcirc4.u(0,0,0.030000, qreg_2[0])
subcirc4.u(0,0,0.295000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.cx(3,1)
main_circ.append(subcirc4,[qreg_0[1],qreg_0[0],0,2])
main_circ.u(param_4,param_3,param_4, qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.append(subcirc2,[0,2,1,qreg_0[1]])
main_circ.append(subcirc2,[0,qreg_0[1],1,qreg_0[0]])
main_circ.append(subcirc4,[1,qreg_0[1],qreg_0[0],3])
main_circ.ry(param_2, 0)
main_circ.cx(0,3)
main_circ.ry(-0.790000, qreg_0[0])
main_circ.u(0,0,0.500000, 2)
main_circ.u(param_1,0,-0.451000, 1)
main_circ.append(subcirc2,[3,0,qreg_0[1],1])
main_circ.append(subcirc1,[qreg_0[0],2,qreg_0[1],0])
main_circ.cx(2,0)
main_circ.u(param_4,-0.988000,param_0, qreg_0[0])
main_circ.ry(-0.212000, qreg_0[1])
main_circ.append(subcirc0,[0,2,qreg_0[1],1])
main_circ.u(param_3,0,0.949000, 1)
main_circ.cx(2,1)
main_circ.cx(0,qreg_0[0])
main_circ.cx(2,1)
main_circ.cx(3,qreg_0[1])
main_circ.cx(qreg_0[1],1)
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(1,qreg_0[1])
main_circ.append(subcirc4,[qreg_0[0],1,0,2])
main_circ.u(0,0,param_4, 2)
main_circ.u(0,0,-0.017000, qreg_0[1])
main_circ.ry(param_2, 2)
main_circ.ry(0.198000, 1)
main_circ.ry(-0.460000, 2)
main_circ.ry(param_2, qreg_0[1])
bindings = {param_0: -0.468000, param_1: 0.344000, param_2: 0.723000, param_3: -0.981000, param_4: -0.189000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
