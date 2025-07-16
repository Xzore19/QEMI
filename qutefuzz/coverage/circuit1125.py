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
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.h(qreg_0[0])
subcirc0.rx(0.990000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.476000, qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1.rx(-0.738000, qreg_0[2])
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.s(qreg_1[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_1[2],qreg_1[1]])
main_circ.cx(qreg_0[0],qreg_1[2])
main_circ.h(qreg_1[2])
main_circ.rx(-0.175000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
main_circ.s(qreg_1[2])
main_circ.h(qreg_1[2])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_1[2],qreg_0[0]])
main_circ.s(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.s(qreg_0[0])
main_circ.s(qreg_1[2])
main_circ.s(qreg_1[0])
main_circ.rx(param_0, qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
main_circ.h(qreg_0[0])
bindings = {param_0: 0.975000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1125")
