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
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,0.426000,0.557000, qreg_1[0])
subcirc0.rz(-0.616000, qreg_2[0])
subcirc0.y(qreg_3[0])
subcirc0.u(pi/2,-0.276000,0.335000, qreg_1[0])
subcirc0.rz(0.127000, qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_3[0])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.u(pi/2,0.248000,0.559000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.rz(-0.351000, qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],0,qreg_0[0]])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],0,qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.u(pi/2,param_0,param_0, qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_0[0],0)
main_circ.u(pi/2,-0.552000,param_0, 0)
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],0])
main_circ.u(pi/2,param_0,param_0, qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],0,qreg_0[2]])
main_circ.u(param_0,param_0,-0.982000, qreg_0[2])
main_circ.rz(param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],0])
bindings = {param_0: 0.963000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
