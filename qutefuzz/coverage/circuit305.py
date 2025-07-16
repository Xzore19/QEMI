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
subcirc0.rx(-0.634000, qreg_1[0])
subcirc0.rx(0.042000, qreg_1[2])
subcirc0.u(pi/2,0.683000,-0.761000, qreg_1[1])
subcirc0.u(pi/2,0.601000,0.479000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.908000,0.485000, qreg_1[1])
subcirc1.x(qreg_1[1])
subcirc1.s(qreg_1[2])
subcirc1.u(pi/2,-0.067000,0.879000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[2])
subcirc2.u(pi/2,0.762000,-0.197000, qreg_0[2])
subcirc2.x(qreg_0[0])
subcirc2.rx(0.975000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.s(0)
main_circ.s(0)
main_circ.append(subcirc1,[qreg_0[1],1,3,qreg_0[0]])
main_circ.s(1)
main_circ.rx(param_0, 0)
main_circ.rx(param_1, qreg_0[0])
main_circ.x(3)
main_circ.s(qreg_0[1])
main_circ.u(param_0,0.472000,param_1, qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],2])
main_circ.append(subcirc1,[qreg_0[1],2,qreg_0[0],3])
main_circ.append(subcirc1,[2,1,qreg_0[0],qreg_0[1]])
main_circ.s(3)
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],1])
main_circ.x(0)
main_circ.x(qreg_0[1])
main_circ.append(subcirc0,[1,0,3,qreg_0[1]])
main_circ.s(1)
main_circ.rx(param_1, 3)
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],2])
main_circ.u(pi/2,-0.563000,param_1, qreg_0[1])
main_circ.x(0)
main_circ.u(pi/2,0.683000,param_1, qreg_0[1])
bindings = {param_0: -0.448000, param_1: 0.862000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "305")
