from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_1[0])
subcirc0.u(-0.856000,0.392000,-0.523000, qreg_2[0])
subcirc0.u(0.503000,0.430000,0.713000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.737000,0.830000,0.249000, qreg_0[1])
subcirc1.z(qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.z(qreg_3[0])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.u(-0.791000,0.583000,-0.042000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.z(qreg_0[3])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.h(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cy(qreg_3[0],qreg_2[0])
subcirc4.cy(qreg_2[0],qreg_0[0])
subcirc4.cy(qreg_2[0],qreg_3[0])
subcirc4.z(qreg_0[0])
subcirc4.cy(qreg_2[0],qreg_1[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.h(2)
main_circ.z(0)
main_circ.h(1)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.append(subcirc0,[0,3,1,2])
main_circ.h(3)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.z(2)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.append(subcirc0,[1,3,2,0])
main_circ.z(2)
main_circ.cy(0,2)
main_circ.u(param_2,0.601000,-0.262000, 2)
main_circ.h(2)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.cy(3,2)
main_circ.cy(1,3)
main_circ.append(subcirc2,[3,0,2,1])
main_circ.cy(1,2)
main_circ.u(param_0,-0.046000,param_0, 0)
main_circ.cy(1,0)
main_circ.append(subcirc2,[1,0,2,3])
main_circ.h(0)
main_circ.cy(1,2)
main_circ.cy(0,3)
main_circ.h(2)
main_circ.cy(2,3)
main_circ.cy(3,2)
bindings = {param_0: 0.196000, param_2: -0.442000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
