from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rz(-0.094000, qreg_2[0])
subcirc0.ry(0.461000, qreg_2[1])
subcirc0.ry(-0.470000, qreg_1[0])
subcirc0.rz(0.459000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_0[3])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.ry(-0.383000, qreg_0[1])
subcirc1.cz(qreg_0[3],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.ry(0.198000, qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.z(qreg_0[0])
main_circ.z(qreg_0[2])
main_circ.z(qreg_0[2])
main_circ.rz(-0.811000, qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.ry(param_0, qreg_0[0])
main_circ.z(qreg_0[3])
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.ry(-0.309000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[2])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.rz(param_0, qreg_0[0])
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.rz(0.602000, qreg_0[3])
main_circ.z(qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.ry(0.394000, qreg_0[2])
main_circ.rz(param_0, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.rz(param_0, qreg_0[2])
bindings = {param_0: -0.580000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1812")
