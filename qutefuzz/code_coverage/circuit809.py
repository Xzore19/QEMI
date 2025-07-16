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
subcirc0.ry(-0.805000, qreg_1[2])
subcirc0.ry(0.840000, qreg_1[0])
subcirc0.ry(-0.108000, qreg_1[0])
subcirc0.u(0,0,0.843000, qreg_1[0])
subcirc0.x(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.098000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.u(0,0,-0.768000, qreg_0[1])
subcirc1.ry(-0.085000, qreg_0[0])
subcirc1.s(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(-0.328000, qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.u(0,0,0.503000, qreg_0[3])
subcirc2.u(0,0,-0.682000, qreg_0[2])
subcirc2.u(0,0,0.814000, qreg_0[0])

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

main_circ.append(subcirc1,[2,3,1,0])
main_circ.x(2)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.ry(-0.487000, 2)
main_circ.ry(0.434000, 2)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.append(subcirc0,[1,3,0,2])
main_circ.u(0,0,param_0, 0)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.x(3)
main_circ.ry(param_0, 3)
main_circ.s(1)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.u(param_2,0,0.498000, 0)
main_circ.x(3)
main_circ.x(0)
main_circ.ry(param_0, 0)
bindings = {param_0: -0.617000, param_2: -0.193000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
