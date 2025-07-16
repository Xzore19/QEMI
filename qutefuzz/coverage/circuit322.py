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
subcirc0.y(qreg_3[0])
subcirc0.u(0.322000,-0.260000,-0.920000, qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.u(pi/2,0.316000,0.183000, qreg_0[1])
subcirc0.u(0.071000,-0.027000,0.925000, qreg_0[0])
subcirc0.u(0.712000,-0.004000,0.531000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.y(qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_0[1])
subcirc1.u(pi/2,0.145000,0.472000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_3[0])
subcirc2.u(-0.787000,0.030000,0.345000, qreg_3[0])
subcirc2.u(pi/2,-0.941000,0.873000, qreg_3[0])
subcirc2.cy(qreg_3[0],qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.u(0.486000,-0.679000,0.913000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(-0.688000,0.782000,-0.604000, qreg_0[0])
subcirc3.u(pi/2,0.290000,-0.184000, qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_2[0])
subcirc3.cy(qreg_2[1],qreg_0[1])
subcirc3.u(0.091000,0.776000,-0.380000, qreg_0[0])
subcirc3.y(qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cy(qreg_1[0],qreg_0[0])
subcirc4.cy(qreg_0[0],qreg_2[0])
subcirc4.cy(qreg_0[0],qreg_2[1])
subcirc4.y(qreg_2[1])
subcirc4.y(qreg_1[0])
subcirc4.y(qreg_2[1])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.u(param_3,0.386000,0.959000, 3)
main_circ.u(param_4,-0.178000,param_1, 3)
main_circ.append(subcirc1,[2,0,3,qreg_0[0],qreg_1[0]])
main_circ.u(pi/2,param_4,param_3, 2)
main_circ.append(subcirc2,[0,1,qreg_1[0],3])
main_circ.u(pi/2,-0.154000,param_4, qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],3,1,qreg_0[0]])
main_circ.u(-0.325000,-0.303000,param_4, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],1,2,3])
main_circ.append(subcirc0,[qreg_1[0],3,qreg_0[0],0,2])
main_circ.cy(2,3)
main_circ.cy(2,qreg_0[0])
main_circ.cy(qreg_0[0],3)
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],0,3,qreg_0[0]])
main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],2,3])
bindings = {param_1: 0.897000, param_3: -0.044000, param_4: -0.250000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
