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
subcirc0.ry(0.145000, qreg_0[3])
subcirc0.ry(-0.786000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[3])
subcirc0.u(0,0,0.293000, qreg_0[2])
subcirc0.u(0,0,-0.932000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.686000, qreg_0[0])
subcirc1.ry(0.075000, qreg_0[3])
subcirc1.u(0.207000,-0.690000,-0.853000, qreg_0[3])
subcirc1.u(0,0,0.941000, qreg_0[0])
subcirc1.cy(qreg_0[2],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")
param_8 = Parameter("param_8")

main_circ.ry(0.032000, qreg_2[0])
main_circ.u(0.493000,-0.306000,0.642000, qreg_2[1])
main_circ.cy(0,qreg_2[1])
main_circ.u(0,0,param_1, 0)
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],0,qreg_2[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.cy(qreg_2[0],qreg_0[0])
main_circ.ry(0.317000, qreg_2[1])
main_circ.u(0.881000,param_2,param_8, qreg_2[1])
main_circ.u(param_2,param_6,0.217000, qreg_0[0])
main_circ.u(param_2,0,0.553000, qreg_2[0])
main_circ.u(0,param_1,param_5, qreg_2[0])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.u(0.375000,param_4,-0.460000, qreg_2[1])
main_circ.u(param_7,0.741000,param_5, qreg_2[1])
main_circ.u(param_6,param_2,param_3, 0)
main_circ.u(param_6,-0.827000,-0.428000, qreg_0[1])
main_circ.ry(param_0, qreg_2[0])
main_circ.ry(0.482000, qreg_0[0])
main_circ.ry(param_4, qreg_2[1])
main_circ.ry(param_8, qreg_2[1])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],qreg_2[1]])
main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_2[0],0)
main_circ.cy(0,qreg_0[1])
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.cy(qreg_0[0],qreg_2[1])
main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.cy(qreg_0[1],0)
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.u(param_7,0.216000,0.764000, qreg_2[1])
main_circ.ry(0.235000, qreg_0[0])
main_circ.ry(param_3, qreg_2[0])
main_circ.u(-0.314000,0.531000,-0.224000, qreg_2[1])
bindings = {param_0: -0.607000, param_1: 0.463000, param_2: 0.834000, param_3: -0.355000, param_4: 0.948000, param_5: 0.233000, param_6: 0.739000, param_7: -0.925000, param_8: 0.179000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1605")
