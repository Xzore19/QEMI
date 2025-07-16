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
subcirc0.cx(qreg_1[0],qreg_2[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.cx(qreg_2[1],qreg_1[0])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.591000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[3])
subcirc1.y(qreg_0[0])
subcirc1.s(qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.s(qreg_1[1])
subcirc2.rz(-0.801000, qreg_1[2])
subcirc2.cx(qreg_1[1],qreg_1[2])
subcirc2.y(qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cx(qreg_2[1],qreg_0[1])
subcirc3.rz(-0.251000, qreg_0[1])
subcirc3.rz(-0.877000, qreg_2[1])
subcirc3.rz(0.095000, qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

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

main_circ.rz(0.327000, 3)
main_circ.s(0)
main_circ.s(0)
main_circ.cx(2,3)
main_circ.rz(param_2, 2)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.rz(param_2, 3)
main_circ.y(0)
main_circ.rz(0.547000, 3)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.rz(param_0, 3)
main_circ.cx(2,0)
main_circ.rz(0.651000, 3)
main_circ.rz(0.838000, 0)
main_circ.y(1)
main_circ.cx(3,2)
main_circ.y(1)
main_circ.y(2)
main_circ.s(3)
main_circ.s(0)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.rz(param_1, 3)
main_circ.cx(1,2)
main_circ.s(0)
main_circ.append(subcirc1,[2,3,0,1])
main_circ.cx(1,0)
main_circ.cx(3,0)
main_circ.cx(2,0)
main_circ.cx(0,2)
main_circ.cx(2,0)
main_circ.s(0)
main_circ.y(2)
main_circ.rz(0.153000, 0)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.s(3)
main_circ.rz(-0.083000, 2)
main_circ.s(0)
main_circ.y(3)
bindings = {param_0: -0.497000, param_1: -0.726000, param_2: -0.349000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1451")
