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
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.766000, qreg_0[0])
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1.u(0,0,0.471000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.y(qreg_0[1])
subcirc1.ry(-0.411000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_0,param_0,-0.392000, 1)
main_circ.cx(0,3)
main_circ.u(param_0,0,param_1, 2)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.append(subcirc0,[0,qreg_1[0],qreg_0[0],3])
main_circ.y(2)
main_circ.u(param_0,param_1,-0.330000, 0)
main_circ.cx(3,0)
main_circ.append(subcirc1,[0,2,qreg_1[0],qreg_0[0]])
main_circ.cx(3,1)
main_circ.y(qreg_1[0])
main_circ.u(0,0,0.173000, 0)
main_circ.ry(param_0, 1)
main_circ.ry(param_0, 2)
main_circ.y(qreg_0[0])
main_circ.u(param_1,param_0,param_0, 1)
main_circ.cx(0,qreg_1[0])
main_circ.y(1)
main_circ.append(subcirc1,[qreg_0[0],2,3,1])
main_circ.ry(0.782000, qreg_0[0])
main_circ.u(0,param_0,param_0, 2)
main_circ.cx(qreg_1[0],3)
bindings = {param_0: -0.362000, param_1: 0.524000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
