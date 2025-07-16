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
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0.u(pi/2,-0.830000,-0.742000, qreg_0[2])
subcirc0.cx(qreg_0[0],qreg_0[3])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.u(pi/2,-0.582000,-0.396000, qreg_0[3])
subcirc0.z(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.cz(qreg_0[1],qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.328000,0.709000, qreg_0[0])
subcirc2.u(pi/2,-0.439000,-0.757000, qreg_2[0])
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.cx(1,2)
main_circ.append(subcirc2,[2,1,3,0])
main_circ.cx(1,0)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.cx(3,0)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.u(param_4,0.708000,param_1, 2)
main_circ.cx(2,0)
main_circ.cz(0,3)
main_circ.cz(0,1)
main_circ.cz(1,3)
main_circ.cx(2,1)
main_circ.u(pi/2,-0.255000,param_3, 3)
main_circ.append(subcirc2,[3,0,1,2])
main_circ.u(pi/2,param_3,param_3, 1)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.cx(1,0)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.u(pi/2,0.501000,param_2, 1)
main_circ.z(3)
main_circ.u(pi/2,param_3,param_1, 0)
main_circ.cz(1,0)
main_circ.cz(0,2)
main_circ.z(2)
main_circ.cx(1,0)
bindings = {param_1: -0.502000, param_2: 0.139000, param_3: -0.962000, param_4: 0.675000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
