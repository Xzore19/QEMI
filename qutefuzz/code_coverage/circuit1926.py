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
subcirc0.h(qreg_0[1])
subcirc0.u(0,0,0.337000, qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.u(0,0,0.411000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.u(0,0,-0.426000, qreg_3[0])
subcirc1.u(0,0,-0.607000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.009000, qreg_3[0])
subcirc2.y(qreg_0[1])
subcirc2.y(qreg_0[1])
subcirc2.cx(qreg_0[2],qreg_0[0])
subcirc2.y(qreg_0[2])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[1,2,qreg_0[0],0])
main_circ.cx(2,0)
main_circ.append(subcirc1,[3,1,0,2])
main_circ.cx(qreg_0[0],2)
main_circ.y(3)
main_circ.append(subcirc1,[qreg_0[0],2,0,3])
main_circ.append(subcirc0,[2,3,1,qreg_0[0]])
main_circ.y(2)
main_circ.h(0)
main_circ.h(2)
main_circ.h(2)
main_circ.append(subcirc1,[qreg_0[0],1,2,0])
main_circ.append(subcirc0,[1,0,qreg_0[0],2])
main_circ.y(3)
main_circ.cx(1,0)
main_circ.append(subcirc1,[3,2,0,qreg_0[0]])
main_circ.u(param_5,param_2,param_4, 3)
main_circ.cx(qreg_0[0],1)
main_circ.append(subcirc1,[3,qreg_0[0],2,1])
main_circ.u(param_0,param_2,param_1, 2)
bindings = {param_0: 0.987000, param_1: 0.799000, param_2: 0.301000, param_4: -0.801000, param_5: -0.027000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1926")
