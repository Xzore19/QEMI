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
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.cz(qreg_1[1],qreg_1[0])
subcirc0.u(0,0,-0.537000, qreg_1[2])
subcirc0.cz(qreg_1[2],qreg_1[0])
subcirc0.cz(qreg_1[1],qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.198000, qreg_0[1])
subcirc1.u(pi/2,0.472000,0.299000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[3])
subcirc1.u(0,0,-0.521000, qreg_0[3])
subcirc1.u(pi/2,-0.381000,-0.961000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,-0.374000,0.820000, qreg_2[0])
subcirc2.cx(qreg_2[1],qreg_0[0])
subcirc2.cx(qreg_0[1],qreg_2[1])
subcirc2.u(0,0,-0.169000, qreg_0[1])
subcirc2.u(0,0,0.117000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc2,[1,0,2,3])
main_circ.cx(3,1)
main_circ.u(0,param_1,-0.752000, 3)
main_circ.u(param_2,param_2,-0.678000, 0)
main_circ.u(0,param_0,param_2, 2)
main_circ.cz(3,0)
main_circ.cz(2,1)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(pi/2,param_0,param_0, 0)
main_circ.cx(2,0)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.append(subcirc0,[3,2,1,0])
main_circ.u(pi/2,param_1,-0.848000, 0)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.append(subcirc0,[2,3,1,0])
main_circ.cx(1,3)
main_circ.cx(0,2)
main_circ.u(param_2,-0.126000,-0.181000, 2)
main_circ.append(subcirc2,[0,2,3,1])
main_circ.cx(2,0)
main_circ.u(pi/2,param_1,0.005000, 2)
main_circ.u(param_0,0,param_0, 1)
main_circ.u(param_0,0,param_0, 1)
main_circ.u(param_2,param_1,param_0, 0)
bindings = {param_0: 0.930000, param_1: 0.855000, param_2: -0.598000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "319")
