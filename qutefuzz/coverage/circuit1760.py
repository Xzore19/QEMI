from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.x(qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.x(qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.x(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.rz(0.122000, qreg_2[1])
subcirc2.h(qreg_0[1])
subcirc2.h(qreg_0[0])
subcirc2.rz(-0.557000, qreg_2[0])
subcirc2.h(qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.x(qreg_1[1])
subcirc3.h(qreg_1[2])
subcirc3.s(qreg_1[2])
subcirc3.s(qreg_0[0])
subcirc3.x(qreg_1[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[3,0,1,qreg_0[0]])
main_circ.x(1)
main_circ.append(subcirc1,[1,0,2,qreg_0[0]])
main_circ.append(subcirc2,[3,2,1,0])
main_circ.s(1)
main_circ.append(subcirc3,[qreg_0[0],1,2,0])
main_circ.rz(param_0, 1)
main_circ.x(3)
main_circ.x(3)
main_circ.append(subcirc2,[2,3,1,0])
main_circ.x(0)
main_circ.h(3)
main_circ.append(subcirc3,[3,qreg_0[0],1,2])
main_circ.append(subcirc1,[qreg_0[0],1,2,3])
main_circ.s(qreg_0[0])
main_circ.x(2)
main_circ.x(0)
main_circ.rz(param_1, 0)
bindings = {param_0: 0.891000, param_1: 0.417000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1760")
