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
subcirc0.ry(0.507000, qreg_3[0])
subcirc0.z(qreg_1[0])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.z(qreg_1[0])
subcirc0.x(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(-0.345000, qreg_0[2])
subcirc1.y(qreg_0[3])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.y(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[3])
subcirc2.y(qreg_0[2])
subcirc2.x(qreg_0[2])
subcirc2.y(qreg_0[3])
subcirc2.y(qreg_0[3])
subcirc2.y(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.y(qreg_2[0])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_2[0])
subcirc3.y(qreg_0[0])
subcirc3.x(qreg_0[0])
subcirc3.y(qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.x(qreg_0[3])
subcirc4.x(qreg_0[3])
subcirc4.z(qreg_0[1])
subcirc4.ry(-0.317000, qreg_0[1])
subcirc4.z(qreg_0[2])
subcirc4.ry(0.722000, qreg_0[2])

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

main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_1[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_1[0],qreg_1[1]])
main_circ.x(qreg_3[0])
main_circ.z(qreg_1[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_1[1],qreg_0[0]])
main_circ.ry(0.244000, qreg_1[0])
main_circ.append(subcirc4,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.z(qreg_3[0])
main_circ.ry(0.362000, qreg_3[0])
main_circ.ry(0.630000, qreg_3[0])
main_circ.ry(-0.199000, qreg_1[0])
main_circ.z(qreg_0[0])
main_circ.z(qreg_3[0])
main_circ.ry(-0.870000, qreg_1[1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "295")
