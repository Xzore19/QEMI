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
subcirc0.u(0,0,0.433000, qreg_0[2])
subcirc0.u(-0.456000,0.248000,0.412000, qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_0[2])
subcirc0.u(0,0,-0.579000, qreg_0[2])
subcirc0.u(0,0,-0.854000, qreg_0[1])
subcirc0.u(-0.994000,0.379000,0.363000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.737000, qreg_3[0])
subcirc1.u(0.964000,-0.707000,-0.666000, qreg_0[2])
subcirc1.u(0,0,0.588000, qreg_0[1])
subcirc1.u(0,0,0.309000, qreg_0[1])
subcirc1.u(0,0,0.722000, qreg_0[1])
subcirc1.u(0,0,-0.956000, qreg_0[2])
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
subcirc2.cx(qreg_0[0],qreg_2[0])
subcirc2.u(0.938000,-0.959000,-0.774000, qreg_0[1])
subcirc2.u(0,0,-0.414000, qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_3[0])
subcirc2.rx(-0.350000, qreg_0[1])
subcirc2.u(-0.869000,-0.540000,-0.848000, qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],0])
main_circ.append(subcirc2,[qreg_0[1],0,qreg_3[0],qreg_0[0]])
main_circ.cx(0,qreg_3[0])
main_circ.cx(0,qreg_2[0])
main_circ.u(param_1,param_2,0.679000, 0)
main_circ.u(0,param_1,param_2, qreg_2[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],0,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],0,qreg_3[0]])
main_circ.u(-0.180000,-0.946000,-0.118000, qreg_2[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_2[0],0)
main_circ.u(0,0,-0.224000, qreg_2[0])
main_circ.u(0,0,param_1, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,qreg_2[0]])
main_circ.u(-0.862000,param_1,param_1, qreg_0[1])
main_circ.cx(qreg_0[0],qreg_2[0])
bindings = {param_1: 0.466000, param_2: -0.617000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "605")
