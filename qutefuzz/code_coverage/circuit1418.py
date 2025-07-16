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
subcirc0.s(qreg_2[0])
subcirc0.cz(qreg_0[1],qreg_2[0])
subcirc0.cz(qreg_2[0],qreg_3[0])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_1[0])
subcirc1.cy(qreg_1[1],qreg_1[0])
subcirc1.rx(0.002000, qreg_3[0])
subcirc1.cy(qreg_0[0],qreg_1[0])
subcirc1.cy(qreg_0[0],qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.rx(0.558000, qreg_0[0])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_1[1],qreg_0[0]])
main_circ.rx(-0.487000, qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_3[0],qreg_0[0]])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cy(qreg_1[1],qreg_1[0])
main_circ.append(subcirc1,[qreg_3[0],0,qreg_0[0],qreg_1[1]])
main_circ.cy(qreg_3[0],0)
main_circ.cy(qreg_1[1],qreg_3[0])
main_circ.rx(0.397000, qreg_3[0])
main_circ.s(qreg_1[0])
main_circ.s(qreg_3[0])
main_circ.s(qreg_3[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.cy(qreg_3[0],qreg_1[1])
main_circ.rx(param_1, qreg_1[0])
main_circ.cy(0,qreg_1[0])
main_circ.append(subcirc1,[qreg_3[0],0,qreg_1[0],qreg_0[0]])
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],0,qreg_1[1]])
main_circ.cz(qreg_0[0],0)
main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_1[1]])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_1[1],qreg_3[0]])
main_circ.s(qreg_3[0])
main_circ.cy(qreg_1[0],0)
bindings = {param_1: 0.694000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1418")
