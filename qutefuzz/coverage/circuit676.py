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
subcirc0.u(pi/2,-0.339000,0.892000, qreg_0[1])
subcirc0.u(pi/2,-0.051000,0.008000, qreg_0[0])
subcirc0.ry(0.554000, qreg_2[1])
subcirc0.cx(qreg_0[1],qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.157000, qreg_0[2])
subcirc1.cx(qreg_0[0],qreg_0[3])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.u(pi/2,0.563000,-0.773000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cx(qreg_0[1],qreg_2[1])
subcirc2.ry(-0.287000, qreg_0[1])
subcirc2.x(qreg_2[1])
subcirc2.cx(qreg_2[1],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.057000,0.495000, qreg_3[0])
subcirc3.u(pi/2,-0.178000,0.281000, qreg_3[0])
subcirc3.ry(0.527000, qreg_0[1])
subcirc3.cx(qreg_0[1],qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.444000,0.602000, qreg_3[0])
subcirc4.u(pi/2,0.430000,0.938000, qreg_3[0])
subcirc4.ry(-0.985000, qreg_3[0])
subcirc4.ry(0.531000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.x(0)
main_circ.append(subcirc4,[1,0,qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.ry(param_3, 1)
main_circ.u(pi/2,param_1,-0.435000, 1)
main_circ.append(subcirc4,[0,1,qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.ry(-0.643000, 0)
main_circ.append(subcirc2,[1,qreg_2[0],qreg_2[1],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],0,1])
main_circ.append(subcirc4,[qreg_2[0],qreg_0[1],0,qreg_2[1],qreg_0[0]])
main_circ.cx(0,1)
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_2[1],1])
main_circ.append(subcirc3,[1,qreg_2[1],qreg_0[0],0])
main_circ.append(subcirc3,[qreg_2[0],1,0,qreg_2[1]])
main_circ.cx(qreg_2[1],0)
main_circ.cx(0,1)
main_circ.cx(0,qreg_2[1])
main_circ.cx(qreg_2[1],1)
main_circ.cx(1,qreg_2[1])
main_circ.cx(qreg_2[1],0)
main_circ.append(subcirc0,[0,qreg_2[0],1,qreg_2[1]])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[1],1,qreg_2[1],0])
main_circ.u(param_0,param_0,param_0, 1)
bindings = {param_0: 0.435000, param_1: 0.418000, param_3: -0.138000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
