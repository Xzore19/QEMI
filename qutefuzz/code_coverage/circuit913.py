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
subcirc0.ry(0.108000, qreg_0[2])
subcirc0.u(0,0,-0.206000, qreg_0[0])
subcirc0.u(0,0,0.410000, qreg_0[0])
subcirc0.ry(0.388000, qreg_0[0])
subcirc0.u(0,0,-0.278000, qreg_3[0])
subcirc0.ry(-0.077000, qreg_0[2])

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

main_circ.y(qreg_2[0])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.u(0,param_1,-0.301000, qreg_2[0])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.ry(param_1, qreg_0[0])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[0],0)
main_circ.y(1)
main_circ.u(0,0,param_1, 1)
main_circ.y(1)
main_circ.y(qreg_0[1])
main_circ.ry(param_0, qreg_2[1])
main_circ.ry(0.627000, 1)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],1,qreg_0[1]])
main_circ.ry(0.157000, qreg_0[0])
main_circ.ry(0.211000, qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],0])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[1],0,1])
main_circ.y(qreg_2[1])
main_circ.cz(1,0)
main_circ.y(qreg_0[1])
main_circ.cz(qreg_2[1],qreg_0[1])
main_circ.cz(1,0)
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_2[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.cz(qreg_2[1],0)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_2[0],1)
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[1],0)
main_circ.ry(0.704000, qreg_2[1])
main_circ.ry(param_0, qreg_0[1])
main_circ.u(param_0,param_1,-0.809000, qreg_2[1])
main_circ.u(param_1,0,-0.787000, 1)
main_circ.y(qreg_2[1])
bindings = {param_0: 0.195000, param_1: 0.639000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
