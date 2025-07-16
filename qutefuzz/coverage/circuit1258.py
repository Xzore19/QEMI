from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.s(qreg_2[0])
subcirc0.u(-0.396000,-0.893000,0.762000, qreg_0[1])
subcirc0.x(qreg_2[0])
subcirc0.u(0.714000,0.846000,0.392000, qreg_3[0])
subcirc0.x(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.u(-0.640000,-0.919000,0.352000, qreg_0[1])
subcirc1.rx(-0.490000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(0.785000, qreg_0[0])
subcirc2.s(qreg_0[3])
subcirc2.s(qreg_0[3])
subcirc2.x(qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.x(qreg_0[2])
main_circ.u(-0.632000,param_1,param_1, qreg_0[2])
main_circ.u(param_0,0.196000,param_1, qreg_0[2])
main_circ.u(param_1,0.491000,param_1, qreg_0[2])
main_circ.u(param_0,param_0,param_1, qreg_0[2])
main_circ.s(qreg_0[0])
main_circ.u(param_1,param_1,param_1, qreg_0[2])
main_circ.u(-0.864000,-0.801000,param_1, qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.u(0.769000,param_0,param_1, qreg_0[3])
main_circ.u(param_0,-0.634000,-0.690000, qreg_0[2])
main_circ.s(qreg_0[3])
main_circ.rx(param_0, qreg_0[2])
main_circ.rx(-0.689000, qreg_0[1])
main_circ.u(param_1,param_0,param_0, qreg_0[3])
main_circ.rx(param_1, qreg_0[1])
main_circ.u(0.374000,-0.657000,0.720000, qreg_0[3])
main_circ.s(qreg_0[0])
main_circ.rx(-0.751000, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.rx(param_1, qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.s(qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.rx(param_1, qreg_0[0])
main_circ.u(param_0,0.812000,param_1, qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.x(qreg_0[0])
main_circ.s(qreg_0[3])
main_circ.rx(param_1, qreg_0[1])
main_circ.rx(0.670000, qreg_0[3])
main_circ.u(param_0,0.561000,-0.859000, qreg_0[3])
main_circ.rx(0.134000, qreg_0[1])
main_circ.s(qreg_0[1])
main_circ.u(param_0,-0.604000,-0.529000, qreg_0[0])
main_circ.rx(-0.919000, qreg_0[0])
main_circ.s(qreg_0[3])
main_circ.rx(0.465000, qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.u(param_1,param_0,0.482000, qreg_0[2])
main_circ.u(-0.066000,0.928000,0.589000, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.rx(param_1, qreg_0[1])
bindings = {param_0: -0.493000, param_1: -0.369000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
