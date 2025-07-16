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
subcirc0.y(qreg_0[1])
subcirc0.u(0,0,0.045000, qreg_0[1])
subcirc0.u(0,0,0.353000, qreg_0[3])
subcirc0.x(qreg_0[3])
subcirc0.x(qreg_0[3])
subcirc0.u(0,0,-0.442000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1.rz(0.192000, qreg_3[0])
subcirc1.y(qreg_3[0])
subcirc1.rz(-0.549000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[2])
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_3[0])
subcirc2.y(qreg_0[0])
subcirc2.u(0,0,0.067000, qreg_0[0])
subcirc2.u(0,0,0.530000, qreg_0[0])

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

main_circ.u(param_1,param_1,0.219000, qreg_1[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.rz(0.146000, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.append(subcirc1,[qreg_1[1],qreg_1[2],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc1,[qreg_1[1],qreg_0[0],qreg_1[2],qreg_1[0]])
main_circ.append(subcirc1,[qreg_1[2],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_1[2],qreg_0[0]])
main_circ.x(qreg_1[2])
bindings = {param_1: -0.081000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1623")
