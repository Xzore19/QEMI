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
subcirc0.s(qreg_0[1])
subcirc0.u(pi/2,-0.928000,-0.163000, qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.s(qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.rz(param_1, qreg_1[2])
main_circ.s(qreg_0[0])
main_circ.s(qreg_1[2])
main_circ.y(qreg_1[0])
main_circ.rz(0.077000, qreg_1[1])
main_circ.u(param_0,0.529000,param_1, qreg_1[2])
main_circ.rz(param_0, qreg_1[2])
main_circ.u(param_2,param_1,param_0, qreg_1[0])
main_circ.u(pi/2,-0.033000,param_2, qreg_1[2])
main_circ.u(pi/2,0.353000,0.921000, qreg_1[1])
main_circ.y(qreg_1[0])
main_circ.y(qreg_1[2])
main_circ.y(qreg_0[0])
main_circ.rz(0.804000, qreg_1[0])
main_circ.y(qreg_1[2])
main_circ.s(qreg_1[2])
main_circ.u(pi/2,param_2,-0.839000, qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
main_circ.u(param_1,0.502000,-0.720000, qreg_0[0])
main_circ.rz(-0.694000, qreg_0[0])
main_circ.u(param_2,param_1,0.693000, qreg_0[0])
main_circ.y(qreg_1[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.y(qreg_1[2])
main_circ.rz(0.878000, qreg_1[0])
main_circ.s(qreg_1[0])
main_circ.y(qreg_1[1])
main_circ.y(qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[2],qreg_0[0],qreg_1[1]])
main_circ.y(qreg_1[2])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_1[2],qreg_1[1]])
main_circ.append(subcirc0,[qreg_1[2],qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.rz(param_1, qreg_1[0])
main_circ.u(pi/2,param_2,param_1, qreg_0[0])
main_circ.y(qreg_1[0])
main_circ.u(pi/2,-0.009000,param_3, qreg_0[0])
main_circ.rz(0.182000, qreg_1[0])
bindings = {param_0: 0.111000, param_1: -0.614000, param_2: 0.027000, param_3: -0.077000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1134")
