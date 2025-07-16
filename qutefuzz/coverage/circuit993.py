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
subcirc0.y(qreg_0[3])
subcirc0.y(qreg_0[1])
subcirc0.rx(0.091000, qreg_0[1])
subcirc0.rx(-0.945000, qreg_0[0])
subcirc0.s(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_2[1])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_2[1],qreg_2[0])
subcirc1.y(qreg_0[1])
subcirc1.rx(0.290000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.rx(-0.080000, qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.s(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.s(3)
main_circ.y(0)
main_circ.y(1)
main_circ.s(3)
main_circ.rx(param_0, 1)
main_circ.rx(param_0, 2)
main_circ.s(3)
main_circ.rx(param_0, 2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc1,[1,3,2,0])
main_circ.rx(param_1, 0)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.s(2)
main_circ.y(0)
main_circ.s(0)
main_circ.append(subcirc1,[2,3,1,0])
main_circ.cx(2,3)
main_circ.cx(3,1)
main_circ.cx(2,0)
main_circ.cx(2,1)
main_circ.append(subcirc1,[2,1,3,0])
main_circ.rx(0.571000, 2)
main_circ.cx(1,3)
main_circ.s(3)
bindings = {param_0: -0.550000, param_1: -0.902000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "993")
