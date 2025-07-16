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
subcirc0.ry(-0.696000, qreg_0[1])
subcirc0.ry(0.307000, qreg_2[0])
subcirc0.rx(0.379000, qreg_2[0])
subcirc0.rz(0.876000, qreg_0[1])
subcirc0.ry(-0.934000, qreg_2[0])

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

main_circ.rz(param_0, 2)
main_circ.ry(-0.775000, 0)
main_circ.ry(param_2, 2)
main_circ.ry(param_1, 0)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.append(subcirc0,[3,0,1,2])
main_circ.append(subcirc0,[2,3,1,0])
main_circ.rx(0.456000, 3)
main_circ.ry(-0.066000, 2)
main_circ.h(2)
main_circ.rz(-0.818000, 1)
main_circ.h(2)
main_circ.rx(-0.965000, 2)
main_circ.h(3)
main_circ.ry(0.488000, 1)
main_circ.append(subcirc0,[1,2,3,0])
main_circ.h(0)
main_circ.ry(param_1, 1)
main_circ.ry(-0.967000, 1)
main_circ.h(1)
main_circ.rx(param_1, 0)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.rx(0.150000, 1)
main_circ.rx(-0.375000, 3)
main_circ.rz(param_1, 2)
main_circ.ry(param_0, 2)
main_circ.h(0)
main_circ.rx(0.721000, 2)
main_circ.rx(param_1, 1)
main_circ.h(3)
main_circ.h(1)
main_circ.ry(param_1, 2)
main_circ.rx(0.991000, 3)
main_circ.ry(0.688000, 2)
main_circ.ry(param_2, 2)
main_circ.rz(-0.725000, 3)
bindings = {param_0: -0.493000, param_1: 0.386000, param_2: 0.623000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
