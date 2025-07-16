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
subcirc0.z(qreg_2[1])
subcirc0.z(qreg_2[1])
subcirc0.z(qreg_2[0])
subcirc0.x(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.rz(0.093000, qreg_1[2])
subcirc2.x(qreg_0[0])
subcirc2.rz(0.656000, qreg_1[1])
subcirc2.s(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.s(qreg_0[1])
subcirc3.x(qreg_0[1])
subcirc3.s(qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_0[2])
subcirc4.rz(-0.379000, qreg_3[0])
subcirc4.z(qreg_0[0])
subcirc4.s(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc2,[3,1,2,qreg_0[0]])
main_circ.append(subcirc0,[1,0,qreg_0[0],2])
main_circ.append(subcirc2,[qreg_0[0],2,1,0])
main_circ.append(subcirc1,[qreg_0[0],0,2,3,1])
main_circ.append(subcirc0,[3,0,qreg_0[0],1])
main_circ.s(2)
main_circ.append(subcirc3,[0,1,qreg_0[0],2])
main_circ.append(subcirc1,[qreg_0[0],1,3,0,2])
main_circ.rz(param_0, 3)
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[1,0,3,2])
main_circ.s(1)
main_circ.s(1)
main_circ.z(3)
main_circ.s(qreg_0[0])
main_circ.z(0)
main_circ.append(subcirc1,[qreg_0[0],2,1,3,0])
main_circ.s(3)
main_circ.x(3)
main_circ.s(3)
main_circ.append(subcirc2,[qreg_0[0],0,1,2])
main_circ.append(subcirc2,[qreg_0[0],1,2,0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc1,[0,3,qreg_0[0],1,2])
bindings = {param_0: 0.332000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
