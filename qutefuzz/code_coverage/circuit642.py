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
subcirc0.y(qreg_0[1])
subcirc0.rx(0.071000, qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.512000, qreg_3[0])
subcirc1.rx(0.127000, qreg_0[2])
subcirc1.rx(-0.689000, qreg_0[1])
subcirc1.z(qreg_0[2])
subcirc1.h(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.h(qreg_1[0])
subcirc2.h(qreg_3[0])
subcirc2.y(qreg_1[1])
subcirc2.y(qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.z(qreg_0[3])
subcirc3.h(qreg_0[2])
subcirc3.rx(-0.798000, qreg_0[2])
subcirc3.y(qreg_0[2])
subcirc3.h(qreg_0[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[0,qreg_3[0],1,qreg_0[0],qreg_0[1]])
main_circ.h(qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],0,qreg_0[0],qreg_3[0],1])
main_circ.append(subcirc2,[1,qreg_0[0],0,qreg_2[0],qreg_0[1]])
main_circ.y(qreg_0[1])
main_circ.append(subcirc3,[qreg_2[0],qreg_0[0],1,qreg_3[0]])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_3[0],0])
main_circ.y(qreg_0[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],0,1])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],1,qreg_2[0],qreg_0[0],0])
main_circ.rx(-0.146000, 1)
main_circ.h(qreg_0[0])
main_circ.y(1)
main_circ.rx(param_1, qreg_3[0])
bindings = {param_1: 0.890000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
