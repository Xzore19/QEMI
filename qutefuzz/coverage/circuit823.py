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
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(pi/2,param_0,0.347000, qreg_0[0])
main_circ.cz(qreg_0[0],2)
main_circ.cz(qreg_0[0],2)
main_circ.h(2)
main_circ.h(2)
main_circ.h(1)
main_circ.h(0)
main_circ.h(0)
main_circ.cz(3,qreg_0[0])
main_circ.append(subcirc1,[3,0,qreg_0[0],2])
main_circ.append(subcirc1,[1,2,3,qreg_0[0]])
main_circ.h(0)
main_circ.h(1)
main_circ.u(param_3,param_2,param_0, qreg_0[0])
main_circ.u(pi/2,param_1,0.438000, 0)
main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[3,2,0,1])
main_circ.h(qreg_0[0])
main_circ.cy(0,1)
main_circ.cz(0,3)
main_circ.u(param_3,param_1,param_3, qreg_0[0])
main_circ.append(subcirc1,[0,2,qreg_0[0],1])
main_circ.cz(2,3)
main_circ.cy(1,2)
main_circ.h(1)
main_circ.cy(0,1)
main_circ.cz(1,2)
main_circ.cz(2,0)
main_circ.cy(3,0)
main_circ.cy(3,1)
main_circ.u(pi/2,param_0,param_3, 0)
main_circ.cy(0,1)
main_circ.u(pi/2,param_0,0.877000, 0)
main_circ.cy(0,qreg_0[0])
main_circ.cz(3,2)
main_circ.u(param_0,-0.137000,-0.324000, 3)
main_circ.append(subcirc1,[qreg_0[0],0,2,3])
main_circ.cy(qreg_0[0],2)
main_circ.u(param_3,0.152000,-0.778000, 2)
bindings = {param_0: -0.250000, param_1: 0.946000, param_2: 0.069000, param_3: 0.956000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
