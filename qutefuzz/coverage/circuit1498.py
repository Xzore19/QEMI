from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_1[1])
subcirc0.y(qreg_1[1])
subcirc0.y(qreg_1[0])
subcirc0.h(qreg_0[0])
subcirc0.y(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.u(-0.086000,0.430000,-0.705000, qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.s(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_3[0])
subcirc2.y(qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.y(qreg_0[1])
subcirc2.s(qreg_0[0])
subcirc2.u(0.166000,0.487000,-0.109000, qreg_0[2])

main_circ = QuantumCircuit(2)
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

main_circ.h(qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.append(subcirc2,[qreg_0[3],1,qreg_0[0],qreg_0[1]])
main_circ.h(qreg_0[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[3],qreg_0[2],1])
main_circ.y(qreg_0[3])
main_circ.u(param_3,param_1,param_3, qreg_0[3])
main_circ.s(qreg_0[2])
main_circ.y(qreg_0[3])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[0],0,1,qreg_0[2]])
main_circ.y(qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],1,qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],1,qreg_0[3],0])
main_circ.y(qreg_0[3])
main_circ.y(qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.y(qreg_0[0])
bindings = {param_1: 0.753000, param_3: -0.195000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1498")
