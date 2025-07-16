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
subcirc0.ry(-0.775000, qreg_3[0])
subcirc0.ry(0.369000, qreg_0[1])
subcirc0.ry(0.513000, qreg_0[0])
subcirc0.ry(-0.804000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[2])
subcirc1.ry(0.008000, qreg_3[0])
subcirc1.h(qreg_0[0])
subcirc1.ry(0.892000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.596000, qreg_2[0])
subcirc2.ry(-0.143000, qreg_0[0])
subcirc2.ry(0.649000, qreg_2[0])
subcirc2.u(0,0,-0.526000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[1])
subcirc3.y(qreg_0[1])
subcirc3.u(0,0,0.059000, qreg_0[1])
subcirc3.ry(-0.029000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(0,0,-0.939000, 0)
main_circ.h(0)
main_circ.u(0,param_0,-0.771000, 2)
main_circ.u(0,param_0,-0.034000, 0)
main_circ.ry(-0.734000, 0)
main_circ.ry(param_0, 3)
main_circ.y(0)
main_circ.h(0)
main_circ.ry(param_0, 0)
main_circ.ry(param_0, qreg_0[0])
main_circ.u(param_0,param_0,-0.823000, qreg_0[0])
main_circ.ry(param_0, 1)
main_circ.u(param_0,param_0,0.221000, 0)
main_circ.append(subcirc0,[qreg_0[0],3,2,1])
main_circ.u(param_0,0,0.101000, 3)
main_circ.y(qreg_0[0])
main_circ.u(param_0,0,-0.233000, 0)
main_circ.ry(-0.422000, 1)
main_circ.ry(-0.359000, 1)
main_circ.append(subcirc0,[0,qreg_0[0],2,1])
main_circ.append(subcirc0,[3,1,2,qreg_0[0]])
main_circ.y(1)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.u(param_0,0,param_0, 1)
main_circ.ry(0.637000, 2)
main_circ.u(0,param_0,-0.288000, 1)
main_circ.append(subcirc0,[3,2,qreg_0[0],1])
main_circ.u(0,param_0,0.200000, 3)
main_circ.ry(-0.757000, 0)
main_circ.ry(0.528000, 1)
main_circ.y(3)
main_circ.u(param_0,param_0,param_0, 1)
bindings = {param_0: -0.112000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
