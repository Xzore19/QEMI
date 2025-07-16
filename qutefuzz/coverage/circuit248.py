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
subcirc0.h(qreg_1[0])
subcirc0.rz(-0.138000, qreg_1[0])
subcirc0.h(qreg_0[0])
subcirc0.rz(0.988000, qreg_2[1])
subcirc0.u(pi/2,0.847000,-0.967000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.rz(-0.027000, qreg_0[0])
subcirc1.u(pi/2,0.751000,0.871000, qreg_0[1])
subcirc1.rz(0.595000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.z(qreg_2[1])
subcirc2.z(qreg_2[1])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.h(qreg_0[1])
main_circ.z(0)
main_circ.rz(param_4, 2)
main_circ.z(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.h(0)
main_circ.append(subcirc2,[3,2,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[0,1,qreg_0[0],2])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[1],2])
main_circ.rz(param_0, 3)
main_circ.z(qreg_0[0])
main_circ.z(0)
main_circ.z(qreg_0[1])
main_circ.append(subcirc2,[0,qreg_0[1],3,qreg_0[0]])
main_circ.append(subcirc2,[2,qreg_0[1],qreg_0[0],3])
main_circ.h(3)
main_circ.h(0)
main_circ.rz(param_2, 1)
main_circ.z(0)
main_circ.u(pi/2,param_4,param_2, qreg_0[0])
main_circ.rz(-0.892000, 2)
main_circ.z(1)
main_circ.h(1)
main_circ.z(3)
main_circ.rz(0.515000, 0)
main_circ.rz(param_6, qreg_0[0])
main_circ.rz(-0.038000, qreg_0[0])
bindings = {param_0: 0.005000, param_2: 0.702000, param_4: 0.575000, param_6: -0.469000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "248")
