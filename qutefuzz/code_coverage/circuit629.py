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
subcirc0.u(pi/2,-0.957000,0.457000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.u(pi/2,0.635000,0.268000, qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_2[0])
subcirc0.z(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.u(pi/2,0.428000,-0.792000, qreg_0[0])
subcirc1.z(qreg_3[0])
subcirc1.u(pi/2,-0.312000,0.113000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[2])

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

main_circ.append(subcirc1,[qreg_0[0],2,qreg_0[1],0])
main_circ.u(pi/2,-0.248000,0.384000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],3,2,1])
main_circ.cx(3,qreg_0[1])
main_circ.cy(3,qreg_0[0])
main_circ.cy(1,3)
main_circ.cy(qreg_0[0],1)
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],0,3])
main_circ.cx(2,qreg_0[1])
main_circ.cy(qreg_0[0],1)
main_circ.append(subcirc0,[1,0,qreg_0[0],2])
main_circ.cx(1,3)
main_circ.z(2)
main_circ.append(subcirc0,[qreg_0[1],0,1,3])
main_circ.z(2)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "629")
