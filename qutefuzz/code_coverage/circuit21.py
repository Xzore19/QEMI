from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.cz(qreg_1[0],qreg_0[0])
subcirc0.u(0,0,0.915000, qreg_1[1])
subcirc0.u(0,0,0.337000, qreg_0[0])
subcirc0.h(qreg_1[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.cz(qreg_0[0],0)
main_circ.h(0)
main_circ.u(param_1,param_2,0.762000, 0)
main_circ.u(0,param_2,-0.491000, qreg_0[2])
main_circ.u(0,param_2,-0.170000, qreg_0[3])
main_circ.h(0)
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],1,0])
main_circ.cz(qreg_0[2],1)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.u(param_1,param_2,param_2, qreg_0[2])
main_circ.cz(1,qreg_0[3])
main_circ.h(qreg_0[3])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cy(qreg_0[1],0)
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.h(qreg_0[1])
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[0],0)
main_circ.u(0,param_1,param_0, qreg_0[1])
main_circ.h(1)
main_circ.u(0,0,-0.801000, qreg_0[2])
main_circ.u(param_2,param_2,param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.cz(0,qreg_0[1])
main_circ.h(1)
main_circ.h(qreg_0[3])
main_circ.cz(1,qreg_0[0])
main_circ.cz(0,qreg_0[0])
main_circ.cz(1,qreg_0[1])
main_circ.u(param_1,param_0,-0.986000, qreg_0[3])
main_circ.h(qreg_0[3])
main_circ.cz(1,qreg_0[3])
main_circ.u(param_2,0,-0.763000, qreg_0[1])
main_circ.h(qreg_0[2])
main_circ.cy(0,qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],1,0,qreg_0[0]])
main_circ.h(qreg_0[1])
main_circ.cz(qreg_0[2],0)
main_circ.h(qreg_0[2])
main_circ.h(1)
bindings = {param_0: 0.554000, param_1: -0.771000, param_2: -0.152000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
