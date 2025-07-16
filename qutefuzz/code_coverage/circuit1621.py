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
subcirc0.x(qreg_0[2])
subcirc0.ry(0.332000, qreg_3[0])
subcirc0.ry(0.792000, qreg_0[1])
subcirc0.ry(-0.558000, qreg_0[2])
subcirc0.ry(-0.771000, qreg_0[1])
subcirc0.ry(0.201000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_0[2])
subcirc1.rx(-0.633000, qreg_0[2])
subcirc1.ry(-0.306000, qreg_0[2])
subcirc1.rx(-0.133000, qreg_0[2])
subcirc1.x(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.rx(-0.656000, qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.ry(-0.417000, qreg_0[0])
subcirc2.x(qreg_0[1])
subcirc2.x(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.y(1)
main_circ.append(subcirc1,[2,3,1,qreg_0[0]])
main_circ.rx(param_3, 2)
main_circ.y(1)
main_circ.y(2)
main_circ.append(subcirc2,[2,3,0,qreg_0[0]])
main_circ.ry(-0.100000, qreg_0[0])
main_circ.x(0)
main_circ.y(qreg_1[0])
main_circ.append(subcirc0,[2,qreg_1[0],qreg_0[0],1,3,0])
main_circ.ry(-0.946000, 0)
main_circ.append(subcirc2,[qreg_0[0],3,1,2])
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],0,1])
main_circ.append(subcirc2,[qreg_0[0],3,qreg_1[0],0])
main_circ.append(subcirc2,[2,0,qreg_1[0],3])
main_circ.x(1)
main_circ.rx(param_1, qreg_1[0])
main_circ.x(qreg_0[0])
bindings = {param_1: 0.055000, param_3: 0.630000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1621")
