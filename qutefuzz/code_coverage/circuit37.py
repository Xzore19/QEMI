from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,-0.603000,-0.674000, qreg_0[0])
subcirc0.y(qreg_2[0])
subcirc0.u(0,0,0.813000, qreg_0[0])
subcirc0.y(qreg_2[1])
subcirc0.u(0,0,0.527000, qreg_2[1])
subcirc0.y(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_0[0])
subcirc1.u(0,0,-0.743000, qreg_0[1])
subcirc1.u(0,0,-0.763000, qreg_3[0])
subcirc1.ry(0.051000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.ry(-0.555000, qreg_0[0])
subcirc2.u(0,0,-0.292000, qreg_2[0])
subcirc2.u(0,0,0.351000, qreg_0[1])
subcirc2.u(pi/2,-0.516000,0.204000, qreg_2[1])
subcirc2.u(0,0,-0.841000, qreg_2[0])
subcirc2.u(0,0,-0.091000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(0.343000, qreg_0[2])
subcirc3.u(0,0,-0.986000, qreg_0[3])
subcirc3.u(0,0,0.271000, qreg_0[0])
subcirc3.u(pi/2,-0.569000,0.394000, qreg_0[1])
subcirc3.u(0,0,0.925000, qreg_0[2])
subcirc3.u(0,0,-0.874000, qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.u(pi/2,0.096000,-0.442000, qreg_0[0])
subcirc4.u(pi/2,0.261000,0.037000, qreg_1[2])
subcirc4.u(0,0,0.477000, qreg_1[2])
subcirc4.y(qreg_1[1])
subcirc4.y(qreg_1[2])
subcirc4.y(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.append(subcirc0,[0,qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.append(subcirc3,[0,qreg_1[0],qreg_2[0],qreg_0[0]])
main_circ.u(param_0,param_1,-0.717000, qreg_2[1])
main_circ.append(subcirc1,[0,qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.y(qreg_2[1])
main_circ.append(subcirc0,[0,qreg_1[0],qreg_2[0],qreg_2[1]])
main_circ.u(param_2,0,param_1, 0)
main_circ.u(param_1,param_2,param_0, qreg_0[0])
main_circ.append(subcirc4,[0,qreg_0[0],qreg_2[1],qreg_1[0],qreg_2[0]])
main_circ.u(0,param_2,param_2, qreg_0[0])
main_circ.append(subcirc3,[qreg_2[1],qreg_0[0],qreg_1[0],0])
main_circ.u(param_2,param_1,param_2, qreg_2[1])
main_circ.y(qreg_0[0])
main_circ.y(0)
main_circ.y(0)
main_circ.u(param_1,param_2,param_1, qreg_2[1])
main_circ.y(qreg_0[0])
main_circ.append(subcirc4,[qreg_1[0],qreg_2[0],qreg_2[1],0,qreg_0[0]])
bindings = {param_0: -0.153000, param_1: -0.012000, param_2: 0.129000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "37")
