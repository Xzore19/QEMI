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
subcirc0.u(0.377000,-0.892000,-0.823000, qreg_2[1])
subcirc0.rz(-0.264000, qreg_2[1])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_2[0])

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
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_3[0])
subcirc1.rz(0.195000, qreg_0[0])
subcirc1.y(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.256000, qreg_3[0])
subcirc2.rz(0.095000, qreg_0[2])
subcirc2.s(qreg_0[1])
subcirc2.u(0.477000,0.095000,-0.967000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.u(0.431000,0.254000,-0.943000, qreg_0[1])
subcirc3.s(qreg_0[2])
subcirc3.rz(0.539000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.rz(-0.563000, qreg_0[0])
subcirc4.s(qreg_1[2])
subcirc4.s(qreg_1[1])
subcirc4.s(qreg_1[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.s(qreg_3[0])
main_circ.rz(-0.184000, qreg_0[0])
main_circ.u(0.135000,param_1,-0.856000, qreg_0[2])
main_circ.s(qreg_3[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.y(qreg_0[0])
main_circ.u(-1.000000,param_1,param_1, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.s(qreg_3[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.u(-0.047000,param_0,-0.757000, qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.y(qreg_3[0])
main_circ.s(qreg_3[0])
main_circ.u(param_1,-0.646000,0.725000, qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.rz(param_1, qreg_0[0])
main_circ.rz(param_1, qreg_0[0])
main_circ.rz(param_0, qreg_0[2])
bindings = {param_0: 0.050000, param_1: -0.769000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1234")
