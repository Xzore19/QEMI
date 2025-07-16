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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.u(-0.068000,0.194000,-0.359000, qreg_3[0])
subcirc0.u(-0.054000,-0.311000,-0.709000, qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.x(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_0[0])
subcirc1.x(qreg_1[0])
subcirc1.x(qreg_1[0])
subcirc1.rz(-0.602000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[0,qreg_0[0],3,1])
main_circ.x(qreg_0[0])
main_circ.cx(qreg_0[0],1)
main_circ.cx(0,1)
main_circ.x(2)
main_circ.rz(-0.551000, 1)
main_circ.append(subcirc0,[qreg_0[0],3,1,2])
main_circ.append(subcirc0,[2,0,3,1])
main_circ.append(subcirc0,[2,0,3,1])
main_circ.u(0.951000,-0.709000,param_1, 1)
main_circ.u(param_0,-0.108000,param_0, 3)
main_circ.append(subcirc1,[0,2,qreg_0[0],3,1])
main_circ.append(subcirc0,[1,0,qreg_0[0],3])
main_circ.append(subcirc0,[3,1,qreg_0[0],2])
main_circ.cx(1,qreg_0[0])
main_circ.x(2)
main_circ.u(0.433000,param_0,0.864000, qreg_0[0])
main_circ.cx(3,2)
main_circ.u(param_0,param_0,param_1, 2)
main_circ.x(1)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.rz(0.229000, 3)
main_circ.rz(-0.213000, qreg_0[0])
main_circ.u(param_0,-0.215000,-0.730000, 1)
bindings = {param_0: 0.026000, param_1: -0.508000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1613")
