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
subcirc0.s(qreg_0[3])
subcirc0.cz(qreg_0[1],qreg_0[3])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0.u(0.176000,0.892000,0.285000, qreg_0[2])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0.u(0.808000,0.898000,0.991000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_3[0])
subcirc1.u(0.467000,0.938000,0.103000, qreg_1[1])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.u(0.833000,-0.060000,-0.429000, qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1.u(0.612000,0.083000,-0.611000, qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.u(-0.874000,-0.425000,0.149000, qreg_0[1])
subcirc2.s(qreg_2[0])
subcirc2.u(0,0,-0.344000, qreg_0[1])
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.u(0.980000,-0.977000,-0.177000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_3[0])
subcirc3.u(0,0,0.291000, qreg_0[1])
subcirc3.cz(qreg_0[0],qreg_0[2])
subcirc3.s(qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cz(qreg_2[0],qreg_0[0])
subcirc4.u(-0.241000,-0.437000,0.202000, qreg_2[1])
subcirc4.s(qreg_0[0])
subcirc4.u(0,0,0.792000, qreg_2[0])
subcirc4.cz(qreg_2[0],qreg_0[0])
subcirc4.u(0.902000,-0.788000,-0.609000, qreg_2[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(2)
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
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.s(qreg_0[1])
main_circ.append(subcirc4,[0,1,qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[0],1,0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[3],qreg_0[0],0,1])
main_circ.append(subcirc4,[qreg_0[1],qreg_0[3],qreg_0[0],1,0,qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[3],1,qreg_0[0],0,qreg_0[2],qreg_0[1]])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.cz(1,0)
main_circ.u(param_5,0,param_4, qreg_0[3])
main_circ.u(0,param_5,-0.115000, 0)
main_circ.u(param_5,param_1,-0.299000, qreg_0[0])
main_circ.cz(1,qreg_0[3])
bindings = {param_1: -0.681000, param_4: 0.293000, param_5: 0.704000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1647")
