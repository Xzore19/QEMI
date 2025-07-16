from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(-0.387000, qreg_2[0])
subcirc0.u(0,0,-0.733000, qreg_0[0])
subcirc0.x(qreg_2[0])
subcirc0.u(0,0,-0.759000, qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.rx(-0.061000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(param_3,param_1,0.227000, 1)
main_circ.rx(-0.297000, 1)
main_circ.append(subcirc0,[qreg_0[0],1,3,2])
main_circ.y(0)
main_circ.append(subcirc0,[2,3,0,qreg_0[0]])
main_circ.y(3)
main_circ.u(0,0,param_4, 2)
main_circ.y(3)
main_circ.u(0,0,0.375000, 1)
main_circ.u(0,0,-0.063000, qreg_0[0])
main_circ.append(subcirc0,[1,0,2,qreg_0[0]])
main_circ.append(subcirc0,[2,0,3,qreg_0[0]])
main_circ.rx(param_2, 3)
main_circ.x(3)
main_circ.rx(-0.079000, 1)
main_circ.u(0,0,-0.318000, 0)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.y(2)
main_circ.rx(param_2, 1)
main_circ.u(param_5,param_1,param_1, 0)
main_circ.u(param_3,0,param_3, 2)
main_circ.y(qreg_0[0])
main_circ.y(0)
bindings = {param_1: -0.106000, param_2: 0.818000, param_3: 0.776000, param_4: 0.925000, param_5: 0.611000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
