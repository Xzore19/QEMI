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
subcirc0.z(qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0.u(-0.724000,0.047000,0.393000, qreg_0[3])
subcirc0.cz(qreg_0[2],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.u(0.080000,-0.801000,-0.443000, qreg_0[0])
subcirc1.u(-0.653000,0.730000,-0.996000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_1[1])
subcirc2.s(qreg_0[0])
subcirc2.cz(qreg_1[0],qreg_3[0])
subcirc2.u(-0.479000,-0.037000,-0.746000, qreg_3[0])
subcirc2.cz(qreg_3[0],qreg_1[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.s(qreg_0[1])
subcirc3.cz(qreg_0[1],qreg_0[3])
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3.cz(qreg_0[3],qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.s(qreg_0[1])
subcirc4.cz(qreg_0[1],qreg_2[0])
subcirc4.u(0.329000,0.357000,0.718000, qreg_0[0])
subcirc4.u(-0.563000,0.398000,-0.205000, qreg_2[0])
subcirc4.cz(qreg_3[0],qreg_0[0])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc4,[qreg_2[1],qreg_0[0],qreg_2[0],1])
main_circ.s(0)
main_circ.s(1)
main_circ.append(subcirc4,[qreg_2[1],1,qreg_2[0],qreg_0[0]])
main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1],1,0])
main_circ.s(qreg_2[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],1,qreg_2[1],0,qreg_2[0]])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_2[1],qreg_2[0],1,qreg_0[1]])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.u(0.067000,param_3,0.437000, 1)
main_circ.s(qreg_2[0])
main_circ.z(0)
main_circ.u(-0.073000,param_0,-0.523000, qreg_0[0])
main_circ.append(subcirc4,[0,qreg_0[1],qreg_2[0],1])
main_circ.z(qreg_0[0])
bindings = {param_0: 0.303000, param_3: -0.792000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
