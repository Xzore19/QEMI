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
subcirc0.s(qreg_0[1])
subcirc0.u(0.758000,-0.778000,-0.827000, qreg_0[3])
subcirc0.u(0,0,-0.247000, qreg_0[1])
subcirc0.u(0.659000,0.973000,-0.876000, qreg_0[2])
subcirc0.u(pi/2,0.381000,-0.465000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.754000,-0.478000, qreg_3[0])
subcirc1.u(pi/2,-0.030000,0.370000, qreg_2[0])
subcirc1.u(0,0,0.801000, qreg_0[1])
subcirc1.u(pi/2,-0.247000,0.674000, qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.070000,-0.200000,-0.142000, qreg_0[1])
subcirc2.s(qreg_0[2])
subcirc2.s(qreg_0[2])
subcirc2.u(0.945000,-0.924000,0.912000, qreg_0[1])
subcirc2.u(0,0,0.118000, qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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

main_circ.s(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[0],0,qreg_1[1]])
main_circ.u(pi/2,-0.220000,-0.864000, qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],1,qreg_1[2],qreg_0[0]])
main_circ.u(-0.469000,param_1,-0.517000, qreg_1[1])
main_circ.s(0)
main_circ.s(1)
main_circ.s(qreg_1[0])
main_circ.u(param_3,0.619000,param_5, qreg_1[0])
main_circ.append(subcirc2,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.u(param_5,0,param_5, qreg_0[0])
main_circ.s(0)
main_circ.u(pi/2,param_5,-0.926000, qreg_1[0])
main_circ.append(subcirc0,[1,qreg_1[0],qreg_1[1],0])
main_circ.u(param_4,param_0,0.045000, qreg_1[1])
main_circ.append(subcirc2,[qreg_1[0],qreg_1[2],qreg_0[0],qreg_1[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[2],1,qreg_1[0]])
main_circ.u(0.085000,param_5,-0.875000, qreg_1[2])
main_circ.u(pi/2,0.423000,param_1, qreg_0[0])
main_circ.u(0.788000,param_3,0.217000, qreg_1[1])
main_circ.s(qreg_1[2])
bindings = {param_0: -0.818000, param_1: 0.996000, param_3: 0.040000, param_4: 0.851000, param_5: -0.018000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "375")
