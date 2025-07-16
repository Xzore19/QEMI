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
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,0.145000,-0.294000, qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0.u(pi/2,-0.532000,-0.137000, qreg_0[2])
subcirc0.z(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(1)
main_circ.u(param_2,param_0,param_1, 0)
main_circ.u(pi/2,param_2,param_0, 2)
main_circ.cz(1,3)
main_circ.u(param_2,-0.489000,-0.015000, 3)
main_circ.append(subcirc0,[2,3,1,0])
main_circ.z(3)
main_circ.z(3)
main_circ.u(param_2,param_2,-0.696000, 1)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.cz(1,0)
main_circ.y(2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc0,[2,0,1,3])
main_circ.z(2)
main_circ.z(1)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.y(3)
main_circ.cz(1,0)
main_circ.cz(0,3)
main_circ.cz(2,0)
main_circ.cz(1,2)
main_circ.cz(0,1)
main_circ.cz(0,1)
main_circ.cz(2,3)
main_circ.cz(1,3)
main_circ.cz(2,3)
main_circ.cz(3,2)
main_circ.cz(2,1)
main_circ.cz(2,1)
main_circ.cz(0,3)
main_circ.cz(3,1)
main_circ.u(param_1,param_1,param_2, 0)
main_circ.z(3)
bindings = {param_0: -0.248000, param_1: -0.551000, param_2: 0.865000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
