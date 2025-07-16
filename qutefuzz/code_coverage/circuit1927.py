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
subcirc0.h(qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(0.726000, qreg_2[1])
subcirc0.h(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,param_0,0.585000, qreg_0[1])
main_circ.rz(-0.890000, qreg_0[2])
main_circ.s(qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[0],qreg_0[3],1,qreg_0[1]])
main_circ.u(0,param_1,param_0, qreg_0[1])
main_circ.u(param_0,param_1,param_1, 0)
main_circ.rz(-0.281000, qreg_0[2])
main_circ.s(qreg_0[3])
main_circ.h(0)
main_circ.rz(param_0, 1)
main_circ.u(0,param_0,-0.638000, qreg_0[0])
main_circ.u(0,0,-0.195000, 0)
main_circ.h(qreg_0[3])
main_circ.s(qreg_0[0])
main_circ.rz(0.381000, qreg_0[3])
main_circ.s(1)
main_circ.h(0)
main_circ.u(0,param_0,-0.460000, qreg_0[3])
main_circ.rz(param_1, qreg_0[0])
main_circ.u(0,param_1,param_0, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],1,0,qreg_0[3],qreg_0[1]])
main_circ.u(param_1,param_0,-0.796000, qreg_0[0])
main_circ.s(qreg_0[2])
main_circ.rz(0.400000, qreg_0[1])
main_circ.rz(-0.121000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,1,qreg_0[3],qreg_0[2]])
main_circ.s(0)
main_circ.h(1)
main_circ.rz(param_1, qreg_0[2])
main_circ.h(1)
main_circ.u(0,param_1,0.346000, qreg_0[2])
bindings = {param_0: -0.762000, param_1: 0.067000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
