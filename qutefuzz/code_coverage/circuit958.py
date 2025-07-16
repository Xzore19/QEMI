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
subcirc0.cz(qreg_2[1],qreg_0[0])
subcirc0.cy(qreg_2[0],qreg_2[1])
subcirc0.cz(qreg_2[0],qreg_2[1])
subcirc0.cy(qreg_1[0],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.x(3)
main_circ.s(2)
main_circ.cz(0,3)
main_circ.cz(0,3)
main_circ.cz(2,1)
main_circ.cy(1,0)
main_circ.x(1)
main_circ.x(3)
main_circ.x(0)
main_circ.cy(0,1)
main_circ.s(2)
main_circ.s(0)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.s(3)
main_circ.s(0)
main_circ.append(subcirc0,[2,1,0,3])
main_circ.cy(2,0)
main_circ.s(3)
main_circ.cy(1,2)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.x(3)
main_circ.s(3)
main_circ.x(3)
main_circ.s(3)
main_circ.cy(0,2)
main_circ.cy(3,0)
main_circ.x(1)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.s(3)
main_circ.x(2)
main_circ.cz(0,2)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.s(3)
main_circ.x(3)
main_circ.x(3)
main_circ.s(3)
main_circ.append(subcirc0,[3,2,1,0])
main_circ.x(3)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "958")
