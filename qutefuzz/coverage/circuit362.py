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
subcirc0.s(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.u(0.632000,-0.484000,0.115000, qreg_2[0])
subcirc0.y(qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[3])
subcirc1.x(qreg_0[3])
subcirc1.u(0.504000,-0.651000,-0.948000, qreg_0[3])
subcirc1.y(qreg_0[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.s(qreg_0[0])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.u(param_0,-0.267000,param_0, 0)
main_circ.x(0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.y(qreg_0[2])
main_circ.x(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],0])
main_circ.u(-0.710000,-0.963000,-0.810000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],0,qreg_0[1]])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],0])
main_circ.u(param_0,-0.405000,-0.015000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_3[0],0])
bindings = {param_0: 0.233000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "362")
