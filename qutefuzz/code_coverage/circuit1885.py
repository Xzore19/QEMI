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
subcirc0.rz(-0.448000, qreg_0[3])
subcirc0.h(qreg_0[3])
subcirc0.rz(0.469000, qreg_0[3])
subcirc0.ry(0.721000, qreg_0[1])
subcirc0.ry(-0.223000, qreg_0[2])
subcirc0.ry(-0.146000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.637000, qreg_0[1])
subcirc1.rx(-0.188000, qreg_0[1])
subcirc1.rz(0.384000, qreg_0[2])
subcirc1.rx(0.560000, qreg_0[1])
subcirc1.h(qreg_0[3])
subcirc1.h(qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[3])
subcirc2.h(qreg_0[1])
subcirc2.h(qreg_0[3])
subcirc2.rz(-0.453000, qreg_0[3])
subcirc2.h(qreg_0[1])
subcirc2.ry(-0.701000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.356000, qreg_0[2])
subcirc3.rz(0.330000, qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3.ry(0.612000, qreg_0[1])
subcirc3.rz(-0.090000, qreg_0[0])
subcirc3.rx(-0.096000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(-0.513000, qreg_3[0])
subcirc4.rx(0.983000, qreg_0[0])
subcirc4.h(qreg_0[2])
subcirc4.rz(0.058000, qreg_0[0])
subcirc4.h(qreg_0[0])
subcirc4.rz(-0.394000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
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

main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[1],0])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.ry(param_1, qreg_0[0])
main_circ.ry(param_1, qreg_0[3])
main_circ.ry(param_1, qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.append(subcirc1,[0,qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.rz(param_0, 0)
main_circ.rz(0.312000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[1],0])
main_circ.rz(param_1, qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],0,qreg_0[1]])
main_circ.ry(param_0, qreg_0[1])
main_circ.rx(param_1, 0)
main_circ.rx(param_0, qreg_0[2])
bindings = {param_0: -0.267000, param_1: -0.908000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1885")
