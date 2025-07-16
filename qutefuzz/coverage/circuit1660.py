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
subcirc0.cy(qreg_2[1],qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.s(qreg_0[1])
subcirc0.u(-0.449000,-0.673000,0.579000, qreg_0[1])
subcirc0.rx(-0.216000, qreg_2[1])
subcirc0.rx(0.342000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_2[0])
subcirc1.cy(qreg_0[1],qreg_2[0])
subcirc1.rx(-0.200000, qreg_0[1])
subcirc1.rx(-0.342000, qreg_2[1])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.326000, qreg_0[1])
subcirc2.u(0.029000,-0.786000,-0.222000, qreg_0[1])
subcirc2.rx(-0.909000, qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.s(qreg_2[0])
subcirc2.u(0.630000,-0.487000,-0.319000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.669000, qreg_1[1])
subcirc3.u(0.110000,0.021000,-0.910000, qreg_1[1])
subcirc3.u(0.187000,-0.230000,0.464000, qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3.u(0.224000,-0.551000,-0.907000, qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rx(0.827000, qreg_0[0])
subcirc4.s(qreg_0[3])
subcirc4.rx(0.299000, qreg_0[1])
subcirc4.u(0.672000,0.862000,0.305000, qreg_0[3])
subcirc4.u(-0.228000,0.659000,0.365000, qreg_0[3])
subcirc4.u(-0.527000,0.134000,-0.310000, qreg_0[3])
subcirc4 = subcirc4.to_gate().control(3)

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

main_circ.s(0)
main_circ.cy(3,0)
main_circ.cy(0,3)
main_circ.rx(-0.523000, 2)
main_circ.cy(1,2)
main_circ.append(subcirc1,[3,2,0,1])
main_circ.s(2)
main_circ.cy(3,2)
main_circ.s(2)
main_circ.rx(param_0, 2)
main_circ.u(-0.888000,-0.156000,0.226000, 3)
main_circ.rx(param_1, 1)
main_circ.rx(param_2, 0)
main_circ.append(subcirc1,[0,2,3,1])
main_circ.cy(1,3)
main_circ.u(param_1,param_0,param_0, 3)
main_circ.rx(0.003000, 1)
main_circ.u(-0.985000,0.285000,0.404000, 3)
main_circ.s(1)
main_circ.u(0.719000,param_2,0.369000, 2)
main_circ.cy(2,1)
main_circ.s(2)
main_circ.s(2)
main_circ.rx(param_0, 2)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.cy(1,2)
main_circ.cy(3,1)
main_circ.cy(3,0)
main_circ.cy(0,3)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.u(param_2,0.246000,-0.410000, 2)
main_circ.s(2)
main_circ.rx(0.237000, 2)
main_circ.s(1)
main_circ.rx(0.388000, 3)
bindings = {param_0: 0.694000, param_1: -0.724000, param_2: -0.820000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
