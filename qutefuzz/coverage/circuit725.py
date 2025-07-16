from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_0[2])
subcirc0.ry(0.944000, qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.ry(-0.225000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.ry(0.896000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_3[0])
subcirc2.h(qreg_0[1])
subcirc2.cy(qreg_0[1],qreg_0[0])
subcirc2.h(qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_0[2])
subcirc3.h(qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_3[0])
subcirc3.x(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc3,[3,2,0,1])
main_circ.append(subcirc2,[2,0,3,1])
main_circ.h(0)
main_circ.ry(-0.506000, 3)
main_circ.h(1)
main_circ.append(subcirc2,[0,1,3,2])
main_circ.h(1)
main_circ.cy(2,1)
main_circ.h(2)
main_circ.append(subcirc3,[3,2,0,1])
main_circ.append(subcirc3,[3,0,1,2])
main_circ.cy(3,0)
main_circ.h(2)
main_circ.ry(param_1, 2)
main_circ.cy(2,3)
main_circ.h(2)
main_circ.append(subcirc3,[1,3,2,0])
main_circ.append(subcirc2,[1,3,2,0])
main_circ.cy(3,0)
main_circ.cy(1,3)
main_circ.cy(0,3)
main_circ.cy(2,0)
main_circ.cy(2,0)
main_circ.cy(3,1)
main_circ.cy(0,2)
main_circ.x(3)
main_circ.append(subcirc3,[0,2,1,3])
main_circ.x(2)
main_circ.cy(1,2)
main_circ.ry(-0.691000, 0)
main_circ.x(2)
main_circ.ry(-0.117000, 3)
main_circ.h(1)
bindings = {param_1: -0.974000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
