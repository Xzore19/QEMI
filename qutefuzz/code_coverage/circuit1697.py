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
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,-0.219000,-0.011000, qreg_0[3])
subcirc0.u(pi/2,0.669000,0.747000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.278000,0.611000,0.818000, qreg_1[1])
subcirc1.z(qreg_3[0])
subcirc1.u(0,0,-0.225000, qreg_3[0])
subcirc1.z(qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.u(0.952000,0.777000,0.112000, qreg_2[1])
subcirc2.u(0,0,0.430000, qreg_2[1])
subcirc2.z(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(0.909000,-0.276000,0.819000, qreg_2[1])
subcirc3.u(0,0,0.369000, qreg_1[0])
subcirc3.z(qreg_1[0])
subcirc3.z(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(pi/2,-0.172000,-0.298000, qreg_0[3])
subcirc4.u(pi/2,0.858000,0.443000, qreg_0[1])
subcirc4.u(0.347000,0.095000,-0.333000, qreg_0[2])
subcirc4.u(pi/2,-0.963000,0.315000, qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.u(param_0,0,param_0, qreg_0[1])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],0,qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[1],0,qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.z(qreg_0[0])
main_circ.u(pi/2,0.361000,param_0, qreg_0[1])
main_circ.append(subcirc2,[qreg_2[0],qreg_3[0],qreg_0[0],0,qreg_0[1]])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_2[0],0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],0,qreg_2[0]])
main_circ.u(param_0,0.258000,param_0, qreg_0[0])
main_circ.append(subcirc4,[qreg_2[0],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[1],0,qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.append(subcirc1,[0,qreg_3[0],qreg_2[0],qreg_0[1]])
main_circ.z(qreg_2[0])
main_circ.u(param_0,param_0,0.566000, qreg_0[0])
bindings = {param_0: 0.447000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
