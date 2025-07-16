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
subcirc0.rz(-0.987000, qreg_1[1])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_1[0])
subcirc0.x(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.929000,0.543000, qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.u(pi/2,-0.511000,-0.385000, qreg_0[2])
subcirc1.rz(-0.677000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,-0.278000,0.909000, qreg_0[0])
subcirc2.u(pi/2,-0.712000,0.288000, qreg_0[3])
subcirc2.u(pi/2,-0.652000,-0.692000, qreg_0[3])
subcirc2.rz(0.712000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(-0.250000, qreg_0[0])
subcirc3.s(qreg_0[3])
subcirc3.rz(0.500000, qreg_0[1])
subcirc3.x(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rz(param_1, 1)
main_circ.append(subcirc1,[qreg_1[0],0,1,3])
main_circ.u(pi/2,param_0,0.034000, qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],3,2,0])
main_circ.append(subcirc3,[1,3,2,qreg_1[0]])
main_circ.s(qreg_1[0])
main_circ.rz(param_0, 3)
main_circ.s(2)
main_circ.append(subcirc3,[qreg_1[0],1,3,2])
main_circ.rz(param_1, 3)
main_circ.append(subcirc0,[qreg_0[0],3,qreg_1[0],1])
main_circ.rz(0.023000, 3)
main_circ.u(param_1,param_1,0.600000, 2)
main_circ.u(param_0,0.071000,param_1, qreg_0[0])
main_circ.rz(-0.469000, 2)
main_circ.append(subcirc0,[2,3,1,0])
main_circ.x(2)
main_circ.append(subcirc3,[3,2,1,qreg_1[0]])
main_circ.append(subcirc3,[qreg_0[0],1,0,2])
main_circ.append(subcirc1,[1,qreg_0[0],0,3])
main_circ.append(subcirc0,[2,qreg_1[0],1,0])
main_circ.s(0)
bindings = {param_0: -0.594000, param_1: -0.367000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
