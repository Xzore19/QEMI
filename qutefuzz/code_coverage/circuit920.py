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
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_0[3],qreg_0[0])
subcirc0.ry(-0.471000, qreg_0[1])
subcirc0.ry(0.652000, qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.109000, qreg_2[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.ry(0.083000, qreg_3[0])
subcirc1.cy(qreg_3[0],qreg_2[0])
subcirc1.ry(-0.264000, qreg_2[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.ry(param_1, qreg_0[0])
main_circ.cz(0,qreg_0[3])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],0,qreg_0[3]])
main_circ.ry(-0.946000, 0)
main_circ.ry(0.615000, qreg_0[2])
main_circ.rx(param_2, 0)
main_circ.append(subcirc1,[0,qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[1],qreg_0[3]])
main_circ.cy(0,qreg_0[3])
main_circ.ry(-0.487000, qreg_0[3])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[3],qreg_0[1]])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[3],0])
main_circ.rx(0.512000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[2],0])
main_circ.rx(-0.926000, qreg_0[0])
main_circ.rx(-0.695000, qreg_0[3])
main_circ.cy(qreg_0[3],0)
main_circ.cz(qreg_0[1],qreg_0[3])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.cy(qreg_0[1],0)
bindings = {param_1: -0.078000, param_2: 0.027000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
