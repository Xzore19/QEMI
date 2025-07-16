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
subcirc0.rz(-0.293000, qreg_0[1])
subcirc0.u(0,0,-0.875000, qreg_0[1])
subcirc0.u(0,0,0.517000, qreg_0[0])
subcirc0.u(0,0,0.929000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_2[1])
subcirc1.cy(qreg_0[1],qreg_2[0])
subcirc1.cy(qreg_2[1],qreg_0[0])
subcirc1.u(0,0,-0.862000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.rz(-0.687000, qreg_0[0])
subcirc2.u(0,0,0.492000, qreg_1[2])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.u(0,0,0.279000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(0.358000, qreg_2[1])
subcirc3.u(0,0,-0.337000, qreg_2[0])
subcirc3.cy(qreg_2[1],qreg_0[1])
subcirc3.cy(qreg_2[1],qreg_2[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rz(-0.949000, qreg_0[3])
subcirc4.cy(qreg_0[2],qreg_0[3])
subcirc4.rz(0.899000, qreg_0[1])
subcirc4.cy(qreg_0[1],qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc4,[0,qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.rz(-0.615000, qreg_1[0])
main_circ.rz(0.557000, qreg_0[0])
main_circ.u(param_2,0,0.796000, qreg_1[0])
main_circ.s(qreg_2[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_2[0],0])
main_circ.append(subcirc0,[qreg_2[0],0,qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.u(0,param_1,param_0, 0)
main_circ.append(subcirc4,[qreg_1[0],qreg_0[0],qreg_3[0],0])
main_circ.s(qreg_0[0])
main_circ.rz(param_1, 0)
main_circ.rz(param_1, 0)
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],0,qreg_2[0]])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.s(qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[0],qreg_0[0],0,qreg_3[0]])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.cy(qreg_1[0],qreg_2[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(0,qreg_3[0])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cy(qreg_3[0],0)
main_circ.cy(qreg_3[0],qreg_2[0])
main_circ.cy(qreg_3[0],0)
main_circ.rz(param_2, qreg_0[0])
main_circ.cy(0,qreg_1[0])
main_circ.rz(param_1, qreg_2[0])
main_circ.u(0,0,-0.580000, 0)
main_circ.rz(param_2, qreg_2[0])
bindings = {param_0: 0.344000, param_1: 0.057000, param_2: -0.689000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1394")
