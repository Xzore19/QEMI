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
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.u(0.603000,-0.536000,-0.921000, qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_3[0])
subcirc0.u(0.697000,-0.321000,0.720000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.554000,-0.666000,0.114000, qreg_0[0])
subcirc1.rx(0.746000, qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.rx(0.616000, qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.u(0.557000,-0.161000,0.950000, qreg_0[1])
subcirc2.u(0.838000,0.912000,0.084000, qreg_0[1])
subcirc2.u(0.558000,-0.748000,-0.001000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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
param_6 = Parameter("param_6")

main_circ.append(subcirc2,[0,qreg_1[0],3,2,qreg_0[0],1])
main_circ.cx(0,qreg_1[0])
main_circ.append(subcirc0,[2,qreg_0[0],1,0])
main_circ.append(subcirc1,[1,3,qreg_1[0],0])
main_circ.u(-0.895000,0.336000,param_4, 0)
main_circ.cz(0,3)
main_circ.append(subcirc1,[0,2,qreg_0[0],1])
main_circ.cx(2,0)
main_circ.append(subcirc1,[1,qreg_0[0],0,3])
main_circ.cx(1,qreg_0[0])
main_circ.append(subcirc0,[1,3,qreg_0[0],0])
main_circ.append(subcirc1,[qreg_1[0],3,0,2])
main_circ.u(-0.164000,param_4,0.047000, 3)
main_circ.u(-0.611000,-0.721000,0.415000, qreg_1[0])
main_circ.append(subcirc0,[2,qreg_0[0],3,1])
main_circ.append(subcirc0,[1,qreg_1[0],2,3])
main_circ.cz(2,qreg_1[0])
main_circ.cz(qreg_1[0],0)
main_circ.rx(0.852000, 0)
main_circ.u(param_4,param_5,param_1, qreg_0[0])
bindings = {param_1: -0.881000, param_4: 0.566000, param_5: 0.571000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
