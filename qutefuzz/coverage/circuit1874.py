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
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.s(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rz(param_3, qreg_0[0])
main_circ.rz(-0.612000, qreg_2[1])
main_circ.h(qreg_2[0])
main_circ.append(subcirc0,[qreg_0[1],0,qreg_2[1],1,qreg_2[0],qreg_0[0]])
main_circ.rz(param_3, qreg_2[1])
main_circ.rz(0.061000, qreg_2[0])
main_circ.append(subcirc0,[qreg_2[0],0,1,qreg_0[1],qreg_0[0],qreg_2[1]])
main_circ.s(qreg_0[0])
main_circ.rz(param_1, qreg_0[1])
main_circ.rz(param_0, qreg_2[1])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[1],1,qreg_0[0],qreg_2[0],0])
main_circ.rz(0.628000, 0)
main_circ.s(qreg_2[0])
main_circ.h(1)
main_circ.h(qreg_0[1])
main_circ.s(qreg_2[1])
main_circ.rz(-0.816000, qreg_0[1])
main_circ.s(qreg_2[1])
main_circ.h(qreg_2[0])
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[1],0)
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.cy(0,qreg_2[0])
main_circ.s(0)
main_circ.cy(qreg_2[1],1)
main_circ.h(qreg_0[0])
bindings = {param_0: 0.205000, param_1: -0.948000, param_3: -0.658000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
