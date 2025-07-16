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
subcirc0.y(qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.u(0.911000,0.881000,0.530000, qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

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

main_circ.rx(param_0, 1)
main_circ.rx(-0.178000, 2)
main_circ.rx(param_1, 1)
main_circ.u(param_1,-0.056000,param_2, 1)
main_circ.z(0)
main_circ.z(0)
main_circ.rx(0.440000, 0)
main_circ.y(3)
main_circ.z(0)
main_circ.z(3)
main_circ.y(3)
main_circ.rx(param_2, 2)
main_circ.u(-0.742000,param_4,param_1, 2)
main_circ.u(-0.614000,-0.493000,0.826000, 1)
main_circ.u(0.838000,0.553000,param_1, 1)
main_circ.u(0.764000,param_4,param_1, 2)
main_circ.y(2)
main_circ.z(0)
main_circ.u(param_3,param_4,0.765000, 1)
main_circ.rx(-0.820000, 0)
main_circ.y(3)
main_circ.z(3)
main_circ.rx(param_3, 0)
main_circ.u(param_1,0.821000,param_4, 0)
main_circ.u(param_2,param_4,param_0, 3)
main_circ.rx(param_1, 0)
main_circ.y(3)
main_circ.y(2)
main_circ.rx(param_3, 0)
main_circ.z(2)
main_circ.y(1)
main_circ.rx(-0.847000, 2)
main_circ.z(1)
main_circ.u(0.988000,-0.354000,0.900000, 1)
main_circ.y(0)
main_circ.u(-0.975000,param_1,-0.030000, 0)
main_circ.rx(param_3, 1)
main_circ.z(2)
main_circ.rx(-0.864000, 3)
main_circ.z(2)
bindings = {param_0: -0.359000, param_1: -0.076000, param_2: -0.321000, param_3: -0.518000, param_4: -0.375000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
