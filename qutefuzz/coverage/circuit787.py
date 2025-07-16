from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.rz(0.741000, qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.rz(0.710000, qreg_0[0])
subcirc0.rz(-0.033000, qreg_1[1])
subcirc0.rx(-0.733000, qreg_1[1])

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.x(qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.rz(0.059000, qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.x(qreg_0[2])
main_circ.rz(0.842000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.rx(param_4, qreg_0[1])
main_circ.rz(-0.785000, qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.rz(-0.046000, qreg_0[1])
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.rx(0.026000, qreg_0[0])
main_circ.rz(0.492000, qreg_0[2])
main_circ.rz(param_0, qreg_3[0])
bindings = {param_0: 0.395000, param_4: -0.109000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "787")
