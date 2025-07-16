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
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.cy(qreg_0[1],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.h(qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0.313000,-0.111000,-0.653000, qreg_0[0])
subcirc2.cz(qreg_0[0],qreg_1[0])
subcirc2.cy(qreg_1[1],qreg_1[0])
subcirc2.cy(qreg_1[2],qreg_1[1])
subcirc2.h(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_0[1])
subcirc3.h(qreg_0[1])
subcirc3.u(-0.342000,-0.317000,-0.652000, qreg_0[1])
subcirc3.h(qreg_0[3])
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cz(qreg_0[0],qreg_0[1])
subcirc4.cz(qreg_0[1],qreg_2[0])
subcirc4.u(-0.871000,-0.407000,-0.540000, qreg_2[1])
subcirc4.cz(qreg_2[0],qreg_0[1])
subcirc4.cy(qreg_0[0],qreg_2[0])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.cz(2,3)
main_circ.u(param_5,0.640000,0.003000, 1)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.cz(1,0)
main_circ.u(param_5,param_4,param_0, 3)
main_circ.cz(2,1)
main_circ.cz(0,2)
main_circ.append(subcirc0,[1,2,3,0])
main_circ.cy(1,2)
main_circ.append(subcirc2,[3,2,1,0])
main_circ.cy(1,0)
main_circ.append(subcirc0,[2,1,0,3])
main_circ.cz(0,3)
main_circ.append(subcirc2,[3,1,0,2])
main_circ.h(2)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.append(subcirc4,[0,1,3,2])
main_circ.u(param_7,param_4,param_3, 0)
main_circ.append(subcirc4,[1,2,3,0])
main_circ.cz(1,0)
main_circ.cz(2,3)
main_circ.cz(1,2)
main_circ.cy(2,3)
main_circ.cy(3,1)
bindings = {param_0: 0.048000, param_3: -0.707000, param_4: -0.063000, param_5: 0.482000, param_7: -0.866000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
