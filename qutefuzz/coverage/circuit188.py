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
subcirc0.ry(-0.699000, qreg_0[3])
subcirc0.s(qreg_0[3])
subcirc0.u(0,0,-0.419000, qreg_0[3])
subcirc0.ry(0.550000, qreg_0[3])
subcirc0.s(qreg_0[3])
subcirc0.rz(0.023000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(-0.034000, qreg_0[1])
subcirc1.rz(-0.986000, qreg_0[0])
subcirc1.u(0,0,0.865000, qreg_0[2])
subcirc1.ry(-0.306000, qreg_0[0])
subcirc1.u(0,0,0.290000, qreg_0[3])
subcirc1.ry(-0.669000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[3])
subcirc2.u(0,0,0.109000, qreg_0[2])
subcirc2.ry(0.164000, qreg_0[1])
subcirc2.s(qreg_0[2])
subcirc2.ry(-0.085000, qreg_0[3])
subcirc2.rz(-0.432000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(0.536000, qreg_2[1])
subcirc3.rz(0.900000, qreg_2[0])
subcirc3.rz(-0.572000, qreg_0[1])
subcirc3.ry(0.597000, qreg_2[0])
subcirc3.s(qreg_2[0])
subcirc3.s(qreg_2[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rz(-0.389000, qreg_0[0])
subcirc4.ry(-0.806000, qreg_0[2])
subcirc4.u(0,0,-0.952000, qreg_0[2])
subcirc4.ry(0.297000, qreg_0[2])
subcirc4.s(qreg_0[1])
subcirc4.rz(-0.999000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(2)
main_circ.s(3)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.u(param_1,param_2,param_1, 1)
main_circ.rz(-0.415000, 2)
main_circ.rz(param_2, 0)
main_circ.rz(0.021000, 2)
main_circ.ry(0.384000, 0)
main_circ.ry(0.349000, 3)
main_circ.ry(param_1, 3)
main_circ.append(subcirc1,[3,1,2,0])
main_circ.append(subcirc0,[0,1,3,2])
main_circ.ry(param_1, 2)
main_circ.append(subcirc4,[3,2,1,0])
main_circ.u(0,param_1,param_2, 1)
main_circ.s(1)
main_circ.s(2)
main_circ.u(0,0,0.805000, 0)
main_circ.u(0,0,param_2, 3)
main_circ.u(0,0,-0.152000, 3)
main_circ.ry(param_1, 0)
main_circ.ry(-0.813000, 1)
main_circ.ry(param_0, 2)
bindings = {param_0: 0.800000, param_1: 0.415000, param_2: -0.741000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "188")
