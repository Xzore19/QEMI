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
subcirc0.cx(qreg_0[0],qreg_1[1])
subcirc0.cx(qreg_1[0],qreg_1[1])
subcirc0.cz(qreg_1[2],qreg_1[1])
subcirc0.cy(qreg_1[2],qreg_0[0])
subcirc0.ry(-0.441000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.991000, qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.ry(0.751000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.ry(0.355000, qreg_3[0])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[2],qreg_0[0])
subcirc3.ry(0.865000, qreg_0[0])
subcirc3.ry(-0.128000, qreg_0[2])
subcirc3.cy(qreg_0[3],qreg_0[0])
subcirc3.cz(qreg_0[0],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cx(qreg_2[0],qreg_3[0])
subcirc4.ry(0.764000, qreg_3[0])
subcirc4.cz(qreg_0[1],qreg_0[0])
subcirc4.cx(qreg_2[0],qreg_3[0])
subcirc4.cz(qreg_0[1],qreg_3[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc4,[qreg_0[0],3,1,qreg_1[0],2,0])
main_circ.append(subcirc2,[qreg_0[0],1,qreg_1[0],0,2,3])
main_circ.cy(2,1)
main_circ.append(subcirc1,[3,qreg_1[0],1,0])
main_circ.append(subcirc0,[qreg_1[0],0,1,3])
main_circ.append(subcirc4,[qreg_0[0],2,0,3,1,qreg_1[0]])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],2,3])
main_circ.cx(3,0)
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.ry(0.357000, qreg_0[0])
main_circ.cx(2,qreg_1[0])
main_circ.cz(1,3)
main_circ.append(subcirc4,[2,qreg_1[0],1,0,qreg_0[0],3])
main_circ.append(subcirc0,[2,qreg_0[0],3,0])
main_circ.cx(1,qreg_1[0])
main_circ.cz(2,qreg_0[0])
main_circ.cy(1,2)
main_circ.cz(qreg_0[0],qreg_1[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1351")
