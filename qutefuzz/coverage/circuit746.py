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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_3[0])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cy(qreg_3[0],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.ry(param_1, 0)
main_circ.ry(param_1, 2)
main_circ.ry(param_0, 2)
main_circ.ry(param_1, 2)
main_circ.y(3)
main_circ.y(0)
main_circ.cy(3,0)
main_circ.y(3)
main_circ.ry(param_0, 2)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.y(1)
main_circ.cy(2,1)
main_circ.ry(param_0, 0)
main_circ.y(2)
main_circ.cy(2,0)
main_circ.cy(1,3)
main_circ.cx(0,1)
main_circ.ry(-0.392000, 1)
main_circ.cx(2,1)
main_circ.ry(param_0, 0)
main_circ.ry(0.077000, 3)
main_circ.ry(param_1, 1)
main_circ.y(0)
main_circ.cx(2,1)
main_circ.ry(-0.334000, 3)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.append(subcirc0,[2,3,0,1])
main_circ.ry(0.258000, 2)
main_circ.ry(param_1, 2)
main_circ.y(3)
main_circ.cy(2,1)
main_circ.y(1)
main_circ.y(2)
main_circ.ry(-0.606000, 1)
bindings = {param_0: -0.681000, param_1: -0.682000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
