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
subcirc0.u(pi/2,0.719000,-0.857000, qreg_0[0])
subcirc0.rz(0.721000, qreg_0[0])
subcirc0.u(0,0,0.539000, qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.u(pi/2,0.861000,0.203000, qreg_0[2])
subcirc0.rz(-0.756000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.628000, qreg_2[1])
subcirc1.u(0,0,-0.764000, qreg_0[1])
subcirc1.rz(0.621000, qreg_0[0])
subcirc1.u(0,0,-0.793000, qreg_0[0])
subcirc1.u(0,0,0.164000, qreg_0[1])
subcirc1.rz(0.619000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[1,3,2,0])
main_circ.append(subcirc0,[0,3,2,1])
main_circ.u(param_0,0,0.411000, 1)
main_circ.u(0,0,0.466000, 0)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.append(subcirc0,[2,1,0,3])
main_circ.u(param_0,0,param_0, 2)
main_circ.rz(-0.467000, 2)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.u(param_0,0,-0.994000, 2)
main_circ.h(0)
main_circ.u(param_0,0.718000,param_0, 2)
main_circ.rz(0.751000, 3)
main_circ.u(param_0,0,param_0, 0)
main_circ.append(subcirc0,[2,1,0,3])
main_circ.h(0)
main_circ.h(0)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.u(param_0,param_0,0.418000, 2)
main_circ.rz(param_0, 0)
bindings = {param_0: -0.586000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
