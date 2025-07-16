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
subcirc0.ry(-0.884000, qreg_3[0])
subcirc0.u(pi/2,-0.635000,-0.711000, qreg_0[1])
subcirc0.u(pi/2,0.209000,0.266000, qreg_0[1])
subcirc0.u(pi/2,0.919000,-0.897000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.z(qreg_2[1])
subcirc1.u(pi/2,-0.154000,-0.640000, qreg_2[0])
subcirc1.u(pi/2,0.293000,0.720000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.u(param_1,0.713000,param_1, qreg_0[2])
main_circ.ry(-0.101000, qreg_0[2])
main_circ.u(param_0,0.809000,-0.780000, qreg_0[2])
main_circ.z(qreg_0[0])
main_circ.u(pi/2,param_2,param_0, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.ry(-0.037000, qreg_0[0])
main_circ.y(qreg_0[2])
main_circ.z(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.y(qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.ry(0.263000, qreg_0[1])
main_circ.u(param_0,0.622000,-0.581000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.ry(param_1, qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.ry(0.617000, qreg_0[2])
main_circ.u(param_0,param_2,param_2, qreg_3[0])
main_circ.u(pi/2,0.144000,-0.482000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.y(qreg_3[0])
bindings = {param_0: 0.144000, param_1: 0.356000, param_2: -0.215000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "819")
