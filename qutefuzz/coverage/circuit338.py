from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(pi/2,0.940000,-0.209000, qreg_0[0])
subcirc0.y(qreg_1[1])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_1[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.769000,-0.417000, qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.y(qreg_0[2])
subcirc2.s(qreg_0[1])
subcirc2.u(0,0,0.965000, qreg_0[3])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(qreg_0[0])
main_circ.u(param_0,0,param_2, qreg_0[1])
main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.s(qreg_0[0])
main_circ.y(1)
main_circ.u(param_0,param_0,0.013000, qreg_2[0])
main_circ.y(qreg_2[1])
main_circ.s(0)
main_circ.u(pi/2,-0.676000,param_1, 0)
main_circ.s(qreg_2[1])
main_circ.u(param_0,-0.479000,param_2, 0)
main_circ.append(subcirc1,[0,1,qreg_0[1],qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],0,1])
main_circ.u(param_0,param_2,param_1, qreg_0[1])
main_circ.u(param_0,param_0,-0.891000, qreg_0[1])
main_circ.append(subcirc1,[qreg_2[0],qreg_2[1],0,qreg_0[1],qreg_0[0],1])
main_circ.append(subcirc1,[qreg_2[1],qreg_2[0],qreg_0[0],1,qreg_0[1],0])
main_circ.u(0,param_2,-0.606000, qreg_2[1])
main_circ.s(qreg_2[1])
main_circ.append(subcirc0,[qreg_2[1],1,0,qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.y(0)
main_circ.u(0,0,-0.536000, 1)
main_circ.append(subcirc1,[1,qreg_0[1],qreg_0[0],qreg_2[1],0,qreg_2[0]])
main_circ.s(qreg_0[0])
main_circ.y(qreg_2[1])
main_circ.append(subcirc1,[1,0,qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.s(qreg_2[1])
bindings = {param_0: -0.053000, param_1: -0.072000, param_2: 0.779000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "338")
