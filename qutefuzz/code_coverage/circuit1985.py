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
subcirc0.u(0,0,-0.874000, qreg_0[3])
subcirc0.rx(-0.628000, qreg_0[3])
subcirc0.u(0,0,-0.971000, qreg_0[3])
subcirc0.u(0,0,0.452000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.997000, qreg_1[1])
subcirc1.h(qreg_3[0])
subcirc1.u(0,0,-0.332000, qreg_1[1])
subcirc1.rx(0.472000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.502000, qreg_0[2])
subcirc2.u(0,0,-0.419000, qreg_0[2])
subcirc2.u(0,0,0.394000, qreg_0[2])
subcirc2.rx(-0.017000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.868000, qreg_3[0])
subcirc3.u(0,0,-0.310000, qreg_1[1])
subcirc3.z(qreg_1[0])
subcirc3.z(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.u(0,0,0.561000, qreg_2[1])
subcirc4.rx(0.874000, qreg_0[0])
subcirc4.z(qreg_2[0])
subcirc4.u(0,0,-0.434000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc1,[3,0,qreg_1[0],qreg_0[0],2,1])
main_circ.append(subcirc0,[qreg_0[0],3,1,qreg_1[0],2,0])
main_circ.z(qreg_1[0])
main_circ.append(subcirc4,[1,qreg_1[0],2,3,qreg_0[0],0])
main_circ.append(subcirc3,[0,2,qreg_0[0],qreg_1[0],3])
main_circ.append(subcirc1,[qreg_1[0],0,2,1,3,qreg_0[0]])
main_circ.append(subcirc4,[qreg_0[0],2,3,1,0,qreg_1[0]])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[1,3,qreg_1[0],2,0,qreg_0[0]])
main_circ.append(subcirc2,[3,qreg_1[0],0,1])
main_circ.append(subcirc0,[1,0,2,qreg_1[0],qreg_0[0],3])
main_circ.append(subcirc2,[0,qreg_1[0],qreg_0[0],2])
main_circ.rx(param_1, 2)
main_circ.append(subcirc0,[qreg_0[0],2,3,0,qreg_1[0],1])
main_circ.append(subcirc0,[1,0,2,qreg_1[0],qreg_0[0],3])
main_circ.append(subcirc1,[2,qreg_1[0],qreg_0[0],3,1,0])
main_circ.rx(-0.022000, 3)
main_circ.h(3)
bindings = {param_1: 0.285000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1985")
