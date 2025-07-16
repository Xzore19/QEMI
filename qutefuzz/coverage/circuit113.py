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
subcirc0.u(0,0,0.755000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.rx(0.003000, qreg_3[0])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.359000, qreg_0[1])
subcirc1.u(0,0,-0.293000, qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0,0,-0.568000, qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2.u(0,0,0.651000, qreg_0[0])
subcirc2.u(0,0,0.797000, qreg_2[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_1[1],qreg_1[0])
subcirc3.u(0,0,-0.366000, qreg_3[0])
subcirc3.u(0,0,-0.768000, qreg_0[0])
subcirc3.rx(0.254000, qreg_3[0])

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
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[2,qreg_0[0],qreg_0[1],1,0,3])
main_circ.u(0,0,param_3, 1)
main_circ.cz(3,2)
main_circ.append(subcirc2,[3,2,qreg_0[1],1])
main_circ.append(subcirc3,[0,3,2,qreg_0[0]])
main_circ.cz(1,qreg_0[0])
main_circ.append(subcirc3,[1,qreg_0[0],qreg_0[1],3])
main_circ.rx(param_3, qreg_0[1])
main_circ.cz(qreg_0[1],2)
main_circ.append(subcirc0,[qreg_0[0],2,3,0,qreg_0[1],1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,3,2,1])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,2])
main_circ.append(subcirc3,[0,3,qreg_0[0],1])
main_circ.rx(param_4, 1)
main_circ.cz(1,qreg_0[0])
main_circ.cz(2,3)
main_circ.cz(qreg_0[1],2)
main_circ.cz(1,qreg_0[0])
main_circ.cz(1,0)
main_circ.cz(0,qreg_0[0])
main_circ.cz(2,3)
main_circ.cz(qreg_0[1],0)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],2)
main_circ.append(subcirc2,[3,qreg_0[0],qreg_0[1],1])
main_circ.rx(-0.772000, qreg_0[1])
main_circ.rx(param_2, 0)
main_circ.z(2)
bindings = {param_2: -0.836000, param_3: -0.084000, param_4: 0.950000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
