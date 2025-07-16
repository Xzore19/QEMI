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
subcirc0.z(qreg_0[0])
subcirc0.rx(-0.200000, qreg_0[3])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.ry(-0.144000, qreg_0[2])
subcirc0.rx(-0.113000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.669000, qreg_0[2])
subcirc1.z(qreg_0[2])
subcirc1.rx(-0.200000, qreg_0[0])
subcirc1.ry(-0.776000, qreg_0[1])
subcirc1.z(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.203000, qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_3[0])
subcirc2.rx(-0.135000, qreg_3[0])
subcirc2.rx(0.707000, qreg_0[2])
subcirc2.z(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.150000, qreg_0[0])
subcirc3.rx(0.714000, qreg_3[0])
subcirc3.cy(qreg_3[0],qreg_0[2])
subcirc3.cy(qreg_0[2],qreg_3[0])
subcirc3.cy(qreg_0[1],qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.ry(-0.160000, 3)
main_circ.rx(param_4, 3)
main_circ.rx(-0.528000, 2)
main_circ.cy(3,2)
main_circ.ry(param_2, 1)
main_circ.ry(-0.626000, 0)
main_circ.append(subcirc2,[1,3,2,0])
main_circ.append(subcirc0,[0,3,1,2])
main_circ.ry(-0.169000, 3)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.z(1)
main_circ.rx(-0.373000, 1)
main_circ.rx(param_5, 0)
main_circ.append(subcirc2,[1,2,0,3])
main_circ.cy(3,2)
main_circ.cy(2,0)
main_circ.cy(1,3)
main_circ.cy(1,0)
main_circ.cy(1,0)
main_circ.cy(3,1)
main_circ.cy(1,0)
main_circ.z(1)
main_circ.cy(1,3)
main_circ.ry(param_3, 2)
main_circ.ry(-0.106000, 3)
bindings = {param_2: -0.355000, param_3: 0.662000, param_4: -0.498000, param_5: -0.331000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
