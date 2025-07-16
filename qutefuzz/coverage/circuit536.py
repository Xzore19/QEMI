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
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.u(pi/2,0.680000,-0.095000, qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_2[0],1,qreg_0[0],0])
main_circ.s(qreg_2[1])
main_circ.x(1)
main_circ.z(qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.z(0)
main_circ.z(qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_2[1],0,1,qreg_2[0]])
main_circ.append(subcirc0,[qreg_2[0],0,qreg_0[0],qreg_0[1]])
main_circ.s(qreg_2[0])
main_circ.u(pi/2,param_0,0.795000, 1)
main_circ.z(qreg_2[1])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.s(0)
main_circ.u(pi/2,param_0,param_0, qreg_0[1])
main_circ.u(pi/2,param_0,-0.540000, qreg_2[0])
main_circ.s(0)
main_circ.append(subcirc0,[1,qreg_0[1],0,qreg_2[1]])
main_circ.u(param_0,param_0,param_0, qreg_2[1])
main_circ.append(subcirc0,[1,qreg_2[1],0,qreg_0[1]])
main_circ.x(qreg_2[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],0])
main_circ.z(qreg_2[1])
main_circ.s(0)
main_circ.u(param_0,param_0,param_0, qreg_0[1])
bindings = {param_0: 0.855000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
