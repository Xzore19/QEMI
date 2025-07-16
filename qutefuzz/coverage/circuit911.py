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
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.765000,0.431000,-0.924000, qreg_0[1])
subcirc1.u(0.916000,-0.359000,0.881000, qreg_0[3])
subcirc1.y(qreg_0[2])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_1[1])
subcirc2.u(-0.314000,0.461000,0.838000, qreg_0[0])
subcirc2.z(qreg_1[0])
subcirc2.u(0.472000,-0.939000,-0.818000, qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[2])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.u(0.518000,-0.337000,-0.366000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.z(qreg_0[0])
subcirc4.u(0.308000,-0.393000,-0.204000, qreg_0[1])
subcirc4.rx(-0.470000, qreg_0[0])
subcirc4.y(qreg_3[0])

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

main_circ.append(subcirc4,[qreg_1[0],3,0,2])
main_circ.u(0.387000,param_1,param_2, 3)
main_circ.u(0.037000,-0.145000,-0.567000, 2)
main_circ.append(subcirc1,[qreg_0[0],3,0,2])
main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_1[0],2,0,3])
main_circ.append(subcirc0,[2,qreg_1[0],qreg_0[0],0,1])
main_circ.y(qreg_1[0])
main_circ.z(1)
main_circ.append(subcirc4,[0,qreg_1[0],2,3])
main_circ.append(subcirc1,[2,qreg_1[0],3,1])
main_circ.append(subcirc4,[0,qreg_1[0],2,1])
main_circ.z(2)
main_circ.append(subcirc0,[qreg_0[0],3,2,qreg_1[0],1])
main_circ.z(1)
main_circ.y(3)
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],0,3])
main_circ.append(subcirc4,[qreg_1[0],3,1,2])
main_circ.append(subcirc2,[2,3,1,qreg_0[0]])
main_circ.z(0)
main_circ.u(param_5,-0.146000,param_4, 0)
main_circ.z(3)
main_circ.u(param_5,param_1,param_3, 2)
bindings = {param_1: 0.704000, param_2: 0.858000, param_3: -0.152000, param_4: 0.670000, param_5: -0.522000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
