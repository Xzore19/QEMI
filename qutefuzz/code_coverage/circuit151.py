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
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.148000, qreg_0[0])
subcirc1.cy(qreg_2[0],qreg_2[1])
subcirc1.cx(qreg_1[0],qreg_2[0])
subcirc1.cy(qreg_0[0],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.864000, qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.cx(qreg_0[1],qreg_0[2])
subcirc2.ry(-0.411000, qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1],1,0])
main_circ.cy(0,qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],1,0,qreg_3[0]])
main_circ.rz(-0.502000, qreg_0[1])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.append(subcirc0,[qreg_0[2],1,qreg_0[1],0,qreg_3[0],qreg_0[0]])
main_circ.append(subcirc0,[1,qreg_3[0],qreg_0[1],0,qreg_0[2],qreg_0[0]])
main_circ.cy(1,qreg_3[0])
main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[1],1,qreg_3[0],qreg_0[0]])
main_circ.rz(param_1, qreg_0[1])
main_circ.cx(0,1)
main_circ.ry(-0.470000, qreg_0[0])
main_circ.ry(param_1, 1)
main_circ.rz(0.497000, qreg_0[2])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.append(subcirc2,[1,qreg_0[2],qreg_0[0],0])
main_circ.append(subcirc1,[0,1,qreg_0[1],qreg_0[2]])
main_circ.append(subcirc1,[1,qreg_0[1],0,qreg_0[0]])
main_circ.cy(qreg_0[2],1)
main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[0],qreg_3[0]])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.rz(param_0, qreg_0[1])
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_0[2],qreg_0[0])
bindings = {param_0: 0.085000, param_1: 0.663000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "151")
