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
subcirc0.ry(-0.816000, qreg_0[2])
subcirc0.ry(0.428000, qreg_0[2])
subcirc0.ry(0.442000, qreg_0[0])
subcirc0.rx(-0.575000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.807000, qreg_0[2])
subcirc1.u(0,0,0.540000, qreg_3[0])
subcirc1.u(0,0,-0.560000, qreg_0[2])
subcirc1.ry(0.150000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.u(0,0,0.901000, qreg_0[2])
subcirc2.ry(-0.281000, qreg_0[0])
subcirc2.rx(0.828000, qreg_0[0])

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

main_circ.z(1)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.rx(-0.514000, 2)
main_circ.u(0,0,0.210000, 2)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.append(subcirc2,[1,3,0,2])
main_circ.append(subcirc2,[3,1,2,0])
main_circ.rx(0.777000, 1)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.append(subcirc2,[1,0,2,3])
main_circ.u(0,0,param_0, 1)
main_circ.ry(param_0, 0)
main_circ.u(param_0,param_1,0.302000, 0)
main_circ.u(param_1,param_1,param_0, 1)
main_circ.z(3)
main_circ.append(subcirc1,[3,1,2,0])
main_circ.u(param_1,param_1,param_1, 3)
main_circ.u(0,param_0,0.525000, 1)
main_circ.z(2)
main_circ.ry(param_1, 0)
main_circ.rx(0.907000, 1)
main_circ.rx(param_0, 0)
main_circ.u(param_0,0,param_0, 2)
main_circ.ry(0.762000, 1)
main_circ.rx(0.952000, 3)
main_circ.u(0,param_0,param_0, 1)
main_circ.z(1)
main_circ.ry(-0.495000, 1)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.rx(0.563000, 0)
main_circ.u(0,0,-0.888000, 2)
bindings = {param_0: -0.251000, param_1: -0.356000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
