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
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_2[1])
subcirc1.cy(qreg_0[1],qreg_2[1])
subcirc1.x(qreg_2[1])
subcirc1.cy(qreg_0[1],qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.h(qreg_0[2])
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2.x(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,-0.268000,-0.282000, qreg_0[1])
subcirc3.cy(qreg_0[3],qreg_0[0])
subcirc3.h(qreg_0[3])
subcirc3.u(pi/2,0.519000,0.036000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.903000,0.684000, qreg_3[0])
subcirc4.x(qreg_0[1])
subcirc4.cy(qreg_0[0],qreg_3[0])
subcirc4.u(pi/2,0.817000,-0.504000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(param_0,-0.733000,param_3, 1)
main_circ.append(subcirc1,[1,qreg_0[0],2,3])
main_circ.h(2)
main_circ.h(0)
main_circ.x(3)
main_circ.append(subcirc4,[2,qreg_0[0],3,1,0])
main_circ.cy(3,qreg_0[0])
main_circ.append(subcirc0,[0,1,qreg_0[0],2,3])
main_circ.x(3)
main_circ.u(pi/2,param_1,-0.290000, 1)
main_circ.u(param_2,0.384000,-0.809000, 3)
main_circ.append(subcirc2,[3,qreg_0[0],2,0])
main_circ.x(3)
main_circ.u(pi/2,-0.436000,0.070000, 1)
main_circ.cy(0,1)
main_circ.cy(qreg_0[0],0)
main_circ.x(0)
main_circ.append(subcirc4,[qreg_0[0],3,0,2,1])
main_circ.cy(0,3)
main_circ.cy(0,1)
main_circ.cy(2,1)
main_circ.cy(0,1)
main_circ.append(subcirc2,[1,qreg_0[0],2,3])
main_circ.append(subcirc0,[2,0,qreg_0[0],3,1])
main_circ.u(param_0,0.251000,-0.511000, 1)
bindings = {param_0: 0.205000, param_1: 0.262000, param_2: -0.626000, param_3: 0.799000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1714")
