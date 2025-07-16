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
subcirc0.rz(-0.697000, qreg_2[1])
subcirc0.u(-0.084000,-0.890000,0.173000, qreg_0[1])
subcirc0.rz(0.418000, qreg_2[0])
subcirc0.rz(0.737000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_2[0],qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_2[0])
subcirc1.cy(qreg_3[0],qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0.225000,0.893000,-0.015000, qreg_0[1])
subcirc2.rz(0.846000, qreg_0[2])
subcirc2.u(0.902000,0.217000,-0.350000, qreg_0[0])
subcirc2.rz(0.265000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.329000, qreg_0[2])
subcirc3.cx(qreg_0[2],qreg_3[0])
subcirc3.u(0.365000,-0.348000,-0.589000, qreg_0[0])
subcirc3.u(-0.732000,0.158000,0.846000, qreg_0[0])

main_circ = QuantumCircuit(0)
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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.u(0.095000,0.740000,-0.650000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.rz(0.543000, qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_3[0])
main_circ.u(0.083000,param_5,0.404000, qreg_0[1])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.u(param_3,param_0,-0.038000, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.u(0.821000,-0.767000,0.750000, qreg_0[1])
main_circ.rz(param_0, qreg_3[0])
main_circ.rz(0.636000, qreg_0[2])
main_circ.cy(qreg_0[0],qreg_0[2])
bindings = {param_0: -0.624000, param_3: 0.586000, param_5: -0.996000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
