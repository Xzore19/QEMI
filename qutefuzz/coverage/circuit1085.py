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
subcirc0.u(0,0,0.780000, qreg_1[1])
subcirc0.x(qreg_1[0])
subcirc0.u(0.395000,0.986000,-0.671000, qreg_1[1])
subcirc0.x(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.869000, qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.707000, qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_0[1])
subcirc2.x(qreg_0[3])
subcirc2.cx(qreg_0[3],qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.cx(2,0)
main_circ.x(2)
main_circ.cx(0,qreg_1[0])
main_circ.u(-0.193000,-0.636000,0.143000, 0)
main_circ.append(subcirc2,[3,2,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc0,[0,qreg_0[0],1,qreg_1[0]])
main_circ.append(subcirc1,[2,qreg_1[0],3,qreg_0[0],1])
main_circ.append(subcirc0,[qreg_1[0],2,qreg_0[0],3])
main_circ.append(subcirc1,[1,qreg_1[0],qreg_0[0],0,3])
main_circ.append(subcirc0,[0,qreg_0[0],3,1])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],0,1])
main_circ.cx(qreg_1[0],0)
main_circ.cx(1,qreg_1[0])
main_circ.cx(3,qreg_1[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_1[0],0)
main_circ.cx(qreg_0[0],0)
main_circ.u(-0.831000,0.918000,-0.483000, 1)
main_circ.x(qreg_0[0])
main_circ.x(1)
main_circ.u(param_0,param_1,-0.632000, 0)
main_circ.append(subcirc1,[qreg_0[0],0,3,2,qreg_1[0]])
bindings = {param_0: 0.320000, param_1: 0.461000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
