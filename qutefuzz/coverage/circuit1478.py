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
subcirc0.rx(-0.398000, qreg_1[1])
subcirc0.cx(qreg_0[0],qreg_1[2])
subcirc0.cz(qreg_1[0],qreg_1[1])
subcirc0.cz(qreg_1[0],qreg_0[0])
subcirc0.rx(-0.959000, qreg_1[0])
subcirc0.cz(qreg_1[2],qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.681000, qreg_0[1])
subcirc1.rz(-0.872000, qreg_3[0])
subcirc1.rz(0.539000, qreg_0[1])
subcirc1.rx(-0.008000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.cx(qreg_3[0],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(-0.074000, qreg_0[1])
subcirc2.rz(-0.003000, qreg_0[2])
subcirc2.rx(0.224000, qreg_0[2])
subcirc2.rz(0.848000, qreg_0[3])
subcirc2.rz(0.808000, qreg_0[1])
subcirc2.cz(qreg_0[3],qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(0.567000, qreg_3[0])
subcirc3.rz(-0.380000, qreg_0[0])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.cx(qreg_3[0],qreg_0[1])
subcirc3.rx(-0.897000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_3[0],qreg_0[0])
subcirc4.rz(0.622000, qreg_1[0])
subcirc4.cx(qreg_1[1],qreg_1[0])
subcirc4.cx(qreg_1[1],qreg_1[0])
subcirc4.rz(-0.860000, qreg_1[1])
subcirc4.cx(qreg_1[0],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rx(param_1, 3)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.rx(-0.034000, 2)
main_circ.cz(0,3)
main_circ.cz(0,3)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.append(subcirc2,[0,2,1,3])
main_circ.cz(2,3)
main_circ.cx(0,3)
main_circ.cx(3,2)
main_circ.append(subcirc2,[3,1,0,2])
main_circ.cz(3,0)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.append(subcirc2,[0,2,1,3])
main_circ.cx(3,0)
main_circ.cx(1,3)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.rz(-0.924000, 1)
main_circ.cx(0,3)
main_circ.cx(2,1)
bindings = {param_1: -0.170000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1478")
