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
subcirc0.u(pi/2,0.621000,-0.411000, qreg_0[2])
subcirc0.cy(qreg_0[0],qreg_0[3])
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_0[2])
subcirc0.u(pi/2,-0.510000,-0.564000, qreg_0[1])

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

main_circ.u(param_2,0.212000,0.266000, 0)
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,2])
main_circ.cy(2,qreg_0[0])
main_circ.u(param_2,-0.265000,0.164000, 1)
main_circ.cx(qreg_0[1],1)
main_circ.cy(qreg_0[1],2)
main_circ.append(subcirc0,[3,1,qreg_0[1],qreg_0[0]])
main_circ.u(pi/2,param_3,param_3, 2)
main_circ.append(subcirc0,[0,1,qreg_0[1],2])
main_circ.cy(3,1)
main_circ.append(subcirc0,[2,3,qreg_0[0],qreg_0[1]])
main_circ.u(param_2,param_0,param_4, 2)
main_circ.h(0)
main_circ.h(qreg_0[1])
main_circ.h(0)
main_circ.cx(qreg_0[1],1)
main_circ.cy(qreg_0[0],1)
main_circ.u(param_1,param_1,param_0, 2)
main_circ.u(pi/2,-0.375000,-0.447000, qreg_0[0])
main_circ.u(param_4,param_3,param_4, qreg_0[1])
main_circ.cx(2,qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.cy(qreg_0[1],1)
main_circ.cx(1,2)
main_circ.cx(1,qreg_0[1])
main_circ.cx(1,3)
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_0[0],2)
main_circ.cy(qreg_0[1],2)
main_circ.h(2)
main_circ.cy(2,3)
main_circ.append(subcirc0,[0,1,qreg_0[0],qreg_0[1]])
main_circ.h(3)
main_circ.h(0)
main_circ.u(pi/2,param_2,-1.000000, 0)
main_circ.cx(3,2)
bindings = {param_0: -0.056000, param_1: -0.647000, param_2: -0.272000, param_3: 0.801000, param_4: -0.733000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
