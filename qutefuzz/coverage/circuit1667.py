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
subcirc0.u(0,0,-0.873000, qreg_0[1])
subcirc0.u(0,0,-0.018000, qreg_0[2])
subcirc0.rz(-0.228000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.y(qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.y(qreg_0[0])
subcirc1.rz(-0.438000, qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],0,qreg_0[2]])
main_circ.rz(0.011000, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.u(param_1,0,param_1, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_0[1],0])
main_circ.u(param_1,param_1,-0.044000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.rz(-0.707000, qreg_0[2])
main_circ.rz(param_0, qreg_3[0])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_3[0],0)
main_circ.rz(-0.034000, 0)
main_circ.append(subcirc1,[0,qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[2],0,qreg_3[0],qreg_0[0]])
main_circ.cx(qreg_3[0],0)
main_circ.y(0)
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.rz(0.501000, qreg_0[2])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.rz(-0.137000, qreg_0[0])
main_circ.cx(0,qreg_3[0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.u(0,0,0.813000, qreg_0[1])
bindings = {param_0: -0.492000, param_1: 0.441000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
