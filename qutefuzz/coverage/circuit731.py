from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.159000, qreg_3[0])
subcirc0.u(0,0,-0.148000, qreg_0[2])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,0.770000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(-0.282000, qreg_0[0])
subcirc1.h(qreg_2[0])
subcirc1.ry(0.420000, qreg_2[1])
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,-0.005000, qreg_0[0])
subcirc1.ry(-0.046000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.z(qreg_0[1])
main_circ.z(0)
main_circ.u(param_1,0,param_2, 3)
main_circ.z(0)
main_circ.z(1)
main_circ.ry(param_0, 0)
main_circ.h(2)
main_circ.ry(0.234000, 3)
main_circ.u(0,param_2,-0.442000, 2)
main_circ.z(3)
main_circ.append(subcirc0,[qreg_0[1],1,3,qreg_0[0]])
main_circ.ry(param_1, 2)
main_circ.ry(-0.790000, 1)
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.h(2)
main_circ.z(0)
main_circ.z(qreg_0[0])
main_circ.z(1)
main_circ.u(0,0,0.176000, 2)
main_circ.h(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[1,3,0,2])
main_circ.u(param_1,0,0.316000, 0)
main_circ.ry(0.573000, qreg_0[1])
main_circ.z(2)
main_circ.h(0)
main_circ.append(subcirc0,[qreg_0[1],1,3,qreg_0[0]])
main_circ.ry(0.133000, qreg_0[0])
main_circ.z(3)
main_circ.ry(-0.944000, 1)
main_circ.u(0,param_1,0.097000, 2)
main_circ.u(0,0,param_0, 2)
main_circ.z(qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.z(2)
main_circ.ry(-0.647000, 2)
main_circ.z(qreg_0[0])
main_circ.ry(param_0, 1)
main_circ.z(qreg_0[1])
bindings = {param_0: -0.278000, param_1: 0.944000, param_2: 0.780000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "731")
