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
subcirc0.s(qreg_0[1])
subcirc0.cy(qreg_0[2],qreg_0[3])
subcirc0.rz(-0.527000, qreg_0[3])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.rz(-0.190000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[1],qreg_0[3])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_2[0])
subcirc2.s(qreg_3[0])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.rz(-0.483000, qreg_3[0])
subcirc2.s(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.rz(0.565000, qreg_0[3])
subcirc3.s(qreg_0[2])
subcirc3.cz(qreg_0[0],qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cy(1,0)
main_circ.append(subcirc2,[2,1,0,3])
main_circ.s(2)
main_circ.append(subcirc1,[2,0,1,3])
main_circ.append(subcirc3,[0,3,2,1])
main_circ.append(subcirc3,[1,3,2,0])
main_circ.append(subcirc2,[1,0,3,2])
main_circ.append(subcirc2,[3,0,1,2])
main_circ.cy(0,1)
main_circ.rz(-0.004000, 1)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.cz(2,3)
main_circ.cy(3,0)
main_circ.s(1)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "236")
