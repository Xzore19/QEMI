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
subcirc0.u(0,0,-0.328000, qreg_0[0])
subcirc0.u(0.751000,-0.441000,0.676000, qreg_0[2])
subcirc0.u(0.381000,0.545000,0.507000, qreg_0[0])
subcirc0.u(0,0,0.708000, qreg_0[1])
subcirc0.u(0.883000,-0.814000,-0.976000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.u(0.189000,-0.948000,-0.324000, qreg_2[0])
subcirc1.y(qreg_0[1])
subcirc1.x(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.u(0,0,0.431000, qreg_2[0])
subcirc2.u(0,0,-0.796000, qreg_0[1])
subcirc2.y(qreg_0[1])
subcirc2.x(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.x(qreg_0[3])
subcirc3.u(0,0,-0.527000, qreg_0[1])
subcirc3.x(qreg_0[3])
subcirc3.u(0,0,-0.903000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

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

main_circ.x(1)
main_circ.x(3)
main_circ.append(subcirc0,[0,qreg_0[0],1,3])
main_circ.append(subcirc0,[3,0,2,qreg_0[0]])
main_circ.u(param_1,0,param_2, 3)
main_circ.append(subcirc0,[0,3,qreg_0[0],2])
main_circ.y(0)
main_circ.append(subcirc0,[qreg_0[0],3,0,1])
main_circ.append(subcirc2,[0,1,3,qreg_0[0],2])
main_circ.u(param_2,param_1,-0.992000, 1)
main_circ.u(param_0,0,-0.993000, 0)
main_circ.append(subcirc2,[2,3,1,qreg_0[0],0])
main_circ.u(0,0,0.478000, 3)
main_circ.u(param_1,param_1,param_0, qreg_0[0])
main_circ.append(subcirc2,[1,qreg_0[0],2,3,0])
main_circ.append(subcirc0,[1,3,0,qreg_0[0]])
main_circ.u(param_0,param_1,param_2, 3)
main_circ.u(-0.330000,0.059000,param_1, 0)
bindings = {param_0: 0.675000, param_1: -0.826000, param_2: -0.577000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1537")
