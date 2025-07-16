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
subcirc0.u(0.089000,-0.775000,0.198000, qreg_1[2])
subcirc0.u(pi/2,-0.911000,-0.905000, qreg_1[2])
subcirc0.u(pi/2,-0.070000,-0.490000, qreg_1[1])
subcirc0.cz(qreg_1[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.809000,0.747000, qreg_1[0])
subcirc1.cz(qreg_1[0],qreg_3[0])
subcirc1.z(qreg_1[1])
subcirc1.cz(qreg_1[0],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,-0.869000,0.323000, qreg_1[0])
subcirc2.z(qreg_2[0])
subcirc2.u(-0.176000,-0.114000,-0.822000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.u(-0.647000,-0.385000,-0.051000, qreg_0[2])
subcirc3.u(-0.770000,0.373000,0.844000, qreg_0[2])
subcirc3.u(-0.006000,-0.585000,-0.348000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(0)
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

main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.cz(qreg_0[1],qreg_0[3])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.u(param_0,param_3,0.366000, qreg_0[1])
main_circ.u(param_3,0.330000,param_2, qreg_0[0])
main_circ.u(pi/2,param_0,param_2, qreg_0[3])
main_circ.z(qreg_0[3])
main_circ.u(0.593000,0.996000,0.200000, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.u(pi/2,-0.714000,param_1, qreg_0[3])
main_circ.z(qreg_0[3])
main_circ.u(0.553000,param_2,-0.618000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.u(pi/2,-0.852000,param_2, qreg_0[3])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.u(param_0,param_1,param_2, qreg_0[3])
bindings = {param_0: 0.800000, param_1: 0.697000, param_2: 0.491000, param_3: -0.459000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
