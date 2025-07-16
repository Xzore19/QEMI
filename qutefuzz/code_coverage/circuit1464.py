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
subcirc0.rz(-0.812000, qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_1[1])
subcirc0.rz(0.850000, qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(-0.996000, qreg_1[1])
subcirc1.rz(-0.104000, qreg_3[0])
subcirc1.ry(-0.359000, qreg_1[0])
subcirc1.u(0,0,-0.342000, qreg_1[0])
subcirc1.u(0,0,-0.122000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.ry(0.209000, qreg_0[1])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_0[3])
subcirc2.cx(qreg_0[3],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[0],qreg_3[0])
subcirc3.cx(qreg_0[0],qreg_3[0])
subcirc3.rz(0.968000, qreg_0[2])
subcirc3.u(0,0,0.475000, qreg_0[0])
subcirc3.rz(0.275000, qreg_0[2])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.rz(0.541000, 1)
main_circ.append(subcirc3,[2,3,qreg_0[0],1])
main_circ.append(subcirc1,[2,3,1,0,qreg_0[0]])
main_circ.rz(param_5, 0)
main_circ.append(subcirc3,[2,qreg_0[0],0,1])
main_circ.append(subcirc1,[2,3,qreg_0[0],0,1])
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc1,[1,3,0,2,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],0,3,2])
main_circ.rz(-0.957000, 3)
main_circ.append(subcirc1,[1,qreg_0[0],2,3,0])
main_circ.cx(qreg_0[0],0)
main_circ.cx(1,2)
main_circ.cx(3,2)
main_circ.cx(qreg_0[0],2)
main_circ.cx(2,0)
main_circ.cx(2,1)
main_circ.cx(2,3)
main_circ.append(subcirc1,[1,qreg_0[0],3,2,0])
main_circ.u(param_3,0,0.946000, 1)
main_circ.u(0,0,0.982000, 2)
main_circ.ry(param_4, 3)
main_circ.ry(-0.745000, 2)
bindings = {param_3: -0.511000, param_4: -0.973000, param_5: -0.438000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
