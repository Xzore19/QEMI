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
subcirc0.rx(0.154000, qreg_0[1])
subcirc0.u(-0.959000,0.564000,0.889000, qreg_0[0])
subcirc0.u(0.314000,-0.177000,0.682000, qreg_0[0])
subcirc0.ry(0.614000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.ry(-0.737000, qreg_0[0])
subcirc1.u(-0.520000,-0.057000,0.778000, qreg_2[1])
subcirc1.ry(-0.580000, qreg_2[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rx(0.923000, qreg_0[1])
main_circ.u(param_1,-0.246000,0.179000, qreg_3[0])
main_circ.rx(-0.897000, qreg_3[0])
main_circ.rx(param_1, qreg_0[1])
main_circ.rx(param_0, qreg_3[0])
main_circ.ry(-0.589000, qreg_2[0])
main_circ.u(param_1,param_0,-0.651000, 1)
main_circ.ry(param_1, qreg_3[0])
main_circ.u(0.066000,0.836000,-0.108000, qreg_3[0])
main_circ.ry(param_2, qreg_0[1])
main_circ.cz(qreg_0[0],1)
main_circ.rx(param_0, qreg_2[0])
main_circ.rx(param_1, qreg_0[0])
main_circ.ry(0.525000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],0,1,qreg_2[0]])
main_circ.ry(param_1, 0)
main_circ.rx(-0.615000, qreg_2[0])
main_circ.ry(0.860000, 1)
main_circ.u(-0.805000,-0.075000,-0.617000, qreg_0[1])
main_circ.append(subcirc1,[qreg_3[0],1,qreg_0[1],qreg_0[0]])
main_circ.rx(-0.048000, qreg_0[0])
main_circ.append(subcirc0,[1,qreg_3[0],0,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],1,qreg_2[0]])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(0,1)
main_circ.cz(qreg_2[0],0)
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_3[0],0)
main_circ.cz(qreg_3[0],1)
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_3[0],1)
bindings = {param_0: 0.657000, param_1: -0.166000, param_2: 0.577000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
