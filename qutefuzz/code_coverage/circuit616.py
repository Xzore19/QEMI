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
subcirc0.u(0.385000,0.918000,-0.569000, qreg_0[3])
subcirc0.rx(0.255000, qreg_0[2])
subcirc0.ry(-0.288000, qreg_0[3])
subcirc0.u(0.034000,0.076000,-0.844000, qreg_0[1])
subcirc0.ry(0.225000, qreg_0[3])
subcirc0.ry(-0.113000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[2,3,1,0])
main_circ.u(-0.109000,-0.872000,0.984000, 1)
main_circ.rx(-0.160000, 3)
main_circ.ry(-0.479000, 2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.u(0.639000,param_2,param_1, qreg_0[0])
main_circ.append(subcirc0,[2,1,0,qreg_0[0]])
main_circ.rx(0.569000, 2)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.append(subcirc0,[0,1,2,3])
main_circ.rx(-0.107000, 2)
main_circ.append(subcirc0,[1,0,2,qreg_0[0]])
main_circ.append(subcirc0,[1,qreg_0[0],2,0])
main_circ.ry(param_1, 1)
main_circ.x(1)
main_circ.x(qreg_0[0])
bindings = {param_1: 0.054000, param_2: -0.616000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "616")
