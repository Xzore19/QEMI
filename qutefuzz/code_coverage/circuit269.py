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
subcirc0.ry(-0.097000, qreg_0[0])
subcirc0.u(0.047000,0.058000,0.700000, qreg_0[0])
subcirc0.y(qreg_0[3])
subcirc0.ry(-0.493000, qreg_0[2])
subcirc0.y(qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.ry(param_3, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.u(param_0,param_0,param_1, qreg_0[0])
main_circ.u(0.177000,param_1,-0.692000, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.y(qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.y(qreg_0[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.u(param_1,-0.849000,param_1, qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.y(qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.ry(0.923000, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.y(qreg_0[2])
main_circ.ry(0.977000, qreg_0[1])
main_circ.u(param_2,0.385000,param_3, qreg_0[0])
main_circ.y(qreg_0[2])
bindings = {param_0: -0.204000, param_1: 0.860000, param_2: 0.473000, param_3: 0.836000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
