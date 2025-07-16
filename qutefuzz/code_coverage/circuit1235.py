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
subcirc0.y(qreg_1[1])
subcirc0.rx(-0.178000, qreg_1[2])
subcirc0.rx(-0.337000, qreg_1[1])
subcirc0.rx(-0.893000, qreg_1[0])
subcirc0.cz(qreg_1[1],qreg_1[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.u(param_3,0,0.875000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],0,qreg_0[1]])
main_circ.u(param_1,param_3,0.509000, qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.rx(-0.690000, qreg_0[1])
main_circ.cz(0,qreg_0[3])
main_circ.rx(-0.270000, qreg_0[1])
main_circ.y(qreg_0[3])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.cz(0,qreg_0[0])
main_circ.rx(param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],0])
main_circ.cz(qreg_0[1],0)
main_circ.cz(0,qreg_0[3])
main_circ.cz(qreg_0[3],0)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(0,qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.rx(param_3, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],0])
bindings = {param_0: -0.962000, param_1: 0.946000, param_3: 0.667000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
