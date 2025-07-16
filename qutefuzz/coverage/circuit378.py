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
subcirc0.cz(qreg_0[0],qreg_2[0])
subcirc0.cz(qreg_2[1],qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.u(pi/2,0.694000,-0.362000, qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_1[1],qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,0.125000,0.244000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_1[0]])
main_circ.u(param_0,0.157000,0.099000, qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_2[0]])
main_circ.z(qreg_1[0])
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.u(param_0,param_0,0.407000, qreg_1[0])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.z(qreg_2[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_1[0],qreg_3[0]])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[0],qreg_2[0],qreg_0[0]])
main_circ.h(qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_2[0],qreg_3[0]])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.z(qreg_3[0])
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_2[0],qreg_0[0],qreg_1[0]])
main_circ.u(param_0,-0.428000,-0.980000, qreg_0[0])
main_circ.h(qreg_2[0])
bindings = {param_0: -0.105000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
