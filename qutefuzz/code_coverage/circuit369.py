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
subcirc0.h(qreg_0[0])
subcirc0.ry(0.393000, qreg_0[1])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.h(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.h(qreg_1[2])
subcirc1.ry(0.478000, qreg_1[0])
subcirc1.h(qreg_1[0])
subcirc1.ry(-0.096000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.ry(-0.962000, 0)
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.ry(-0.712000, qreg_2[0])
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.s(qreg_3[0])
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.h(0)
main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_2[0]])
main_circ.h(qreg_3[0])
main_circ.h(qreg_0[1])
main_circ.ry(param_3, qreg_3[0])
main_circ.s(0)
main_circ.s(0)
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.s(qreg_2[0])
main_circ.ry(-0.105000, qreg_0[0])
main_circ.s(0)
main_circ.h(qreg_3[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],0,qreg_3[0]])
main_circ.s(qreg_3[0])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.ry(param_4, 0)
main_circ.ry(param_1, 0)
main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_3[0],qreg_2[0])
main_circ.cx(0,qreg_2[0])
main_circ.cx(qreg_3[0],qreg_2[0])
main_circ.cx(qreg_2[0],0)
main_circ.h(qreg_2[0])
main_circ.cx(0,qreg_0[1])
main_circ.ry(0.600000, qreg_2[0])
main_circ.ry(0.519000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],0])
bindings = {param_1: 0.843000, param_3: -0.438000, param_4: -0.733000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "369")
