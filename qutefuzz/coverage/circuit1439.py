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
subcirc0.ry(0.159000, qreg_0[2])
subcirc0.ry(0.165000, qreg_0[2])
subcirc0.y(qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.y(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.694000,0.461000, qreg_0[3])
subcirc1.y(qreg_0[2])
subcirc1.u(pi/2,-0.742000,-0.135000, qreg_0[3])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.y(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.856000, qreg_3[0])
subcirc2.u(pi/2,-0.323000,0.703000, qreg_1[0])
subcirc2.u(pi/2,0.474000,-0.376000, qreg_1[0])
subcirc2.y(qreg_1[0])
subcirc2.u(pi/2,0.363000,-0.300000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[1,qreg_3[0],qreg_0[1],0])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.y(1)
main_circ.y(qreg_0[2])
main_circ.ry(0.266000, qreg_0[2])
main_circ.u(pi/2,0.411000,param_1, qreg_0[1])
main_circ.y(1)
main_circ.append(subcirc1,[1,qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.y(qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[1])
main_circ.ry(param_1, 0)
main_circ.ry(param_1, qreg_0[0])
main_circ.append(subcirc1,[1,qreg_3[0],0,qreg_0[1]])
main_circ.y(0)
main_circ.ry(param_1, 1)
main_circ.u(pi/2,param_0,param_0, qreg_0[2])
main_circ.append(subcirc1,[0,qreg_0[1],1,qreg_0[0]])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_3[0],1)
main_circ.cz(qreg_0[2],1)
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[2],qreg_3[0])
main_circ.y(1)
main_circ.u(pi/2,param_1,-0.116000, 1)
main_circ.cz(qreg_0[2],qreg_0[0])
bindings = {param_0: 0.137000, param_1: 0.003000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1439")
