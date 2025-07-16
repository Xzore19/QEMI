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
subcirc0.ry(0.624000, qreg_0[1])
subcirc0.z(qreg_2[0])
subcirc0.h(qreg_0[0])
subcirc0.ry(-0.743000, qreg_2[0])
subcirc0.u(0.288000,0.946000,0.480000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_1[0])
subcirc1.u(0.059000,0.531000,0.546000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_2[1])
subcirc1.h(qreg_2[0])

main_circ = QuantumCircuit(2)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.h(qreg_0[2])
main_circ.ry(param_3, 1)
main_circ.u(-0.491000,-0.397000,param_1, qreg_0[2])
main_circ.ry(-0.302000, qreg_0[2])
main_circ.ry(param_0, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.ry(0.563000, 1)
main_circ.ry(param_3, 0)
main_circ.ry(0.887000, qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],1])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],1,qreg_0[1]])
main_circ.ry(param_3, 0)
main_circ.h(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_3[0],0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],1,qreg_0[1]])
main_circ.append(subcirc0,[0,1,qreg_0[2],qreg_0[1]])
main_circ.ry(-0.451000, qreg_0[0])
main_circ.append(subcirc1,[1,qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.ry(param_0, qreg_0[2])
main_circ.ry(0.898000, 0)
bindings = {param_0: -0.901000, param_1: -0.934000, param_3: -0.223000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1811")
