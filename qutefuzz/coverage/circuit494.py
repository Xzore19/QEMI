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
subcirc0.s(qreg_0[2])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[3])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.s(qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.s(qreg_0[0])

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],0,1])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(1,qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0],1])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],1,0,qreg_0[1]])
main_circ.s(qreg_0[2])
main_circ.cx(qreg_3[0],0)
main_circ.z(qreg_3[0])
main_circ.cx(0,qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[0],0)
main_circ.append(subcirc1,[qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.z(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.cz(1,qreg_0[2])
main_circ.cx(qreg_0[2],0)
main_circ.z(qreg_0[0])
main_circ.s(qreg_0[2])
main_circ.cz(0,qreg_0[0])
main_circ.cz(qreg_3[0],qreg_0[2])
main_circ.z(1)
main_circ.s(1)
main_circ.cz(qreg_0[2],1)
main_circ.cz(qreg_3[0],qreg_0[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
