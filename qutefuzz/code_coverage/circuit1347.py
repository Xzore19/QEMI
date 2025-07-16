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
subcirc0.u(0,0,-0.147000, qreg_0[2])
subcirc0.x(qreg_3[0])
subcirc0.rz(0.601000, qreg_3[0])
subcirc0.x(qreg_0[2])
subcirc0.rx(-0.061000, qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.rz(0.573000, 1)
main_circ.x(0)
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],1,qreg_1[0]])
main_circ.rz(0.543000, 0)
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],0,qreg_1[0]])
main_circ.rx(param_1, 1)
main_circ.append(subcirc0,[0,qreg_2[1],qreg_1[0],qreg_2[0]])
main_circ.u(0,param_0,param_1, qreg_1[0])
main_circ.rx(-0.104000, 1)
main_circ.rz(param_0, qreg_0[0])
main_circ.x(qreg_2[1])
main_circ.u(0,0,-0.942000, qreg_1[0])
main_circ.rx(0.377000, 1)
main_circ.u(0,param_1,-0.012000, qreg_2[1])
main_circ.rx(param_1, qreg_0[0])
main_circ.u(0,0,0.434000, qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],1,qreg_2[0],0])
main_circ.u(0,param_1,param_1, qreg_1[0])
main_circ.x(0)
main_circ.rx(0.289000, qreg_2[0])
main_circ.x(qreg_2[0])
main_circ.rx(param_1, qreg_1[0])
main_circ.rz(-0.220000, 0)
main_circ.u(param_0,param_1,-0.537000, qreg_2[1])
main_circ.u(param_0,param_0,param_1, 0)
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],1,qreg_2[0]])
main_circ.rz(0.907000, 1)
main_circ.x(1)
main_circ.rx(param_1, 1)
main_circ.rz(param_1, qreg_2[0])
bindings = {param_0: -0.563000, param_1: -0.785000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
