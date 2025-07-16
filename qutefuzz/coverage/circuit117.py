from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(0.068000, qreg_2[0])
subcirc0.rz(0.321000, qreg_2[1])
subcirc0.x(qreg_2[1])
subcirc0.s(qreg_2[0])
subcirc0.x(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.s(qreg_0[0])
subcirc1.ry(0.458000, qreg_0[1])
subcirc1.ry(-0.972000, qreg_0[3])
subcirc1.rz(0.136000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.ry(-0.607000, qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_0[1])
subcirc2.rz(-0.184000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[2])
subcirc3.rz(-0.557000, qreg_3[0])
subcirc3.ry(-0.831000, qreg_0[2])
subcirc3.s(qreg_3[0])
subcirc3.s(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.723000, qreg_0[1])
subcirc4.ry(-0.605000, qreg_3[0])
subcirc4.rz(0.926000, qreg_3[0])
subcirc4.rz(-0.879000, qreg_0[1])
subcirc4.x(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],2,3,0])
main_circ.s(2)
main_circ.rz(0.507000, qreg_0[0])
main_circ.append(subcirc0,[1,0,2,3])
main_circ.x(3)
main_circ.append(subcirc0,[1,0,qreg_0[0],3])
main_circ.rz(param_1, 1)
main_circ.append(subcirc4,[0,1,2,3])
main_circ.append(subcirc0,[0,1,3,qreg_0[0]])
main_circ.s(1)
main_circ.ry(param_0, qreg_0[0])
main_circ.s(2)
main_circ.append(subcirc4,[3,0,2,qreg_0[0]])
main_circ.append(subcirc4,[3,2,0,qreg_0[0]])
bindings = {param_0: 0.841000, param_1: -0.668000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "117")
