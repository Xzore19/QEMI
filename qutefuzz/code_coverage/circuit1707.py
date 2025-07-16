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
subcirc0.rx(-0.208000, qreg_1[1])
subcirc0.h(qreg_3[0])
subcirc0.rx(-0.919000, qreg_1[1])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.cz(qreg_0[3],qreg_0[2])
subcirc1.x(qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_3[0])
subcirc2.rx(0.598000, qreg_0[2])
subcirc2.cz(qreg_3[0],qreg_0[1])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_2[1],0])
main_circ.cz(qreg_2[0],0)
main_circ.cz(0,qreg_0[1])
main_circ.x(0)
main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],0,1])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.rx(param_2, qreg_2[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[1],1])
main_circ.rx(param_2, 0)
main_circ.rx(-0.550000, qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.x(qreg_2[1])
bindings = {param_2: 0.985000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1707")
