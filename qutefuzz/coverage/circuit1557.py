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
subcirc0.u(0,0,0.462000, qreg_0[0])
subcirc0.u(0,0,-0.734000, qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.x(qreg_0[1])

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

main_circ.u(pi/2,param_1,0.757000, qreg_0[0])
main_circ.append(subcirc0,[3,0,2,1])
main_circ.u(0,param_0,0.027000, 1)
main_circ.append(subcirc0,[qreg_0[0],1,0,qreg_0[1]])
main_circ.rz(param_1, 2)
main_circ.u(pi/2,param_1,0.532000, 1)
main_circ.x(2)
main_circ.u(pi/2,-0.902000,param_1, 3)
main_circ.u(0,param_1,param_0, 3)
main_circ.x(2)
main_circ.u(pi/2,-0.147000,param_1, 1)
main_circ.append(subcirc0,[2,qreg_0[1],3,qreg_0[0]])
main_circ.x(0)
main_circ.x(1)
main_circ.x(qreg_0[0])
main_circ.rz(-0.242000, qreg_0[1])
main_circ.x(2)
main_circ.u(0,param_1,0.378000, 2)
main_circ.rz(param_0, 2)
main_circ.u(param_0,0,param_0, 0)
main_circ.x(0)
main_circ.u(param_0,0,param_0, qreg_0[0])
main_circ.x(1)
main_circ.u(param_1,0,-0.380000, 1)
main_circ.append(subcirc0,[qreg_0[0],2,0,1])
main_circ.x(2)
main_circ.u(param_0,param_0,-0.752000, 2)
main_circ.append(subcirc0,[qreg_0[0],1,0,qreg_0[1]])
main_circ.rz(0.502000, 1)
main_circ.u(param_0,param_0,0.122000, 0)
main_circ.x(0)
main_circ.rz(param_0, 1)
main_circ.rz(0.917000, 3)
main_circ.u(param_0,param_0,-0.977000, 2)
main_circ.x(0)
main_circ.u(param_1,param_1,0.468000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],0,1,2])
main_circ.rz(0.622000, 0)
main_circ.u(param_0,0.813000,param_1, qreg_0[1])
main_circ.x(qreg_0[0])
bindings = {param_0: -0.726000, param_1: -0.502000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
