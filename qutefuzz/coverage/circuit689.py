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
subcirc0.z(qreg_0[1])
subcirc0.u(0.887000,-0.544000,0.975000, qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_2[0])
subcirc0.u(0.527000,0.169000,0.361000, qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_2[0])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.u(0.786000,0.967000,0.786000, qreg_2[0])
subcirc1.y(qreg_2[1])
subcirc1.cz(qreg_0[1],qreg_2[1])
subcirc1.z(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.911000,0.777000,0.915000, qreg_3[0])
subcirc2.y(qreg_3[0])
subcirc2.cz(qreg_0[2],qreg_3[0])
subcirc2.z(qreg_0[2])
subcirc2.z(qreg_3[0])
subcirc2.y(qreg_0[2])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.y(3)
main_circ.y(1)
main_circ.u(-0.198000,0.693000,-0.782000, 2)
main_circ.cz(3,2)
main_circ.cz(1,3)
main_circ.y(2)
main_circ.z(3)
main_circ.append(subcirc1,[2,3,0,1])
main_circ.append(subcirc1,[3,0,1,2])
main_circ.cz(0,1)
main_circ.z(3)
main_circ.z(0)
main_circ.y(2)
main_circ.append(subcirc1,[3,1,2,0])
main_circ.z(2)
main_circ.u(param_2,0.758000,-0.697000, 0)
main_circ.append(subcirc2,[2,1,3,0])
main_circ.y(3)
main_circ.cz(2,3)
main_circ.cz(3,2)
main_circ.cz(2,1)
main_circ.cz(0,3)
main_circ.cz(0,1)
main_circ.cz(1,0)
main_circ.append(subcirc1,[1,2,3,0])
main_circ.y(1)
main_circ.y(3)
main_circ.cz(0,1)
main_circ.y(3)
bindings = {param_2: 0.322000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "689")
