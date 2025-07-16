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
subcirc0.u(0,0,-0.549000, qreg_3[0])
subcirc0.u(0,0,0.792000, qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0.u(0,0,-0.319000, qreg_3[0])
subcirc0.z(qreg_0[0])
subcirc0.ry(0.854000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.ry(0.964000, qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.u(0,0,0.780000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_1[1])
subcirc2.z(qreg_1[1])
subcirc2.ry(0.161000, qreg_1[0])
subcirc2.z(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[1])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_3[0])
subcirc3.ry(-0.470000, qreg_0[0])
subcirc3.z(qreg_2[0])
subcirc3.x(qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,0.767000, qreg_3[0])
subcirc4.z(qreg_0[0])
subcirc4.ry(0.142000, qreg_0[0])
subcirc4.x(qreg_0[2])
subcirc4.ry(0.049000, qreg_0[0])
subcirc4.ry(0.326000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.z(0)
main_circ.ry(-0.404000, 0)
main_circ.x(2)
main_circ.append(subcirc2,[2,0,qreg_0[0],3,1])
main_circ.x(2)
main_circ.u(0,0,-0.882000, 2)
main_circ.append(subcirc4,[qreg_0[0],0,1,2])
main_circ.x(qreg_0[0])
main_circ.append(subcirc3,[2,1,3,0])
main_circ.z(1)
main_circ.x(0)
main_circ.append(subcirc4,[qreg_0[0],0,1,3])
main_circ.append(subcirc2,[qreg_0[0],0,3,2,1])
main_circ.z(0)
main_circ.append(subcirc4,[0,qreg_0[0],1,3])
main_circ.ry(param_1, 2)
bindings = {param_1: 0.714000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
