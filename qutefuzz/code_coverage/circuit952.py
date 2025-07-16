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
subcirc0.ry(0.779000, qreg_0[2])
subcirc0.u(pi/2,0.077000,-0.596000, qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.ry(-0.364000, qreg_0[3])
subcirc0.u(pi/2,0.629000,-0.399000, qreg_0[2])
subcirc0.ry(-0.204000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.cz(0,2)
main_circ.u(pi/2,param_4,param_3, 0)
main_circ.u(param_0,-0.241000,param_4, 0)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.append(subcirc0,[3,1,2,0])
main_circ.append(subcirc0,[2,3,0,1])
main_circ.ry(param_3, 3)
main_circ.cz(3,1)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.h(0)
main_circ.u(param_3,-0.071000,param_3, 2)
main_circ.cz(1,0)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.cz(1,3)
main_circ.cz(0,1)
main_circ.cz(3,0)
main_circ.cz(3,2)
main_circ.cz(3,0)
main_circ.cz(0,2)
main_circ.u(param_5,0.685000,param_2, 1)
main_circ.ry(0.758000, 1)
main_circ.cz(2,3)
main_circ.u(param_5,param_0,param_4, 0)
main_circ.h(3)
bindings = {param_0: -0.196000, param_2: -0.757000, param_3: 0.804000, param_4: -0.084000, param_5: 0.534000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
