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
subcirc0.cy(qreg_0[0],qreg_0[3])
subcirc0.s(qreg_0[2])
subcirc0.rz(-0.015000, qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.rz(0.065000, qreg_0[3])
subcirc0.s(qreg_0[3])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.rz(0.128000, qreg_0[3])
main_circ.s(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.rz(param_1, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.s(qreg_0[1])
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.s(qreg_0[0])
main_circ.rz(0.564000, qreg_0[2])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.u(0,param_2,param_1, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
main_circ.rz(-0.686000, qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.rz(0.834000, qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.rz(0.955000, qreg_0[0])
main_circ.u(0,param_0,param_0, qreg_0[2])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
bindings = {param_0: 0.669000, param_1: -0.498000, param_2: -0.827000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
