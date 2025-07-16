from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(-0.992000,-0.286000,0.721000, qreg_3[0])
subcirc0.u(0.385000,0.979000,-0.210000, qreg_1[1])
subcirc0.u(-0.216000,-0.595000,-0.251000, qreg_3[0])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_1[0])
subcirc0.rz(0.035000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.145000,-0.068000,-0.272000, qreg_0[2])
subcirc1.u(-0.231000,0.590000,0.331000, qreg_0[1])
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_0[2])
subcirc1.z(qreg_3[0])
subcirc1.rz(-0.898000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.append(subcirc1,[2,3,0,1])
main_circ.u(0,param_4,-0.811000, 1)
main_circ.u(param_1,param_2,-0.310000, 0)
main_circ.u(-0.458000,param_0,param_4, 0)
main_circ.u(param_1,-0.056000,-0.575000, 3)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.append(subcirc1,[1,3,0,2])
main_circ.rz(-0.106000, 3)
main_circ.append(subcirc1,[3,0,2,1])
main_circ.z(0)
main_circ.rz(-0.198000, 3)
main_circ.rz(param_4, 0)
main_circ.u(0,0,-0.970000, 3)
main_circ.u(0.665000,param_4,param_1, 3)
main_circ.u(param_2,param_0,-0.378000, 0)
main_circ.z(2)
main_circ.rz(-0.643000, 1)
main_circ.append(subcirc1,[3,0,2,1])
main_circ.u(0.638000,0.753000,param_3, 3)
main_circ.rz(-0.343000, 3)
main_circ.rz(0.191000, 1)
main_circ.rz(0.383000, 0)
main_circ.u(param_3,param_4,-0.385000, 3)
main_circ.rz(-0.076000, 1)
main_circ.u(param_1,0,-0.642000, 0)
bindings = {param_0: 0.073000, param_1: 0.490000, param_2: 0.864000, param_3: -0.661000, param_4: 0.520000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1944")
