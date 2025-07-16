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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.x(qreg_0[3])
subcirc0.rz(0.641000, qreg_0[2])
subcirc0.x(qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.x(qreg_0[0])
subcirc1.rz(-0.789000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

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
subcirc2.rz(-0.652000, qreg_0[0])
subcirc2.rx(-0.834000, qreg_3[0])
subcirc2.rx(-0.389000, qreg_2[0])
subcirc2.cx(qreg_3[0],qreg_2[0])
subcirc2.x(qreg_2[0])
subcirc2.rx(0.938000, qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_3[0],qreg_1[0])
subcirc3.rz(0.160000, qreg_1[0])
subcirc3.rz(-0.901000, qreg_1[0])
subcirc3.cx(qreg_1[1],qreg_0[0])
subcirc3.rx(-0.243000, qreg_1[1])
subcirc3.x(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cx(2,0)
main_circ.rx(0.147000, 2)
main_circ.cx(3,0)
main_circ.rz(0.503000, 3)
main_circ.x(2)
main_circ.rz(-0.181000, 2)
main_circ.rx(0.153000, 2)
main_circ.x(3)
main_circ.rz(-0.826000, 0)
main_circ.cx(0,3)
main_circ.rx(param_0, 2)
main_circ.append(subcirc2,[2,1,3,0])
main_circ.append(subcirc2,[2,1,0,3])
main_circ.x(2)
main_circ.rz(0.092000, 0)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.cx(0,2)
main_circ.cx(0,1)
main_circ.cx(1,0)
main_circ.cx(2,3)
main_circ.cx(1,2)
main_circ.cx(3,1)
main_circ.cx(3,2)
main_circ.append(subcirc2,[3,2,1,0])
bindings = {param_0: 0.547000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
