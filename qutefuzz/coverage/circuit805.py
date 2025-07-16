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
subcirc0.cz(qreg_3[0],qreg_1[0])
subcirc0.ry(0.325000, qreg_1[0])
subcirc0.u(0.102000,0.579000,0.849000, qreg_0[0])
subcirc0.ry(0.164000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.587000,-0.647000,-0.968000, qreg_0[3])
subcirc1.s(qreg_0[2])
subcirc1.u(-0.480000,-0.952000,-0.654000, qreg_0[3])
subcirc1.ry(-0.269000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.s(1)
main_circ.s(1)
main_circ.append(subcirc1,[1,2,3,0])
main_circ.s(2)
main_circ.u(param_0,-0.605000,param_0, 2)
main_circ.s(0)
main_circ.u(-0.193000,param_0,0.130000, 3)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.append(subcirc1,[2,1,3,0])
main_circ.u(param_0,param_0,0.507000, 1)
main_circ.u(0.127000,param_0,-0.445000, 2)
main_circ.u(param_0,-0.342000,param_0, 1)
main_circ.cz(3,1)
main_circ.cz(0,3)
main_circ.u(param_0,-0.182000,0.382000, 0)
main_circ.append(subcirc1,[2,1,3,0])
main_circ.cz(3,1)
main_circ.s(1)
main_circ.cz(1,2)
main_circ.cz(1,2)
main_circ.cz(1,2)
main_circ.cz(1,3)
main_circ.cz(1,2)
main_circ.cz(0,1)
main_circ.cz(0,2)
main_circ.cz(3,1)
main_circ.cz(2,0)
main_circ.cz(0,2)
main_circ.cz(3,0)
main_circ.cz(0,3)
main_circ.ry(param_0, 1)
bindings = {param_0: 0.865000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
