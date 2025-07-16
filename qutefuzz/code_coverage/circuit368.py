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
subcirc0.z(qreg_0[1])
subcirc0.u(0,0,-0.918000, qreg_0[1])
subcirc0.u(0,0,0.057000, qreg_0[1])
subcirc0.u(0,0,-0.078000, qreg_0[3])
subcirc0.ry(0.471000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,0.218000, qreg_0[1])
subcirc1.z(qreg_0[1])
subcirc1.h(qreg_0[3])
subcirc1.ry(-0.941000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(0.093000, qreg_0[2])
subcirc2.ry(0.699000, qreg_0[1])
subcirc2.ry(0.227000, qreg_0[1])
subcirc2.h(qreg_0[2])
subcirc2.u(0,0,1.000000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_0[1])
subcirc3.u(0,0,-0.436000, qreg_2[1])
subcirc3.u(0,0,0.380000, qreg_2[1])
subcirc3.h(qreg_2[0])
subcirc3.z(qreg_2[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.z(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.h(qreg_1[0])
main_circ.z(2)
main_circ.h(0)
main_circ.append(subcirc1,[3,2,0,qreg_1[0],qreg_0[0]])
main_circ.h(2)
main_circ.append(subcirc1,[qreg_0[0],3,2,1,qreg_1[0]])
main_circ.append(subcirc2,[1,qreg_1[0],3,2,0,qreg_0[0]])
main_circ.append(subcirc1,[3,1,qreg_0[0],2,0])
main_circ.h(2)
main_circ.ry(param_1, 0)
main_circ.append(subcirc1,[3,2,qreg_0[0],qreg_1[0],1])
main_circ.h(1)
main_circ.h(3)
main_circ.append(subcirc1,[qreg_1[0],0,qreg_0[0],1,3])
main_circ.ry(0.291000, 1)
main_circ.append(subcirc1,[qreg_1[0],0,qreg_0[0],1,3])
main_circ.append(subcirc1,[0,qreg_0[0],2,3,1])
main_circ.u(0,0,0.156000, 1)
main_circ.z(0)
main_circ.ry(0.295000, 3)
main_circ.z(qreg_0[0])
main_circ.u(param_3,param_3,param_2, 0)
bindings = {param_1: -0.535000, param_2: 0.561000, param_3: 0.204000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "368")
