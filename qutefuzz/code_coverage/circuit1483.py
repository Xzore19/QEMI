from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,0.887000, qreg_0[0])
subcirc0.u(0.018000,0.267000,-0.519000, qreg_1[1])
subcirc0.cz(qreg_1[1],qreg_1[0])
subcirc0.cz(qreg_1[0],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.cz(qreg_1[1],qreg_0[0])
subcirc1.cz(qreg_1[0],qreg_0[0])
subcirc1.u(0.957000,-0.285000,-0.911000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[3,0,2,1])
main_circ.u(0,0,-0.857000, 1)
main_circ.h(0)
main_circ.u(0,0,param_1, 3)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cz(1,2)
main_circ.u(0,0,0.328000, 1)
main_circ.h(0)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.h(2)
main_circ.cz(0,3)
main_circ.h(0)
main_circ.u(-0.044000,-0.009000,param_1, 2)
main_circ.u(0,0,param_1, 3)
main_circ.h(0)
main_circ.u(-0.836000,param_1,param_0, 0)
main_circ.h(0)
main_circ.cz(0,1)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc0,[1,2,3,0])
main_circ.u(param_0,0,-0.187000, 0)
main_circ.cz(0,3)
main_circ.h(3)
main_circ.u(0,0,param_0, 0)
main_circ.h(3)
main_circ.cz(1,3)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.u(0,param_1,0.668000, 0)
bindings = {param_0: 0.676000, param_1: 0.432000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1483")
