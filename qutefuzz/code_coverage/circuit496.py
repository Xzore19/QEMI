from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(-0.954000, qreg_3[0])
subcirc0.y(qreg_0[1])
subcirc0.ry(-0.623000, qreg_3[0])
subcirc0.rx(0.027000, qreg_0[0])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cy(2,0)
main_circ.ry(-0.243000, 2)
main_circ.ry(0.885000, 3)
main_circ.rx(0.721000, 1)
main_circ.ry(-0.276000, 1)
main_circ.y(0)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.ry(1.000000, 2)
main_circ.y(0)
main_circ.ry(0.365000, 1)
main_circ.cy(1,0)
main_circ.y(1)
main_circ.y(1)
main_circ.rx(param_3, 1)
main_circ.y(1)
main_circ.rx(0.476000, 1)
main_circ.ry(param_3, 1)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.rx(param_0, 3)
main_circ.cy(2,1)
main_circ.cy(3,1)
main_circ.rx(0.624000, 1)
main_circ.y(2)
main_circ.append(subcirc0,[0,3,1,2])
main_circ.y(0)
main_circ.append(subcirc0,[2,1,0,3])
main_circ.cy(1,3)
main_circ.cy(0,1)
main_circ.cy(3,0)
main_circ.cy(0,3)
main_circ.cy(2,3)
main_circ.cy(0,1)
main_circ.cy(1,0)
main_circ.cy(2,3)
main_circ.cy(1,0)
main_circ.cy(2,1)
main_circ.cy(0,2)
main_circ.ry(param_0, 2)
main_circ.rx(0.705000, 0)
main_circ.cy(1,3)
bindings = {param_0: 0.587000, param_3: -0.357000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
