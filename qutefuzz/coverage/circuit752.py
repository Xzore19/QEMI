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
subcirc0.ry(-0.064000, qreg_0[0])
subcirc0.h(qreg_0[3])
subcirc0.ry(-0.487000, qreg_0[2])
subcirc0.rz(0.562000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.171000, qreg_1[0])
subcirc1.h(qreg_1[0])
subcirc1.h(qreg_2[0])
subcirc1.u(0,0,0.564000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.473000, qreg_3[0])
subcirc2.h(qreg_2[0])
subcirc2.ry(-0.661000, qreg_3[0])
subcirc2.ry(-0.602000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(-0.282000, qreg_0[0])
subcirc3.rz(-0.651000, qreg_2[1])
subcirc3.h(qreg_2[0])
subcirc3.u(0,0,-0.891000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.rz(0.049000, qreg_2[0])
subcirc4.u(0,0,-0.303000, qreg_0[1])
subcirc4.rz(0.319000, qreg_2[0])
subcirc4.ry(0.921000, qreg_2[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[0],0,qreg_0[2],1,qreg_3[0],qreg_0[1]])
main_circ.h(0)
main_circ.rz(param_2, 0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],1,qreg_0[2],qreg_0[1],0])
main_circ.u(param_0,0,-0.009000, qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.ry(-0.308000, 0)
main_circ.u(0,0,0.825000, qreg_0[2])
main_circ.ry(0.971000, 0)
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],1,qreg_3[0],qreg_0[2],0])
main_circ.rz(-0.567000, qreg_3[0])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[1],qreg_0[0],1,0,qreg_0[2]])
main_circ.u(param_0,param_0,param_2, qreg_0[2])
main_circ.u(param_1,0,-0.658000, 1)
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],1,qreg_0[0]])
main_circ.u(0,0,param_2, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,1])
main_circ.u(param_0,param_1,param_0, 0)
main_circ.u(param_1,0,param_1, qreg_0[1])
main_circ.h(qreg_3[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],qreg_0[1],1,qreg_0[2],0])
main_circ.rz(param_1, 0)
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_3[0]])
main_circ.ry(param_0, 0)
main_circ.u(param_1,0,param_2, 0)
bindings = {param_0: 0.976000, param_1: -0.957000, param_2: -0.391000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "752")
