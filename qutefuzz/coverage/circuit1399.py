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
subcirc0.cx(qreg_3[0],qreg_1[1])
subcirc0.rz(0.440000, qreg_0[0])
subcirc0.rz(-0.253000, qreg_3[0])
subcirc0.ry(0.729000, qreg_1[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.ry(param_0, qreg_0[2])
main_circ.cx(qreg_0[3],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.ry(-0.993000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.y(qreg_0[0])
main_circ.rz(0.654000, qreg_0[3])
main_circ.rz(param_0, qreg_0[3])
main_circ.rz(-0.759000, qreg_0[2])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.y(qreg_0[3])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.ry(-0.120000, qreg_0[3])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.rz(0.470000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.y(qreg_0[3])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.ry(param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.rz(0.812000, qreg_0[3])
main_circ.y(qreg_0[2])
main_circ.rz(param_1, qreg_0[2])
bindings = {param_0: -0.180000, param_1: 0.552000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1399")
