from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_2[1])
subcirc0.x(qreg_0[1])
subcirc0.cx(qreg_2[1],qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.z(3)
main_circ.append(subcirc0,[3,0,1,qreg_0[1],2])
main_circ.z(3)
main_circ.cx(qreg_0[0],0)
main_circ.cx(3,2)
main_circ.cx(qreg_0[1],1)
main_circ.append(subcirc0,[qreg_0[1],0,3,1,2])
main_circ.append(subcirc0,[2,0,qreg_0[1],3,qreg_0[0]])
main_circ.cx(0,qreg_0[1])
main_circ.append(subcirc0,[2,1,qreg_0[1],qreg_0[0],3])
main_circ.u(param_1,param_1,0.362000, qreg_0[1])
main_circ.u(param_1,param_0,param_1, 1)
main_circ.cx(2,qreg_0[1])
main_circ.append(subcirc0,[3,qreg_0[0],2,0,qreg_0[1]])
main_circ.z(3)
main_circ.z(qreg_0[1])
main_circ.u(param_1,-0.393000,-0.902000, 3)
main_circ.z(qreg_0[1])
main_circ.u(param_0,0.449000,param_0, qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.x(3)
main_circ.z(2)
bindings = {param_0: -0.011000, param_1: 0.479000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
