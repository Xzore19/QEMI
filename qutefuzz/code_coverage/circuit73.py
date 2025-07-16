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
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.u(0,0,-0.990000, qreg_0[0])
subcirc0.ry(-0.255000, qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0.ry(-0.394000, qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.s(qreg_2[0])
subcirc1.ry(-0.225000, qreg_2[0])
subcirc1.cx(qreg_0[0],qreg_2[0])
subcirc1.u(0,0,-0.769000, qreg_2[0])
subcirc1.ry(0.105000, qreg_2[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_2,0,-0.362000, qreg_1[1])
main_circ.ry(param_2, qreg_1[1])
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.ry(-0.674000, qreg_3[0])
main_circ.u(param_2,0,param_2, 0)
main_circ.u(0,param_2,0.743000, qreg_1[1])
main_circ.append(subcirc1,[qreg_0[0],1,qreg_1[1],0])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],0,1])
main_circ.s(qreg_0[0])
main_circ.s(0)
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.u(param_0,param_1,0.270000, qreg_1[1])
main_circ.cx(qreg_1[1],0)
main_circ.append(subcirc0,[1,0,qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.s(1)
main_circ.ry(-0.105000, 0)
main_circ.ry(param_2, qreg_1[0])
main_circ.append(subcirc1,[0,1,qreg_0[0],qreg_1[1]])
main_circ.ry(param_1, qreg_1[1])
main_circ.cx(qreg_0[0],qreg_1[1])
main_circ.cx(qreg_1[0],1)
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_0[0],1)
main_circ.cx(qreg_3[0],qreg_1[0])
main_circ.cx(0,qreg_1[1])
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.cx(qreg_1[1],qreg_1[0])
main_circ.cx(qreg_1[0],0)
main_circ.cx(0,qreg_0[0])
main_circ.u(0,0,-0.369000, qreg_3[0])
main_circ.u(0,param_1,0.223000, qreg_3[0])
main_circ.s(0)
main_circ.ry(param_1, qreg_0[0])
main_circ.u(0,0,-0.209000, qreg_0[0])
main_circ.ry(-0.378000, qreg_3[0])
bindings = {param_0: 0.841000, param_1: -0.948000, param_2: 0.984000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "73")
