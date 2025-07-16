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
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc0,[qreg_2[0],1,qreg_0[0],qreg_2[1]])
main_circ.cz(0,qreg_0[0])
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.cz(1,qreg_0[1])
main_circ.z(0)
main_circ.cz(qreg_2[0],0)
main_circ.z(0)
main_circ.cz(1,qreg_2[0])
main_circ.cx(qreg_2[0],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],1,qreg_0[0],0])
main_circ.u(pi/2,0.527000,param_3, qreg_2[0])
main_circ.u(param_3,0.615000,0.828000, qreg_2[0])
main_circ.cz(1,0)
main_circ.cz(qreg_2[0],qreg_2[1])
main_circ.cx(qreg_0[1],qreg_2[1])
main_circ.cz(qreg_2[1],1)
main_circ.append(subcirc0,[qreg_0[1],1,0,qreg_2[0]])
main_circ.cz(0,qreg_0[0])
main_circ.u(pi/2,-0.345000,param_4, 0)
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[0],qreg_0[1]])
main_circ.cz(qreg_2[1],1)
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[1],qreg_2[1])
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.u(param_5,-0.285000,param_4, qreg_0[0])
main_circ.cx(qreg_0[0],qreg_2[0])
main_circ.cx(qreg_2[1],qreg_0[1])
bindings = {param_3: -0.146000, param_4: 0.954000, param_5: 0.734000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
