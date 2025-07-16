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
subcirc0.ry(-0.585000, qreg_0[0])
subcirc0.ry(0.173000, qreg_0[0])
subcirc0.u(0.236000,-0.276000,0.613000, qreg_0[1])
subcirc0.rx(-0.578000, qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.104000, qreg_0[2])
subcirc1.rx(-0.222000, qreg_0[0])
subcirc1.z(qreg_0[2])
subcirc1.u(0.868000,0.166000,0.276000, qreg_0[0])
subcirc1.rx(0.991000, qreg_0[0])
subcirc1.ry(0.834000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.u(0.309000,param_0,0.947000, 3)
main_circ.append(subcirc0,[2,3,1,qreg_0[1],qreg_0[0],0])
main_circ.append(subcirc1,[0,1,qreg_0[1],3,qreg_0[0],2])
main_circ.append(subcirc1,[1,3,0,qreg_0[1],2,qreg_0[0]])
main_circ.z(0)
main_circ.ry(param_3, 1)
main_circ.z(0)
main_circ.rx(-0.551000, qreg_0[1])
main_circ.z(3)
main_circ.append(subcirc0,[qreg_0[1],2,3,qreg_0[0],1,0])
main_circ.z(3)
main_circ.rx(0.051000, 1)
main_circ.ry(param_2, 3)
main_circ.ry(0.286000, 3)
main_circ.ry(param_3, 2)
main_circ.z(0)
main_circ.z(0)
main_circ.z(2)
main_circ.rx(0.859000, 3)
main_circ.ry(param_1, 2)
main_circ.rx(param_1, 0)
main_circ.ry(param_1, 0)
main_circ.z(0)
main_circ.z(1)
bindings = {param_0: 0.267000, param_1: 0.665000, param_2: -0.525000, param_3: -0.013000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
