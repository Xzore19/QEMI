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
subcirc0.u(pi/2,0.119000,-0.336000, qreg_0[2])
subcirc0.u(-0.786000,0.424000,0.079000, qreg_0[1])
subcirc0.u(pi/2,0.083000,-0.188000, qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[2])
subcirc0.u(-0.936000,-0.277000,0.768000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,0.333000,0.423000, qreg_2[0])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.u(0.506000,0.353000,0.140000, qreg_2[1])
subcirc1.u(-0.708000,0.260000,-0.808000, qreg_2[1])
subcirc1.cy(qreg_1[0],qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.693000,-0.321000,0.280000, qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2.u(-0.653000,0.151000,-0.113000, qreg_0[0])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.u(pi/2,0.067000,-0.014000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cy(qreg_2[0],qreg_0[1])
subcirc3.z(qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_0[0])
subcirc3.u(-0.603000,-0.881000,0.773000, qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.u(-0.400000,-0.024000,-0.331000, qreg_2[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.436000,0.255000,0.931000, qreg_1[1])
subcirc4.u(pi/2,0.570000,-0.983000, qreg_1[1])
subcirc4.u(-0.013000,-0.803000,0.717000, qreg_3[0])
subcirc4.cy(qreg_1[0],qreg_3[0])
subcirc4.cy(qreg_3[0],qreg_1[0])
subcirc4.z(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.z(0)
main_circ.append(subcirc2,[qreg_2[0],0,qreg_0[0],qreg_0[1]])
main_circ.u(pi/2,param_5,-0.058000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.z(qreg_0[0])
main_circ.u(param_0,param_1,param_3, qreg_2[1])
main_circ.cy(qreg_2[1],0)
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
main_circ.append(subcirc3,[qreg_0[1],0,qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.u(param_3,-0.731000,-0.520000, 0)
main_circ.z(qreg_2[0])
main_circ.u(param_4,param_0,-0.518000, 0)
main_circ.u(pi/2,param_2,-0.383000, qreg_0[1])
main_circ.u(pi/2,param_2,-0.459000, qreg_2[1])
main_circ.u(0.166000,-0.245000,param_2, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[1],0,qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.cy(0,qreg_0[1])
main_circ.cy(qreg_2[1],0)
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.z(qreg_2[1])
main_circ.u(param_2,-0.391000,-0.750000, qreg_0[0])
main_circ.u(param_1,-0.530000,0.733000, qreg_2[1])
main_circ.z(qreg_0[0])
main_circ.u(pi/2,0.968000,-0.428000, qreg_2[1])
main_circ.z(qreg_0[0])
bindings = {param_0: -0.505000, param_1: -0.052000, param_2: -0.491000, param_3: 0.281000, param_4: 0.179000, param_5: 0.251000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
