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
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,-0.127000, qreg_0[1])
subcirc0.h(qreg_0[3])
subcirc0.cz(qreg_0[3],qreg_0[2])
subcirc0.z(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.u(0,0,-0.754000, qreg_1[0])
subcirc1.cz(qreg_1[1],qreg_1[0])
subcirc1.u(0,0,0.181000, qreg_1[0])
subcirc1.z(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_3[0])
subcirc2.z(qreg_2[0])
subcirc2.z(qreg_0[0])
subcirc2.cz(qreg_0[0],qreg_3[0])
subcirc2.u(0,0,0.101000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.z(3)
main_circ.u(0,param_0,-0.454000, 2)
main_circ.z(0)
main_circ.z(1)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.u(param_0,param_0,param_0, 0)
main_circ.h(3)
main_circ.append(subcirc1,[3,0,2,1])
main_circ.append(subcirc1,[2,3,0,1])
main_circ.cz(2,3)
main_circ.h(1)
main_circ.z(0)
main_circ.append(subcirc1,[1,0,3,2])
main_circ.z(2)
main_circ.z(3)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.z(3)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.append(subcirc1,[1,3,2,0])
main_circ.cz(0,2)
main_circ.cz(3,2)
main_circ.cz(2,3)
main_circ.cz(2,0)
main_circ.cz(3,0)
main_circ.cz(3,0)
main_circ.cz(1,3)
main_circ.cz(1,2)
main_circ.cz(3,0)
main_circ.cz(2,0)
main_circ.cz(1,0)
main_circ.h(3)
main_circ.u(0,param_0,0.157000, 2)
main_circ.h(2)
bindings = {param_0: 0.539000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
