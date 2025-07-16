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
subcirc0.ry(-0.467000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_0[2])
subcirc0.u(0.622000,-0.801000,-0.720000, qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.ry(0.396000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.rz(0.619000, qreg_1[1])
subcirc1.rz(-0.516000, qreg_0[0])
subcirc1.u(-0.327000,-0.272000,0.260000, qreg_1[2])
subcirc1.ry(-0.602000, qreg_1[2])
subcirc1.rz(0.092000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(0.963000, qreg_0[0])
subcirc2.rz(0.011000, qreg_0[2])
subcirc2.rz(-0.945000, qreg_0[2])
subcirc2.rz(-0.281000, qreg_0[3])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[2],qreg_0[3])
subcirc3.rz(0.696000, qreg_0[0])
subcirc3.u(0.014000,-0.779000,-0.761000, qreg_0[3])
subcirc3.ry(0.823000, qreg_0[0])
subcirc3.ry(-0.448000, qreg_0[1])

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
param_3 = Parameter("param_3")

main_circ.rz(param_2, 2)
main_circ.rz(param_2, 0)
main_circ.ry(param_0, 3)
main_circ.u(param_1,0.099000,-0.615000, qreg_0[0])
main_circ.append(subcirc3,[2,qreg_0[0],3,1])
main_circ.cz(0,qreg_0[0])
main_circ.rz(-0.161000, qreg_0[0])
main_circ.append(subcirc3,[3,0,2,1])
main_circ.cz(2,1)
main_circ.ry(param_0, 3)
main_circ.ry(param_0, 3)
main_circ.u(param_2,-0.847000,param_0, 0)
main_circ.cz(1,3)
main_circ.append(subcirc2,[qreg_0[0],0,1,2,3])
main_circ.append(subcirc3,[qreg_0[0],2,1,0])
main_circ.append(subcirc3,[0,3,qreg_0[0],2])
main_circ.ry(-0.342000, 1)
main_circ.rz(0.041000, qreg_0[0])
main_circ.u(-0.153000,param_0,param_0, 2)
main_circ.cz(2,qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],3,0,1,2])
main_circ.cz(qreg_0[0],3)
main_circ.cz(0,1)
main_circ.cz(1,0)
main_circ.cz(1,qreg_0[0])
main_circ.cz(2,3)
main_circ.cz(2,3)
main_circ.cz(qreg_0[0],1)
main_circ.cz(1,0)
main_circ.u(param_3,0.148000,param_3, 1)
main_circ.append(subcirc2,[qreg_0[0],3,0,1,2])
main_circ.cz(qreg_0[0],0)
bindings = {param_0: 0.128000, param_1: 0.199000, param_2: -0.270000, param_3: -0.222000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
