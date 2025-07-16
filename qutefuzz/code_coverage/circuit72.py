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
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.z(qreg_0[3])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.rz(-0.998000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_2[1])
subcirc1.y(qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.rz(0.929000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.rz(0.732000, qreg_0[1])
subcirc2.rz(0.133000, qreg_3[0])
subcirc2.rz(-0.272000, qreg_0[1])
subcirc2.z(qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc1,[3,2,0,1])
main_circ.cy(1,3)
main_circ.append(subcirc2,[3,1,0,2])
main_circ.y(3)
main_circ.y(2)
main_circ.z(2)
main_circ.z(1)
main_circ.z(1)
main_circ.y(2)
main_circ.cy(2,0)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.rz(0.957000, 2)
main_circ.append(subcirc2,[0,2,3,1])
main_circ.append(subcirc2,[1,0,2,3])
main_circ.cy(2,0)
main_circ.cy(1,0)
main_circ.cy(0,3)
main_circ.cy(2,3)
main_circ.cy(0,3)
main_circ.cy(0,1)
main_circ.cy(0,3)
main_circ.cy(3,1)
main_circ.cy(3,2)
main_circ.cy(1,3)
main_circ.cy(1,2)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "72")
