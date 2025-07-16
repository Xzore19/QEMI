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
subcirc0.u(pi/2,0.796000,-0.579000, qreg_0[0])
subcirc0.cz(qreg_1[0],qreg_1[1])
subcirc0.cx(qreg_1[0],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_1[2])
subcirc0.rx(0.081000, qreg_1[0])
subcirc0.u(pi/2,-0.432000,0.064000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_2[1])
subcirc1.rx(-0.074000, qreg_2[0])
subcirc1.u(pi/2,-0.935000,-0.563000, qreg_2[1])
subcirc1.u(pi/2,-0.522000,0.472000, qreg_0[0])
subcirc1.u(pi/2,-0.844000,-0.841000, qreg_0[1])
subcirc1.rx(-0.609000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.538000, qreg_0[1])
subcirc2.rx(0.335000, qreg_3[0])
subcirc2.cx(qreg_0[0],qreg_3[0])
subcirc2.rx(0.792000, qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_0[1])

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

main_circ.cx(qreg_1[0],1)
main_circ.append(subcirc2,[qreg_0[0],1,2,0])
main_circ.cx(3,0)
main_circ.cz(0,1)
main_circ.cz(qreg_1[0],1)
main_circ.append(subcirc1,[0,3,1,qreg_1[0],2])
main_circ.cx(3,0)
main_circ.rx(param_1, 0)
main_circ.rx(param_0, qreg_1[0])
main_circ.append(subcirc1,[2,0,3,qreg_1[0],1])
main_circ.u(pi/2,param_0,param_0, 3)
main_circ.append(subcirc2,[qreg_0[0],3,2,0])
main_circ.u(param_1,param_1,-0.054000, 3)
main_circ.rx(0.034000, 2)
main_circ.append(subcirc1,[0,qreg_0[0],qreg_1[0],1,3])
bindings = {param_0: 0.306000, param_1: -0.249000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
