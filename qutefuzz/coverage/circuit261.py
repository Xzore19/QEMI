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
subcirc0.h(qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_2[0])
subcirc0.u(0,0,0.898000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.521000, qreg_0[0])
subcirc1.rz(-0.130000, qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,-0.065000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.156000, qreg_3[0])
subcirc2.h(qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[2])
subcirc3.s(qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3.rz(0.572000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(1)
main_circ.s(2)
main_circ.h(3)
main_circ.u(0,0,param_1, 1)
main_circ.h(3)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.u(param_1,0,param_0, 2)
main_circ.h(3)
main_circ.rz(param_1, 2)
main_circ.h(3)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.rz(param_1, 1)
main_circ.append(subcirc2,[2,3,1,0])
main_circ.u(0,0,0.756000, 2)
main_circ.h(2)
main_circ.u(param_0,0,param_1, 3)
main_circ.rz(0.035000, 1)
main_circ.h(3)
main_circ.s(1)
main_circ.s(1)
main_circ.s(3)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.h(3)
main_circ.u(param_2,0,-0.176000, 2)
main_circ.s(2)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.s(1)
main_circ.h(3)
main_circ.h(1)
main_circ.u(param_1,param_1,-0.505000, 2)
main_circ.u(param_1,param_2,param_0, 3)
main_circ.append(subcirc2,[2,3,0,1])
main_circ.append(subcirc2,[1,0,2,3])
main_circ.s(1)
main_circ.u(0,0,0.635000, 0)
main_circ.append(subcirc2,[0,2,1,3])
bindings = {param_0: 0.538000, param_1: -0.883000, param_2: -0.865000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "261")
