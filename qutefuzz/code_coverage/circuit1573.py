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
subcirc0.z(qreg_1[1])
subcirc0.u(0,0,-0.160000, qreg_1[1])
subcirc0.ry(-0.354000, qreg_1[2])
subcirc0.ry(0.390000, qreg_0[0])
subcirc0.z(qreg_1[2])
subcirc0.ry(-0.579000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.ry(-0.301000, qreg_3[0])
subcirc1.u(0,0,-0.055000, qreg_3[0])
subcirc1.rz(0.156000, qreg_0[0])
subcirc1.ry(0.538000, qreg_0[1])
subcirc1.u(0,0,-0.086000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0,0,0.443000, qreg_0[0])
subcirc2.ry(0.852000, qreg_2[1])
subcirc2.ry(0.918000, qreg_2[1])
subcirc2.rz(-0.147000, qreg_2[0])
subcirc2.z(qreg_2[0])
subcirc2.z(qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_1[0])
subcirc3.z(qreg_2[1])
subcirc3.rz(-0.485000, qreg_2[1])
subcirc3.rz(-0.435000, qreg_0[0])
subcirc3.ry(-0.268000, qreg_2[0])
subcirc3.u(0,0,-0.273000, qreg_2[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.101000, qreg_0[0])
subcirc4.rz(-0.784000, qreg_0[2])
subcirc4.z(qreg_0[0])
subcirc4.u(0,0,0.909000, qreg_3[0])
subcirc4.z(qreg_0[0])
subcirc4.u(0,0,0.126000, qreg_3[0])

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
param_3 = Parameter("param_3")

main_circ.rz(param_0, qreg_1[0])
main_circ.ry(param_1, 0)
main_circ.ry(0.265000, 3)
main_circ.append(subcirc2,[3,2,1,0,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc4,[1,qreg_0[0],3,2])
main_circ.u(param_3,param_2,-0.968000, 0)
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],2,0,3,1])
main_circ.rz(param_1, qreg_0[0])
main_circ.append(subcirc2,[0,3,2,qreg_0[0],1,qreg_1[0]])
main_circ.rz(0.064000, 0)
main_circ.append(subcirc2,[3,0,1,2,qreg_1[0],qreg_0[0]])
main_circ.append(subcirc3,[3,qreg_0[0],qreg_1[0],1,2,0])
main_circ.append(subcirc3,[0,qreg_1[0],3,qreg_0[0],1,2])
main_circ.z(0)
main_circ.append(subcirc1,[2,0,1,qreg_1[0]])
main_circ.ry(param_1, 0)
main_circ.u(param_2,param_1,0.824000, 0)
bindings = {param_0: -0.048000, param_1: 0.851000, param_2: 0.607000, param_3: 0.714000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
