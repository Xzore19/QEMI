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
subcirc0.y(qreg_0[3])
subcirc0.u(pi/2,0.112000,-0.874000, qreg_0[0])
subcirc0.y(qreg_0[3])
subcirc0.y(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.766000,0.955000, qreg_0[2])
subcirc1.u(0.136000,-0.229000,-0.392000, qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1.u(pi/2,-0.980000,-0.980000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.581000,-0.914000, qreg_1[0])
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_2[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_3[0]])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.u(-0.054000,0.782000,param_0, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],0,qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[1],0])
main_circ.h(qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.u(pi/2,0.742000,-0.677000, qreg_0[2])
main_circ.h(0)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.h(0)
main_circ.u(pi/2,0.025000,param_0, qreg_0[0])
main_circ.u(-0.737000,param_0,-0.968000, qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
bindings = {param_0: 0.311000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "900")
