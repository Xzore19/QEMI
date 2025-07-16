from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.x(qreg_0[0])
subcirc0.u(pi/2,-0.668000,-0.869000, qreg_0[1])
subcirc0.u(0,0,-0.355000, qreg_2[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[1])
subcirc0.u(pi/2,-0.334000,-0.099000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.087000,0.488000, qreg_3[0])
subcirc1.u(0,0,0.303000, qreg_3[0])
subcirc1.u(0,0,-0.290000, qreg_0[0])
subcirc1.u(pi/2,-0.665000,-0.881000, qreg_0[0])
subcirc1.u(pi/2,-0.686000,-0.951000, qreg_3[0])
subcirc1.u(0,0,-0.959000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

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
param_5 = Parameter("param_5")

main_circ.cz(qreg_0[3],0)
main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.x(qreg_0[1])
main_circ.u(param_4,0,param_1, qreg_0[3])
main_circ.cz(0,qreg_0[2])
main_circ.x(qreg_0[3])
main_circ.append(subcirc0,[qreg_0[3],0,qreg_0[1],qreg_0[0]])
main_circ.x(qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.cz(0,qreg_0[3])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.u(param_1,0,param_3, qreg_0[1])
main_circ.x(0)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[1],0)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.u(param_2,param_0,param_3, 0)
main_circ.u(param_0,param_0,param_1, qreg_0[0])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.cz(qreg_0[3],0)
main_circ.u(pi/2,-0.614000,param_3, qreg_0[0])
bindings = {param_0: -0.257000, param_1: 0.629000, param_2: -0.294000, param_3: 0.151000, param_4: -0.280000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesSimpleCommutation")
