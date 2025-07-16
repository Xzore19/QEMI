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
subcirc0.rz(-0.914000, qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.rz(0.901000, qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.rz(0.440000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.ry(0.245000, qreg_3[0])
subcirc1.ry(0.618000, qreg_2[0])
subcirc1.h(qreg_3[0])
subcirc1.ry(-0.638000, qreg_2[0])
subcirc1.rz(0.605000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rz(param_2, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.rz(0.705000, qreg_3[0])
main_circ.rz(param_2, qreg_3[0])
main_circ.ry(param_2, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.u(pi/2,0.862000,param_1, qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.u(pi/2,param_1,0.963000, qreg_0[2])
main_circ.u(pi/2,param_2,-0.492000, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.u(param_2,0.277000,param_1, qreg_3[0])
main_circ.ry(-0.100000, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.ry(param_3, qreg_0[1])
main_circ.ry(param_3, qreg_0[2])
main_circ.ry(-0.469000, qreg_0[1])
main_circ.u(param_2,param_0,param_2, qreg_3[0])
bindings = {param_0: 0.233000, param_1: -0.833000, param_2: -0.343000, param_3: -0.370000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1805")
