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
subcirc0.y(qreg_0[3])
subcirc0.ry(0.363000, qreg_0[2])
subcirc0.ry(-0.121000, qreg_0[2])
subcirc0.ry(-0.856000, qreg_0[1])
subcirc0.ry(-0.368000, qreg_0[3])
subcirc0.ry(-0.511000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.067000, qreg_3[0])
subcirc1.u(0,0,-0.238000, qreg_3[0])
subcirc1.u(0,0,-0.587000, qreg_0[2])
subcirc1.y(qreg_0[0])
subcirc1.ry(0.601000, qreg_3[0])
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.cz(0,2)
main_circ.cz(3,0)
main_circ.cz(qreg_0[0],0)
main_circ.y(2)
main_circ.append(subcirc1,[2,3,1,qreg_0[0]])
main_circ.y(3)
main_circ.u(param_2,param_0,param_1, qreg_0[0])
main_circ.y(1)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.cz(0,2)
main_circ.append(subcirc1,[3,qreg_0[0],1,0])
main_circ.append(subcirc1,[qreg_0[0],1,2,0])
main_circ.y(3)
main_circ.cz(qreg_0[0],0)
main_circ.cz(1,2)
main_circ.cz(2,0)
main_circ.cz(1,2)
main_circ.cz(qreg_0[0],0)
main_circ.cz(0,3)
main_circ.append(subcirc1,[3,2,0,1])
main_circ.y(0)
bindings = {param_0: -0.327000, param_1: 0.787000, param_2: 0.707000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
