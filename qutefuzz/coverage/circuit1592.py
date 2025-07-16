from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,-0.606000,0.449000, qreg_2[1])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.u(pi/2,-0.841000,-0.018000, qreg_0[0])
subcirc0.y(qreg_2[0])

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

main_circ.append(subcirc0,[1,3,0,2])
main_circ.cz(2,0)
main_circ.cz(2,0)
main_circ.u(param_3,param_4,param_0, 0)
main_circ.y(0)
main_circ.cz(1,0)
main_circ.y(2)
main_circ.y(2)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.cz(3,2)
main_circ.s(2)
main_circ.s(2)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.y(3)
main_circ.cz(0,3)
main_circ.s(1)
main_circ.y(0)
main_circ.y(3)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.u(pi/2,0.502000,-0.787000, 2)
main_circ.y(1)
main_circ.y(2)
main_circ.cz(3,1)
main_circ.u(param_0,param_0,param_4, 3)
main_circ.cz(1,0)
main_circ.cz(3,1)
main_circ.cz(2,3)
main_circ.s(3)
main_circ.u(param_1,param_5,param_2, 1)
main_circ.u(pi/2,param_3,0.154000, 2)
main_circ.s(2)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.y(2)
main_circ.y(3)
main_circ.s(1)
main_circ.cz(3,1)
main_circ.u(pi/2,-0.496000,param_2, 3)
main_circ.y(3)
bindings = {param_0: 0.762000, param_1: -0.707000, param_2: -0.133000, param_3: 0.073000, param_4: -0.442000, param_5: 0.878000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
