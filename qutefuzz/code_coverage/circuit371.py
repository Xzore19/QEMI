from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.cy(qreg_3[0],qreg_2[0])
subcirc0.u(pi/2,0.534000,-0.159000, qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_2[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.023000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.u(pi/2,-0.500000,0.024000, qreg_0[3])
subcirc1.u(pi/2,0.775000,-0.779000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

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

main_circ.cz(qreg_1[0],1)
main_circ.cy(2,3)
main_circ.u(pi/2,param_1,0.933000, qreg_1[0])
main_circ.rx(0.734000, 0)
main_circ.rx(0.359000, 3)
main_circ.rx(param_0, 2)
main_circ.rx(-0.917000, qreg_0[0])
main_circ.cy(2,qreg_1[0])
main_circ.cz(1,0)
main_circ.rx(param_2, qreg_1[0])
main_circ.append(subcirc1,[0,3,qreg_1[0],1,2])
main_circ.u(param_0,0.308000,-0.534000, 1)
main_circ.cz(3,0)
main_circ.rx(param_2, qreg_1[0])
main_circ.rx(param_2, qreg_0[0])
main_circ.rx(-0.938000, qreg_0[0])
main_circ.u(param_1,param_2,-0.723000, 1)
main_circ.cy(qreg_1[0],2)
main_circ.append(subcirc1,[qreg_0[0],2,0,1,qreg_1[0]])
main_circ.cy(0,qreg_1[0])
main_circ.u(param_0,-0.900000,param_1, qreg_1[0])
main_circ.u(pi/2,param_0,0.585000, qreg_0[0])
main_circ.cz(3,1)
main_circ.rx(-0.422000, qreg_1[0])
main_circ.append(subcirc1,[0,3,2,qreg_1[0],1])
main_circ.cy(3,2)
main_circ.append(subcirc1,[0,qreg_1[0],qreg_0[0],2,1])
main_circ.append(subcirc1,[3,qreg_1[0],qreg_0[0],2,1])
main_circ.u(pi/2,param_2,param_1, 0)
main_circ.cz(0,qreg_0[0])
main_circ.cz(qreg_0[0],0)
bindings = {param_0: 0.679000, param_1: 0.531000, param_2: 0.008000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
