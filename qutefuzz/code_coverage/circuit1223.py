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
subcirc0.rz(0.083000, qreg_3[0])
subcirc0.y(qreg_0[2])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.rz(-0.879000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.z(3)
main_circ.z(0)
main_circ.cz(2,3)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.cz(3,2)
main_circ.y(1)
main_circ.rz(param_2, 2)
main_circ.z(3)
main_circ.z(1)
main_circ.cz(0,2)
main_circ.y(3)
main_circ.y(0)
main_circ.cz(0,2)
main_circ.rz(param_1, 0)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.rz(param_2, 1)
main_circ.rz(param_1, 1)
main_circ.y(0)
main_circ.rz(-0.581000, 3)
main_circ.cz(1,0)
main_circ.rz(param_2, 2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc0,[2,1,0,3])
main_circ.y(1)
main_circ.cz(1,0)
main_circ.y(2)
main_circ.cz(1,2)
main_circ.cz(2,0)
main_circ.cz(0,2)
main_circ.cz(3,2)
main_circ.cz(2,3)
main_circ.cz(1,0)
main_circ.cz(3,1)
main_circ.cz(1,3)
main_circ.z(1)
main_circ.z(0)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.z(3)
main_circ.y(2)
main_circ.cz(2,1)
bindings = {param_1: -0.191000, param_2: -0.979000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1223")
