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
subcirc0.ry(0.104000, qreg_0[1])
subcirc0.h(qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0.u(-0.606000,0.082000,-0.380000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.537000,0.500000,0.452000, qreg_0[1])
subcirc1.z(qreg_2[0])
subcirc1.h(qreg_3[0])
subcirc1.ry(0.835000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.ry(0.653000, qreg_1[1])
subcirc2.ry(0.349000, qreg_1[1])
subcirc2.h(qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.638000,-0.837000,0.939000, qreg_0[2])
subcirc3.ry(-0.559000, qreg_0[1])
subcirc3.u(0.189000,-0.776000,0.210000, qreg_0[2])
subcirc3.z(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.z(qreg_3[0])
subcirc4.u(0.632000,-0.239000,-0.961000, qreg_3[0])
subcirc4.u(-0.786000,-0.445000,-0.158000, qreg_1[0])
subcirc4.z(qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],2,3,0])
main_circ.append(subcirc1,[2,qreg_0[0],0,3,1])
main_circ.append(subcirc1,[2,3,0,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[3,1,qreg_0[1],0,2])
main_circ.append(subcirc2,[2,3,qreg_0[1],qreg_0[0],0,1])
main_circ.append(subcirc2,[qreg_0[0],2,qreg_0[1],1,0,3])
main_circ.append(subcirc2,[1,0,3,qreg_0[1],qreg_0[0],2])
main_circ.append(subcirc0,[qreg_0[0],2,1,3,0])
main_circ.append(subcirc1,[qreg_0[1],3,qreg_0[0],1,0])
main_circ.append(subcirc1,[0,2,1,3,qreg_0[1]])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
