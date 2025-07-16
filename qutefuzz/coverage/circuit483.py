from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_3[0],qreg_1[1])
subcirc0.u(pi/2,0.399000,-0.496000, qreg_1[1])
subcirc0.cz(qreg_1[1],qreg_1[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.rz(-0.771000, qreg_1[0])
subcirc0.cy(qreg_0[0],qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.rz(0.665000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,0.685000,-0.473000, qreg_1[0])
subcirc2.cz(qreg_2[0],qreg_0[0])
subcirc2.cy(qreg_2[1],qreg_0[0])
subcirc2.u(pi/2,0.141000,-0.835000, qreg_2[0])
subcirc2.cy(qreg_2[0],qreg_2[1])
subcirc2.cz(qreg_0[0],qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cy(qreg_0[1],qreg_0[0])
subcirc3.u(pi/2,0.343000,0.600000, qreg_0[0])
subcirc3.rz(0.724000, qreg_2[0])
subcirc3.cy(qreg_0[1],qreg_2[1])
subcirc3.rz(0.053000, qreg_0[0])
subcirc3.cy(qreg_2[0],qreg_2[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cy(qreg_0[1],qreg_0[2])
subcirc4.rz(-0.695000, qreg_0[0])
subcirc4.cy(qreg_0[1],qreg_0[2])
subcirc4.rz(-0.352000, qreg_0[2])
subcirc4.u(pi/2,0.773000,0.156000, qreg_0[0])
subcirc4.u(pi/2,0.591000,-0.028000, qreg_0[2])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.rz(param_0, qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[3])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.append(subcirc4,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.rz(param_1, qreg_0[3])
main_circ.u(pi/2,param_2,param_2, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2]])
main_circ.rz(param_0, qreg_0[2])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.append(subcirc4,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.append(subcirc4,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.rz(0.169000, qreg_0[2])
bindings = {param_0: -0.758000, param_1: 0.132000, param_2: 0.301000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "483")
