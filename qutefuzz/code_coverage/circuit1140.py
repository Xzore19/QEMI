from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.140000, qreg_3[0])
subcirc0.ry(0.927000, qreg_1[1])
subcirc0.cz(qreg_1[0],qreg_1[1])
subcirc0.rz(0.114000, qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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
param_5 = Parameter("param_5")

main_circ.cz(qreg_3[0],qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.x(qreg_1[0])
main_circ.cz(qreg_3[0],qreg_1[1])
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_1[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.rz(param_1, qreg_0[0])
main_circ.rz(param_3, qreg_1[0])
main_circ.cz(qreg_1[1],qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.ry(0.566000, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_3[0]])
main_circ.ry(param_0, qreg_0[0])
main_circ.x(qreg_1[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.rz(0.383000, qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.rz(param_4, qreg_1[0])
main_circ.cz(qreg_1[0],qreg_1[1])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.rz(param_1, qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[1],qreg_0[0],qreg_1[0]])
bindings = {param_0: 0.543000, param_1: 0.130000, param_3: 0.105000, param_4: 0.539000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1140")
