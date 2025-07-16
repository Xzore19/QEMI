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
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.rx(-0.417000, qreg_0[3])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.rx(-0.997000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_1[0],qreg_2[0])
subcirc2.rx(0.150000, qreg_3[0])
subcirc2.cx(qreg_1[0],qreg_0[0])
subcirc2.rx(-0.638000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.y(qreg_0[0])
subcirc3.rx(0.073000, qreg_0[1])
subcirc3.cy(qreg_0[1],qreg_2[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.rx(0.254000, qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.rx(0.543000, qreg_0[0])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.rx(param_1, qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.rx(-0.106000, qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.rx(-0.672000, qreg_0[1])
bindings = {param_1: -0.535000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
