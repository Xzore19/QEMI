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
subcirc0.ry(0.211000, qreg_0[2])
subcirc0.ry(-0.950000, qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.rz(0.854000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.ry(0.760000, qreg_0[2])
subcirc1.ry(0.415000, qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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

main_circ.s(qreg_0[0])
main_circ.s(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.ry(param_2, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[3])
main_circ.y(qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.ry(-0.123000, qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.s(qreg_0[3])
main_circ.rz(0.774000, qreg_0[1])
main_circ.s(qreg_0[1])
main_circ.ry(-0.525000, qreg_0[0])
main_circ.y(qreg_0[3])
main_circ.s(qreg_0[3])
main_circ.y(qreg_0[1])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.ry(-0.570000, qreg_0[1])
main_circ.y(qreg_0[3])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
main_circ.ry(-0.507000, qreg_0[0])
main_circ.ry(-0.300000, qreg_0[2])
main_circ.rz(-0.616000, qreg_0[1])
main_circ.rz(-0.911000, qreg_0[0])
main_circ.rz(param_0, qreg_0[2])
main_circ.y(qreg_0[3])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.ry(0.993000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.rz(param_2, qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.rz(0.284000, qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.rz(0.427000, qreg_0[1])
main_circ.s(qreg_0[3])
bindings = {param_0: 0.262000, param_2: -0.353000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
