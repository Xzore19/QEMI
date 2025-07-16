from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.408000,0.046000, qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.x(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[0],qreg_2[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cz(qreg_2[0],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cz(0,2)
main_circ.cz(3,1)
main_circ.cx(3,1)
main_circ.cz(2,3)
main_circ.u(param_1,param_2,param_2, 2)
main_circ.x(1)
main_circ.u(param_0,param_0,param_0, 1)
main_circ.x(0)
main_circ.x(3)
main_circ.cz(2,0)
main_circ.x(0)
main_circ.x(1)
main_circ.x(2)
main_circ.u(param_0,param_2,param_1, 3)
main_circ.x(0)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(pi/2,-0.083000,param_0, 0)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.x(0)
main_circ.x(1)
main_circ.cx(1,3)
main_circ.cx(2,0)
main_circ.u(pi/2,param_1,param_0, 1)
main_circ.append(subcirc0,[3,1,2,0])
main_circ.x(3)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.cz(3,0)
main_circ.x(3)
main_circ.cx(2,3)
main_circ.x(3)
main_circ.x(0)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.x(2)
main_circ.cz(0,3)
main_circ.u(param_2,0.535000,param_2, 3)
main_circ.cx(2,0)
main_circ.cz(1,3)
main_circ.x(2)
bindings = {param_0: -0.805000, param_1: -0.178000, param_2: 0.039000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "774")
