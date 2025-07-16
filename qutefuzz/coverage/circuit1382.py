from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.rx(-0.203000, qreg_1[0])
subcirc0.u(pi/2,0.408000,0.182000, qreg_1[1])
subcirc0.y(qreg_1[2])
subcirc0.u(pi/2,-0.664000,0.063000, qreg_1[2])
subcirc0.cy(qreg_0[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.cy(qreg_0[3],qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.rx(0.665000, qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.y(qreg_0[2])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,3])
main_circ.cy(0,qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],2,3,0])
main_circ.append(subcirc1,[qreg_0[1],2,qreg_0[0],3,1,0])
main_circ.append(subcirc1,[0,3,qreg_0[0],1,2,qreg_0[1]])
main_circ.append(subcirc1,[0,2,qreg_0[1],qreg_0[0],1,3])
main_circ.y(2)
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],1,0,3,2])
main_circ.append(subcirc1,[1,0,2,qreg_0[1],qreg_0[0],3])
main_circ.y(3)
main_circ.append(subcirc1,[qreg_0[1],1,0,qreg_0[0],2,3])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],1,2,0,3])
main_circ.u(pi/2,param_4,0.021000, 2)
main_circ.append(subcirc1,[3,qreg_0[1],qreg_0[0],2,0,1])
main_circ.u(pi/2,-0.959000,0.237000, qreg_0[0])
main_circ.cy(0,qreg_0[1])
main_circ.rx(-0.300000, 3)
main_circ.u(pi/2,0.326000,param_3, 1)
main_circ.cy(2,0)
main_circ.u(pi/2,param_3,-0.817000, 1)
bindings = {param_3: -0.881000, param_4: 0.331000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1382")
