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
subcirc0.rx(-0.792000, qreg_3[0])
subcirc0.rx(-0.371000, qreg_0[1])
subcirc0.rx(0.032000, qreg_0[0])
subcirc0.x(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.493000, qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1.ry(-0.124000, qreg_0[0])
subcirc1.rz(0.263000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(-0.109000, qreg_0[1])
subcirc2.ry(0.576000, qreg_0[3])
subcirc2.ry(0.675000, qreg_0[0])
subcirc2.ry(-0.396000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(-0.891000, qreg_0[1])
subcirc3.rz(-0.234000, qreg_0[3])
subcirc3.x(qreg_0[2])
subcirc3.rx(0.292000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.rz(-0.580000, qreg_2[1])
subcirc4.rz(0.609000, qreg_2[0])
subcirc4.rz(-0.969000, qreg_2[1])
subcirc4.ry(0.746000, qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rz(0.236000, 0)
main_circ.append(subcirc3,[0,qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.rz(param_1, qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],0,qreg_3[0],qreg_0[0]])
main_circ.ry(param_1, 0)
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_1[0],qreg_3[0],0])
main_circ.append(subcirc2,[qreg_3[0],qreg_2[0],0,qreg_0[0],qreg_1[0]])
main_circ.rz(param_2, qreg_2[0])
main_circ.x(0)
main_circ.x(qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.ry(param_0, qreg_1[0])
main_circ.rx(-0.644000, 0)
main_circ.rz(param_0, qreg_1[0])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],0,qreg_2[0]])
main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],0,qreg_2[0]])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],qreg_1[0],0])
main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],0,qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_3[0],qreg_1[0]])
main_circ.rz(param_0, 0)
main_circ.rz(-0.903000, qreg_0[0])
main_circ.ry(param_1, qreg_1[0])
bindings = {param_0: -0.676000, param_1: -0.771000, param_2: 0.523000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "424")
