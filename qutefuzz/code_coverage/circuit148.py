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
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.u(0,0,-0.476000, qreg_2[0])
subcirc0.u(0,0,0.534000, qreg_2[1])
subcirc0.z(qreg_0[0])
subcirc0.y(qreg_2[0])

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
param_5 = Parameter("param_5")

main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(0,0,param_3, 2)
main_circ.u(0,param_2,-0.546000, 2)
main_circ.z(2)
main_circ.ry(0.575000, 1)
main_circ.z(2)
main_circ.ry(-0.906000, 3)
main_circ.y(2)
main_circ.y(1)
main_circ.y(0)
main_circ.y(3)
main_circ.z(2)
main_circ.y(0)
main_circ.y(2)
main_circ.ry(param_5, 3)
main_circ.y(2)
main_circ.y(3)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.y(3)
main_circ.ry(param_1, 2)
main_circ.y(0)
main_circ.z(0)
main_circ.u(0,param_3,0.512000, 1)
main_circ.z(3)
main_circ.u(0,param_0,param_4, 3)
main_circ.append(subcirc0,[3,1,2,0])
main_circ.y(3)
main_circ.ry(-0.316000, 2)
main_circ.y(2)
main_circ.u(0,param_3,param_1, 1)
main_circ.z(2)
main_circ.u(param_1,0,param_5, 0)
bindings = {param_0: 0.017000, param_1: -0.727000, param_2: -0.739000, param_3: -0.016000, param_4: 0.985000, param_5: 0.095000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "148")
