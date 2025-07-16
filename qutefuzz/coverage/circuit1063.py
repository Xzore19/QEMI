from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(0.111000, qreg_2[0])
subcirc0.cz(qreg_1[0],qreg_3[0])
subcirc0.rx(-0.065000, qreg_0[0])
subcirc0.rx(-0.374000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_2[0])
subcirc1.cx(qreg_2[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_2[0],qreg_0[0])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.x(qreg_0[1])
subcirc2.rx(0.631000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.cz(2,0)
main_circ.append(subcirc2,[3,qreg_0[1],qreg_0[0],2,0])
main_circ.append(subcirc2,[1,qreg_0[0],0,qreg_0[1],3])
main_circ.x(3)
main_circ.cz(3,1)
main_circ.append(subcirc2,[qreg_0[1],1,qreg_0[0],3,0])
main_circ.rx(0.862000, 3)
main_circ.append(subcirc1,[1,2,qreg_0[0],0,3,qreg_0[1]])
main_circ.cz(2,3)
main_circ.append(subcirc1,[0,1,2,qreg_0[1],qreg_0[0],3])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.rx(0.576000, 2)
main_circ.append(subcirc1,[1,qreg_0[0],2,3,qreg_0[1],0])
main_circ.x(1)
main_circ.x(2)
main_circ.append(subcirc2,[qreg_0[0],1,2,3,0])
main_circ.rx(0.363000, 1)
main_circ.x(qreg_0[1])
main_circ.cz(qreg_0[0],2)
main_circ.cx(qreg_0[1],2)
main_circ.rx(0.074000, 2)
main_circ.append(subcirc2,[qreg_0[0],3,1,0,2])
main_circ.rx(param_3, 1)
main_circ.append(subcirc2,[3,qreg_0[0],qreg_0[1],0,2])
main_circ.x(2)
main_circ.x(1)
main_circ.cz(qreg_0[1],0)
main_circ.cz(2,1)
bindings = {param_3: 0.730000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1063")
