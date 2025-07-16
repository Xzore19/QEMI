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
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,0.601000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.rx(0.448000, qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.u(0,0,-0.897000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_2[1])
subcirc1.cx(qreg_0[0],qreg_2[1])
subcirc1.u(0,0,-0.190000, qreg_2[0])
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.rx(-0.250000, qreg_0[1])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],0])
main_circ.u(0,0,param_1, qreg_0[2])
main_circ.cx(1,qreg_0[0])
main_circ.cx(qreg_0[1],0)
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[3],1])
main_circ.u(param_0,0,param_2, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],1,qreg_0[0]])
main_circ.h(qreg_0[3])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[2],qreg_0[1]])
main_circ.h(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.rx(0.263000, qreg_0[0])
main_circ.h(0)
main_circ.append(subcirc0,[qreg_0[1],1,0,qreg_0[0]])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(qreg_0[3],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[1]])
main_circ.u(0,param_3,0.039000, qreg_0[3])
main_circ.u(0,param_1,param_4, qreg_0[2])
bindings = {param_0: 0.571000, param_1: 0.139000, param_2: -0.121000, param_3: 0.303000, param_4: -0.434000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "288")
