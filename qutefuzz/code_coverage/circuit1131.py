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
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0.u(0,0,0.951000, qreg_0[1])
subcirc0.u(0,0,-0.158000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_2[0])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0,0,-0.023000, qreg_0[1])
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.u(0,0,-0.812000, qreg_2[1])
subcirc2.u(0,0,-0.181000, qreg_0[0])
subcirc2.u(0,0,0.191000, qreg_2[0])
subcirc2.x(qreg_2[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(0.436000,-0.106000,-0.766000, qreg_1[2])
subcirc3.u(-0.021000,0.072000,-0.757000, qreg_0[0])
subcirc3.cz(qreg_1[2],qreg_1[1])
subcirc3.u(0.799000,-0.605000,-0.407000, qreg_1[1])
subcirc3.cz(qreg_1[1],qreg_1[0])
subcirc3.x(qreg_1[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[0],qreg_0[2])
subcirc4.u(0.573000,-0.663000,-0.984000, qreg_0[2])
subcirc4.cz(qreg_0[1],qreg_3[0])
subcirc4.u(0.970000,-0.039000,0.111000, qreg_0[0])
subcirc4.u(-0.819000,0.016000,-0.426000, qreg_0[2])
subcirc4.cz(qreg_3[0],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.u(param_0,param_1,param_2, qreg_0[1])
main_circ.u(param_1,param_2,-0.842000, qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.x(qreg_0[3])
main_circ.u(param_0,param_2,param_2, qreg_0[3])
main_circ.x(qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.u(0,param_2,0.103000, qreg_0[3])
main_circ.u(param_1,param_2,param_2, qreg_0[3])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.u(0.776000,0.053000,0.818000, qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[3])
main_circ.append(subcirc3,[qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.u(param_1,0,param_0, qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.u(param_2,param_1,param_1, qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.u(param_1,-0.925000,-0.321000, qreg_0[1])
main_circ.u(param_1,0,0.052000, qreg_0[0])
main_circ.u(param_1,param_1,-0.157000, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.u(param_1,param_1,0.801000, qreg_0[2])
main_circ.u(param_0,-0.103000,-0.626000, qreg_0[1])
bindings = {param_0: 0.106000, param_1: -0.393000, param_2: 0.349000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
