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
subcirc0.y(qreg_2[1])
subcirc0.u(0.877000,-0.410000,0.322000, qreg_2[1])
subcirc0.rz(0.884000, qreg_2[0])
subcirc0.u(0.264000,-0.161000,-0.143000, qreg_2[1])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.073000,0.076000,-0.434000, qreg_3[0])
subcirc1.y(qreg_2[0])
subcirc1.y(qreg_1[0])
subcirc1.rz(0.646000, qreg_3[0])
subcirc1.z(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.y(qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_1[0])
subcirc3.z(qreg_3[0])
subcirc3.rz(0.133000, qreg_0[0])
subcirc3.z(qreg_1[0])
subcirc3.y(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.z(qreg_0[1])
subcirc4.y(qreg_0[1])
subcirc4.z(qreg_0[1])
subcirc4.u(-0.598000,0.399000,0.553000, qreg_0[0])
subcirc4.y(qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc4,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.rz(param_1, qreg_0[2])
main_circ.z(qreg_0[2])
main_circ.y(qreg_0[0])
main_circ.u(0.468000,-0.433000,param_1, qreg_0[1])
main_circ.rz(-0.301000, qreg_0[3])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.rz(-0.898000, qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.rz(-0.120000, qreg_0[1])
main_circ.y(qreg_0[0])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.y(qreg_0[0])
main_circ.rz(param_1, qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.rz(param_1, qreg_0[2])
main_circ.rz(param_1, qreg_0[0])
main_circ.y(qreg_0[3])
main_circ.z(qreg_0[3])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[2])
main_circ.rz(0.595000, qreg_0[2])
main_circ.rz(-0.377000, qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
bindings = {param_1: 0.530000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1860")
