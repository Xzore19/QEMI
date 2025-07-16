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
subcirc0.s(qreg_0[1])
subcirc0.u(0,0,-0.748000, qreg_0[0])
subcirc0.u(0,0,0.146000, qreg_3[0])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_3[0])
subcirc0.u(0,0,0.284000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_1[1],qreg_0[0])
subcirc1.u(0,0,0.323000, qreg_3[0])
subcirc1.u(0,0,-0.663000, qreg_0[0])
subcirc1.h(qreg_1[0])
subcirc1.u(0,0,0.741000, qreg_0[0])
subcirc1.u(0,0,-0.070000, qreg_1[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.s(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.u(0,0,0.694000, qreg_2[0])
main_circ.cx(qreg_0[1],0)
main_circ.u(0,param_1,0.774000, qreg_2[1])
main_circ.s(qreg_0[0])
main_circ.h(0)
main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_0[1]])
main_circ.cx(qreg_0[1],0)
main_circ.s(qreg_2[0])
main_circ.cx(qreg_0[1],qreg_2[1])
main_circ.s(0)
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_2[1],0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_2[1]])
main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],0,qreg_0[1]])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_2[0],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_2[1])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.cx(0,qreg_2[1])
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.cx(qreg_0[0],qreg_2[0])
main_circ.cx(0,qreg_2[1])
bindings = {param_1: 0.665000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "521")
