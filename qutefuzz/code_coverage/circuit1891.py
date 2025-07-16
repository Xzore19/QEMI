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
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[3])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.u(pi/2,-0.918000,-0.559000, qreg_0[3])
subcirc0.cy(qreg_0[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.u(pi/2,-0.974000,0.813000, qreg_0[2])
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.u(pi/2,0.915000,0.242000, qreg_0[1])
subcirc1.u(pi/2,0.172000,0.307000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(-0.895000,-0.461000,0.301000, qreg_2[1])
subcirc2.u(-0.140000,0.624000,-0.302000, qreg_2[0])
subcirc2.cy(qreg_2[1],qreg_0[0])
subcirc2.cy(qreg_0[1],qreg_2[0])
subcirc2.u(pi/2,-0.292000,0.984000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,-0.962000,0.725000, qreg_0[0])
subcirc3.u(pi/2,0.936000,-0.816000, qreg_0[1])
subcirc3.u(pi/2,0.516000,-0.162000, qreg_3[0])
subcirc3.u(-0.821000,-0.911000,-0.231000, qreg_0[0])
subcirc3.cy(qreg_0[2],qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.y(1)
main_circ.u(param_4,param_1,param_4, 1)
main_circ.append(subcirc1,[2,3,0,1])
main_circ.append(subcirc1,[0,3,2,1])
main_circ.append(subcirc2,[1,0,2,3])
main_circ.append(subcirc3,[3,1,2,0])
main_circ.append(subcirc0,[2,3,1,0])
main_circ.append(subcirc0,[0,2,1,3])
main_circ.y(3)
main_circ.append(subcirc3,[2,1,3,0])
main_circ.u(0.182000,0.440000,0.375000, 2)
main_circ.u(pi/2,0.776000,-0.364000, 0)
main_circ.append(subcirc1,[1,0,3,2])
bindings = {param_1: 0.832000, param_4: -0.700000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1891")
