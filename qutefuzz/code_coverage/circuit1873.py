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
subcirc0.u(pi/2,-0.471000,0.293000, qreg_2[0])
subcirc0.rx(0.866000, qreg_2[1])
subcirc0.ry(0.952000, qreg_2[1])
subcirc0.u(-0.657000,-0.070000,-0.454000, qreg_2[1])
subcirc0.u(pi/2,-0.947000,-0.824000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.201000, qreg_0[1])
subcirc1.ry(-0.178000, qreg_2[0])
subcirc1.ry(0.515000, qreg_2[0])
subcirc1.ry(0.410000, qreg_0[0])
subcirc1.ry(0.400000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.993000, qreg_0[2])
subcirc2.ry(-0.011000, qreg_3[0])
subcirc2.rx(-0.949000, qreg_0[0])
subcirc2.rx(-0.378000, qreg_0[1])
subcirc2.u(pi/2,-0.355000,-0.912000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.213000, qreg_1[1])
subcirc3.ry(0.674000, qreg_1[1])
subcirc3.u(0.999000,-0.509000,-0.243000, qreg_0[0])
subcirc3.u(0.049000,-0.572000,-0.645000, qreg_3[0])
subcirc3.u(pi/2,-0.317000,-0.918000, qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.rx(param_4, 0)
main_circ.ry(param_4, qreg_0[1])
main_circ.ry(0.429000, qreg_0[2])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc2,[0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.ry(-0.640000, qreg_0[1])
main_circ.u(param_3,param_0,param_1, 0)
main_circ.u(-0.735000,0.205000,-0.231000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2],0])
main_circ.u(param_3,-0.008000,param_1, qreg_0[2])
main_circ.ry(-0.025000, qreg_0[0])
main_circ.ry(0.689000, qreg_0[3])
main_circ.ry(-0.986000, qreg_0[2])
main_circ.rx(-0.358000, 0)
main_circ.u(0.911000,param_2,-0.023000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],0,qreg_0[3],qreg_0[0]])
main_circ.append(subcirc2,[0,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.rx(param_3, qreg_0[3])
main_circ.u(-0.998000,param_1,0.805000, qreg_0[0])
main_circ.ry(0.770000, qreg_0[3])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[1],0,qreg_0[3]])
main_circ.u(0.518000,param_3,param_1, 0)
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.u(param_2,param_4,-0.462000, qreg_0[0])
main_circ.u(pi/2,-0.995000,-0.482000, qreg_0[2])
bindings = {param_0: 0.415000, param_1: -0.787000, param_2: -0.777000, param_3: -0.859000, param_4: -0.647000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
