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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.h(qreg_2[1])
subcirc0.rx(-0.785000, qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.rx(0.667000, qreg_0[0])
subcirc0.h(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(-0.799000, qreg_1[0])
subcirc1.h(qreg_0[0])
subcirc1.rx(-0.560000, qreg_2[0])
subcirc1.h(qreg_2[1])
subcirc1.rx(0.537000, qreg_2[1])
subcirc1.y(qreg_1[0])
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
subcirc2.rx(0.818000, qreg_0[0])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_2[0])
subcirc2.h(qreg_3[0])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.202000, qreg_0[0])
subcirc3.rx(-0.577000, qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3.rx(-0.106000, qreg_3[0])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.y(qreg_0[3])
subcirc4.z(qreg_0[2])
subcirc4.rx(0.757000, qreg_0[1])
subcirc4.y(qreg_0[0])
subcirc4.y(qreg_0[3])
subcirc4.y(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3],0])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[1],0,qreg_0[3],qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[2],qreg_0[3],qreg_0[0],0,qreg_0[1]])
main_circ.z(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3],0])
main_circ.h(qreg_0[1])
main_circ.y(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[3],0])
main_circ.y(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[3],qreg_0[2]])
main_circ.rx(param_3, qreg_0[3])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.h(qreg_0[0])
main_circ.rx(param_3, 0)
main_circ.h(qreg_0[2])
main_circ.z(qreg_0[0])
main_circ.rx(param_2, qreg_0[3])
main_circ.z(qreg_0[2])
main_circ.z(0)
main_circ.z(qreg_0[0])
bindings = {param_2: 0.140000, param_3: 0.063000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
