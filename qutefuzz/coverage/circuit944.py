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
subcirc0.h(qreg_0[2])
subcirc0.u(0,0,0.232000, qreg_0[1])
subcirc0.x(qreg_0[3])
subcirc0.h(qreg_0[3])
subcirc0.h(qreg_0[0])
subcirc0.u(pi/2,-0.613000,-0.676000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.x(qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.u(0,param_0,param_1, qreg_0[3])
main_circ.h(0)
main_circ.x(0)
main_circ.u(0,0,-0.277000, qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.u(pi/2,0.013000,param_2, qreg_0[0])
main_circ.u(param_1,0,-0.238000, qreg_0[1])
main_circ.h(0)
main_circ.u(param_2,param_2,0.855000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.u(0,0,0.510000, 0)
main_circ.x(qreg_0[0])
main_circ.u(param_0,0.633000,param_1, qreg_0[0])
main_circ.x(qreg_0[3])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
main_circ.u(param_1,param_2,param_1, qreg_0[1])
main_circ.u(pi/2,0.693000,-0.883000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],0,qreg_0[3],qreg_0[1]])
main_circ.u(pi/2,param_2,0.088000, qreg_0[1])
main_circ.u(0,0,param_1, 0)
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],0,qreg_0[0],qreg_0[3]])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.u(0,0,-0.847000, qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.u(param_0,0.875000,0.252000, qreg_0[0])
main_circ.u(pi/2,0.110000,param_2, qreg_0[2])
main_circ.x(0)
main_circ.x(0)
main_circ.h(qreg_0[2])
main_circ.u(param_1,param_1,param_0, qreg_0[3])
bindings = {param_0: -0.077000, param_1: -0.306000, param_2: 0.734000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "944")
