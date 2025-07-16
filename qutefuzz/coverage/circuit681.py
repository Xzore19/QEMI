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
subcirc0.u(0,0,-0.120000, qreg_0[2])
subcirc0.rz(-0.464000, qreg_0[2])
subcirc0.u(0,0,0.569000, qreg_0[1])
subcirc0.x(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.379000, qreg_0[1])
subcirc1.rz(0.328000, qreg_0[1])
subcirc1.cy(qreg_2[0],qreg_0[1])
subcirc1.u(0,0,-0.379000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[3,0,qreg_0[0],qreg_1[0]])
main_circ.x(1)
main_circ.u(param_0,0,param_5, qreg_0[0])
main_circ.append(subcirc1,[0,3,1,qreg_1[0]])
main_circ.cy(1,qreg_0[0])
main_circ.append(subcirc1,[2,3,1,qreg_1[0]])
main_circ.x(3)
main_circ.u(0,0,0.626000, 1)
main_circ.u(param_0,0,param_0, 0)
main_circ.rz(param_2, 3)
main_circ.x(2)
main_circ.u(param_4,0,-0.003000, 2)
main_circ.append(subcirc0,[1,qreg_0[0],2,qreg_1[0]])
main_circ.cy(1,qreg_0[0])
main_circ.rz(param_3, 2)
main_circ.rz(-0.674000, 3)
main_circ.append(subcirc1,[0,qreg_1[0],2,3])
main_circ.x(3)
main_circ.x(2)
main_circ.u(param_1,param_0,param_2, 1)
main_circ.append(subcirc1,[0,qreg_0[0],3,qreg_1[0]])
main_circ.append(subcirc0,[qreg_1[0],2,1,qreg_0[0]])
main_circ.cy(3,qreg_1[0])
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_1[0],2)
main_circ.cy(2,qreg_1[0])
main_circ.cy(qreg_0[0],1)
main_circ.cy(2,qreg_1[0])
main_circ.cy(3,qreg_1[0])
main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[0],3)
main_circ.cy(qreg_0[0],3)
main_circ.append(subcirc1,[3,qreg_1[0],1,2])
main_circ.rz(-0.888000, 0)
main_circ.rz(-0.495000, qreg_0[0])
bindings = {param_0: -0.799000, param_1: -0.210000, param_2: -0.526000, param_3: 0.735000, param_4: -0.636000, param_5: -0.717000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "681")
