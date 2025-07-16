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
subcirc0.u(0,0,-0.389000, qreg_1[0])
subcirc0.z(qreg_1[0])
subcirc0.u(0.835000,-0.601000,-0.771000, qreg_2[0])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_2[0])
subcirc1.u(0.925000,0.330000,-0.089000, qreg_2[0])
subcirc1.s(qreg_0[0])
subcirc1.z(qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.697000, qreg_1[1])
subcirc2.u(-0.153000,0.950000,0.995000, qreg_1[0])
subcirc2.z(qreg_1[0])
subcirc2.s(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.s(qreg_3[0])
main_circ.u(param_1,0,-0.245000, qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.s(0)
main_circ.u(param_1,0,-0.989000, qreg_3[0])
main_circ.u(0.126000,0.046000,-0.569000, 0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[0],0])
main_circ.u(0,param_0,-0.682000, qreg_0[2])
main_circ.s(qreg_0[0])
main_circ.s(qreg_3[0])
main_circ.u(param_1,param_1,param_1, qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.u(param_1,0,param_0, qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],0,qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_0[1],0])
main_circ.z(0)
main_circ.z(qreg_0[1])
main_circ.u(param_1,0.548000,-0.221000, qreg_0[0])
main_circ.s(qreg_0[2])
main_circ.z(qreg_3[0])
main_circ.s(qreg_0[1])
main_circ.u(0,param_0,0.477000, qreg_0[2])
main_circ.z(qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.u(param_0,0,-0.033000, qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.u(param_0,0,param_0, qreg_0[2])
main_circ.z(qreg_0[2])
main_circ.u(0,0,param_0, qreg_0[1])
bindings = {param_0: 0.843000, param_1: 0.281000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1677")
