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
subcirc0.rz(0.376000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(0.325000, qreg_0[2])
subcirc0.s(qreg_0[1])
subcirc0.cy(qreg_3[0],qreg_0[2])
subcirc0.rz(0.182000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.rz(-0.658000, qreg_0[2])
subcirc1.rz(-0.522000, qreg_0[0])
subcirc1.rz(0.299000, qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.x(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.420000, qreg_3[0])
subcirc2.x(qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2.rz(0.158000, qreg_2[0])
subcirc2.cy(qreg_0[1],qreg_3[0])
subcirc2.cy(qreg_3[0],qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[2])
subcirc3.cy(qreg_0[1],qreg_0[2])
subcirc3.rz(0.809000, qreg_0[2])
subcirc3.rz(0.849000, qreg_0[0])
subcirc3.x(qreg_0[2])
subcirc3.rz(-0.291000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.s(qreg_0[1])
subcirc4.x(qreg_0[0])
subcirc4.rz(-0.734000, qreg_0[0])
subcirc4.cy(qreg_0[0],qreg_0[2])
subcirc4.rz(-0.973000, qreg_0[2])
subcirc4.s(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(2)
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

main_circ.x(qreg_0[0])
main_circ.cy(0,qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.append(subcirc4,[qreg_0[3],0,1,qreg_0[1],qreg_0[2]])
main_circ.s(qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.x(0)
main_circ.cy(qreg_0[1],1)
main_circ.rz(-0.647000, 1)
main_circ.append(subcirc4,[qreg_0[2],qreg_0[1],qreg_0[0],1,qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],1,qreg_0[0],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc4,[0,qreg_0[0],qreg_0[1],qreg_0[3],1])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.cy(1,qreg_0[3])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.cy(1,qreg_0[3])
main_circ.cy(0,qreg_0[2])
main_circ.cy(1,qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[3])
main_circ.cy(1,qreg_0[2])
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1774")
