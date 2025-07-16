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
subcirc0.u(0,0,0.731000, qreg_0[0])
subcirc0.u(0,0,-0.472000, qreg_0[3])
subcirc0.s(qreg_0[3])
subcirc0.s(qreg_0[0])
subcirc0.ry(-0.192000, qreg_0[3])
subcirc0.s(qreg_0[1])

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

main_circ.append(subcirc0,[1,2,0,3])
main_circ.u(param_2,param_1,param_2, 3)
main_circ.ry(0.470000, qreg_0[0])
main_circ.ry(param_3, qreg_0[0])
main_circ.ry(-0.212000, qreg_0[0])
main_circ.s(3)
main_circ.append(subcirc0,[qreg_0[0],0,3,2])
main_circ.s(2)
main_circ.s(1)
main_circ.cz(1,qreg_0[0])
main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(param_5,param_2,0.587000, 3)
main_circ.ry(param_2, 0)
main_circ.cz(2,0)
main_circ.cz(0,1)
main_circ.cz(0,1)
main_circ.cz(0,1)
main_circ.cz(3,qreg_0[0])
main_circ.cz(qreg_0[0],1)
main_circ.cz(2,1)
main_circ.cz(qreg_0[0],2)
main_circ.cz(1,3)
main_circ.cz(2,0)
main_circ.cz(3,0)
main_circ.cz(3,qreg_0[0])
bindings = {param_1: -0.107000, param_2: -0.721000, param_3: -0.779000, param_5: 0.527000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
