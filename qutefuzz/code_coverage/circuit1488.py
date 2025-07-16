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
subcirc0.x(qreg_2[1])
subcirc0.x(qreg_2[0])
subcirc0.x(qreg_2[0])
subcirc0.u(-0.206000,-0.193000,-0.606000, qreg_2[0])
subcirc0.x(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,-0.951000,0.669000, qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.u(-0.176000,0.539000,-0.025000, qreg_2[0])
subcirc1.x(qreg_2[1])
subcirc1.x(qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[2])
subcirc2.u(-0.865000,0.399000,-0.731000, qreg_0[1])
subcirc2.z(qreg_0[2])
subcirc2.u(0.171000,0.647000,0.461000, qreg_0[3])
subcirc2.u(-0.692000,0.540000,-0.549000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(pi/2,0.485000,-0.520000, qreg_2[0])
subcirc3.u(0.236000,0.957000,0.218000, qreg_2[1])
subcirc3.z(qreg_2[0])
subcirc3.u(0.516000,0.588000,0.981000, qreg_0[1])
subcirc3.u(-0.747000,0.734000,0.068000, qreg_0[0])

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.z(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_0[2]])
main_circ.x(qreg_3[0])
main_circ.u(0.443000,param_2,param_1, qreg_0[2])
main_circ.z(0)
main_circ.u(pi/2,-0.885000,0.248000, qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.append(subcirc3,[qreg_0[1],0,qreg_3[0],qreg_0[0]])
main_circ.append(subcirc2,[0,qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,qreg_0[2]])
main_circ.u(param_0,param_1,0.245000, qreg_3[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[0],0])
main_circ.u(param_2,-0.691000,param_0, 0)
main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],0,qreg_3[0]])
main_circ.append(subcirc3,[qreg_0[0],qreg_3[0],qreg_0[2],0])
main_circ.u(-0.651000,param_2,param_0, qreg_3[0])
main_circ.u(pi/2,0.494000,param_0, qreg_3[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1],0])
main_circ.u(param_2,param_1,param_1, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.u(param_2,-0.801000,0.768000, qreg_3[0])
main_circ.u(-0.928000,0.071000,-0.038000, qreg_3[0])
bindings = {param_0: -0.245000, param_1: -0.407000, param_2: 0.960000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1488")
