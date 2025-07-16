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
subcirc0.s(qreg_1[0])
subcirc0.rx(-0.236000, qreg_1[0])
subcirc0.rx(0.846000, qreg_1[2])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cx(qreg_1[0],qreg_1[2])
subcirc1.rx(0.840000, qreg_1[1])
subcirc1.rx(0.840000, qreg_0[0])
subcirc1.x(qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.x(qreg_2[0])
subcirc2.cx(qreg_0[1],qreg_2[1])
subcirc2.x(qreg_2[1])
subcirc2.s(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[1],qreg_3[0])
subcirc3.rx(-0.151000, qreg_0[2])
subcirc3.s(qreg_3[0])
subcirc3.rx(0.047000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.x(qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.rx(-0.193000, qreg_2[0])
main_circ.append(subcirc1,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.cx(qreg_0[1],qreg_2[1])
main_circ.x(qreg_2[0])
main_circ.rx(0.643000, qreg_2[0])
main_circ.s(qreg_0[1])
main_circ.s(qreg_0[1])
main_circ.rx(param_1, qreg_0[1])
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.rx(param_4, qreg_0[1])
main_circ.rx(param_1, qreg_0[0])
main_circ.x(qreg_0[1])
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.append(subcirc1,[qreg_2[1],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.cx(qreg_2[1],qreg_0[0])
main_circ.x(qreg_2[1])
main_circ.cx(qreg_0[0],qreg_2[1])
main_circ.x(qreg_2[0])
main_circ.x(qreg_2[1])
main_circ.x(qreg_2[1])
main_circ.rx(0.188000, qreg_0[1])
main_circ.x(qreg_2[0])
main_circ.rx(param_0, qreg_2[0])
main_circ.s(qreg_0[1])
main_circ.append(subcirc1,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.cx(qreg_0[0],qreg_2[1])
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_2[1],qreg_0[0])
main_circ.cx(qreg_0[1],qreg_2[1])
main_circ.cx(qreg_0[1],qreg_2[0])
main_circ.x(qreg_0[1])
main_circ.x(qreg_2[1])
main_circ.s(qreg_2[0])
main_circ.s(qreg_0[1])
main_circ.cx(qreg_2[1],qreg_2[0])
main_circ.rx(param_2, qreg_2[0])
bindings = {param_0: -0.197000, param_1: -0.074000, param_2: 0.332000, param_4: 0.285000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1282")
