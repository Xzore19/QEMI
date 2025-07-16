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
subcirc0.ry(-0.426000, qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.rx(-0.491000, qreg_3[0])
subcirc0.rx(0.674000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.rx(-0.177000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.723000,-0.917000,-0.441000, qreg_0[1])
subcirc2.u(-0.094000,0.076000,0.324000, qreg_2[0])
subcirc2.ry(0.046000, qreg_0[1])
subcirc2.ry(-0.332000, qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0.540000,0.747000,0.778000, qreg_0[1])
subcirc3.rx(-0.714000, qreg_0[2])
subcirc3.z(qreg_0[3])
subcirc3.rx(-0.109000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.ry(0.203000, qreg_0[1])
subcirc4.z(qreg_0[1])
subcirc4.u(0.479000,-0.981000,-0.941000, qreg_0[2])
subcirc4.z(qreg_0[3])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(param_2, qreg_2[1])
main_circ.rx(-0.149000, qreg_2[0])
main_circ.rx(-0.619000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_1[0]])
main_circ.u(-0.427000,-0.813000,-0.900000, qreg_2[1])
main_circ.rx(param_2, qreg_2[1])
main_circ.u(param_1,param_1,-0.184000, qreg_0[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_1[0],qreg_0[0],qreg_2[1]])
main_circ.ry(0.732000, qreg_2[1])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_1[0],qreg_2[1]])
main_circ.z(qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.z(qreg_2[1])
main_circ.u(param_2,-0.548000,param_0, qreg_2[1])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_1[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_1[0],qreg_2[1]])
main_circ.rx(param_2, qreg_2[1])
main_circ.ry(param_0, qreg_0[0])
bindings = {param_0: 0.440000, param_1: -0.633000, param_2: -0.471000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1070")
