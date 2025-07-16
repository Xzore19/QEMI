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
subcirc0.s(qreg_0[3])
subcirc0.ry(0.350000, qreg_0[0])
subcirc0.u(0,0,-0.109000, qreg_0[3])
subcirc0.ry(0.607000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.977000, qreg_0[1])
subcirc1.u(0,0,-0.402000, qreg_0[0])
subcirc1.s(qreg_0[2])
subcirc1.ry(-0.572000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(0,param_2,param_0, 2)
main_circ.u(param_2,0,-0.704000, 0)
main_circ.ry(-0.853000, 3)
main_circ.ry(-0.497000, 1)
main_circ.u(0,0,-0.898000, 3)
main_circ.append(subcirc1,[2,0,qreg_1[0],1,qreg_0[0]])
main_circ.u(param_1,0,param_1, 2)
main_circ.rz(-0.816000, qreg_0[0])
main_circ.rz(param_2, qreg_0[0])
main_circ.rz(param_2, 1)
main_circ.ry(0.205000, 2)
main_circ.rz(param_1, 0)
main_circ.rz(param_0, 3)
main_circ.ry(0.869000, 0)
main_circ.append(subcirc1,[qreg_0[0],0,2,qreg_1[0],1])
main_circ.u(param_1,0,0.475000, 3)
main_circ.rz(param_1, qreg_1[0])
main_circ.s(0)
main_circ.rz(-0.584000, 1)
main_circ.rz(0.553000, 3)
main_circ.append(subcirc1,[2,qreg_0[0],1,qreg_1[0],0])
main_circ.append(subcirc0,[qreg_0[0],2,qreg_1[0],1])
main_circ.s(qreg_0[0])
main_circ.append(subcirc1,[1,3,2,qreg_0[0],0])
main_circ.append(subcirc0,[qreg_0[0],3,0,2])
main_circ.ry(-0.832000, 3)
main_circ.u(0,param_1,param_2, qreg_1[0])
main_circ.s(2)
main_circ.append(subcirc1,[0,2,1,qreg_0[0],3])
main_circ.append(subcirc0,[qreg_1[0],1,3,qreg_0[0]])
main_circ.append(subcirc0,[1,3,qreg_1[0],qreg_0[0]])
bindings = {param_0: 0.886000, param_1: -0.891000, param_2: 0.141000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1267")
