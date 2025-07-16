from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0,0,-0.401000, qreg_2[1])
subcirc0.u(-0.147000,0.874000,-0.861000, qreg_2[0])
subcirc0.x(qreg_0[0])
subcirc0.u(0.177000,0.892000,0.378000, qreg_0[0])
subcirc0.x(qreg_2[0])
subcirc0.cy(qreg_0[0],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_2[0])
subcirc1.x(qreg_2[0])
subcirc1.u(0,0,-0.187000, qreg_1[0])
subcirc1.u(0,0,0.019000, qreg_2[1])
subcirc1.cy(qreg_2[0],qreg_2[1])
subcirc1.cy(qreg_0[0],qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.482000,-0.146000,-0.331000, qreg_1[0])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.x(qreg_0[0])
subcirc2.u(0.128000,-0.681000,0.416000, qreg_1[0])
subcirc2.cy(qreg_1[0],qreg_1[1])
subcirc2.u(0,0,0.511000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],0,1])
main_circ.append(subcirc2,[2,1,qreg_1[0],qreg_0[0],0,3])
main_circ.append(subcirc2,[1,qreg_0[0],2,0,3,qreg_1[0]])
main_circ.append(subcirc2,[3,0,2,qreg_1[0],qreg_0[0],1])
main_circ.append(subcirc2,[1,qreg_0[0],0,3,qreg_1[0],2])
main_circ.append(subcirc1,[3,qreg_1[0],1,2])
main_circ.append(subcirc0,[3,2,1,0,qreg_1[0],qreg_0[0]])
main_circ.cy(qreg_0[0],3)
main_circ.cy(1,qreg_0[0])
main_circ.append(subcirc1,[1,3,qreg_0[0],0])
main_circ.u(0,param_2,param_5, 0)
main_circ.append(subcirc1,[2,qreg_0[0],3,qreg_1[0]])
main_circ.u(0.811000,-0.751000,0.193000, 0)
bindings = {param_2: -0.957000, param_5: -0.942000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "211")
