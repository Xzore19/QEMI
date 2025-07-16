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
subcirc0.u(pi/2,0.823000,0.714000, qreg_0[2])
subcirc0.y(qreg_0[1])
subcirc0.u(pi/2,-0.174000,-0.559000, qreg_0[3])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cy(qreg_1[0],qreg_1[2])
subcirc1.y(qreg_1[1])
subcirc1.y(qreg_1[0])
subcirc1.u(pi/2,0.879000,-0.884000, qreg_1[0])
subcirc1.cz(qreg_0[0],qreg_1[1])
subcirc1.y(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,0.848000,0.161000, qreg_2[1])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.cz(qreg_2[1],qreg_0[1])
subcirc2.u(pi/2,-0.331000,0.123000, qreg_0[1])
subcirc2.cz(qreg_0[1],qreg_2[1])
subcirc2.u(pi/2,-0.191000,0.570000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.cy(qreg_0[3],qreg_0[0])
subcirc3.cz(qreg_0[0],qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.cz(qreg_0[2],qreg_0[3])
subcirc3.y(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4.cy(qreg_0[1],qreg_0[2])
subcirc4.cz(qreg_0[3],qreg_0[1])
subcirc4.u(pi/2,0.358000,0.960000, qreg_0[2])
subcirc4.y(qreg_0[0])
subcirc4.u(pi/2,-0.655000,-0.064000, qreg_0[3])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.cy(qreg_0[0],0)
main_circ.append(subcirc0,[qreg_1[0],0,qreg_2[1],1,qreg_0[0],qreg_2[0]])
main_circ.y(1)
main_circ.u(pi/2,0.230000,param_2, qreg_2[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_1[0],qreg_2[0],qreg_2[1],1])
main_circ.u(pi/2,0.271000,-0.427000, qreg_2[0])
main_circ.append(subcirc3,[0,qreg_0[0],1,qreg_2[1],qreg_1[0]])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_2[0],qreg_1[0],1])
main_circ.append(subcirc1,[qreg_1[0],qreg_2[0],1,qreg_0[0]])
main_circ.cy(qreg_2[0],qreg_1[0])
main_circ.append(subcirc0,[1,qreg_0[0],0,qreg_2[1],qreg_2[0],qreg_1[0]])
main_circ.append(subcirc3,[0,qreg_2[0],qreg_2[1],qreg_1[0],qreg_0[0]])
main_circ.cz(qreg_1[0],qreg_2[1])
bindings = {param_2: 0.153000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
