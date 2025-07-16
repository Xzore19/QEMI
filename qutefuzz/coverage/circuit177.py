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
subcirc0.ry(-0.302000, qreg_0[0])
subcirc0.u(0,0,-0.076000, qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_2[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_2[1])
subcirc0.h(qreg_2[1])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.u(param_0,0,-0.424000, qreg_0[0])
main_circ.u(param_0,0,-0.203000, qreg_3[0])
main_circ.cx(qreg_0[0],0)
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0],0])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0],0])
main_circ.h(qreg_0[0])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_0[1],0)
main_circ.ry(0.975000, qreg_0[0])
main_circ.h(0)
main_circ.cx(qreg_0[1],0)
main_circ.ry(0.714000, qreg_2[0])
main_circ.cx(qreg_2[0],qreg_0[0])
main_circ.append(subcirc0,[0,qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.cx(qreg_2[0],0)
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.ry(param_0, qreg_3[0])
main_circ.ry(param_4, qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.u(param_3,0,0.791000, qreg_0[0])
main_circ.ry(param_3, qreg_2[0])
main_circ.cx(qreg_2[0],qreg_3[0])
main_circ.h(0)
bindings = {param_0: 0.131000, param_3: 0.300000, param_4: 0.011000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
