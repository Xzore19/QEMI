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
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cy(qreg_1[0],qreg_0[0])
subcirc0.cy(qreg_1[1],qreg_0[0])
subcirc0.u(-0.004000,0.020000,0.264000, qreg_1[1])
subcirc0.cx(qreg_0[0],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_0[2])
subcirc1.u(0.534000,0.243000,0.608000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cx(qreg_2[1],qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.u(0.050000,0.220000,-0.602000, qreg_2[0])
subcirc2.cx(qreg_0[0],qreg_2[1])
subcirc2.cy(qreg_2[0],qreg_2[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[0],qreg_0[1])
subcirc3.z(qreg_2[0])
subcirc3.cx(qreg_2[0],qreg_3[0])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_1[0],qreg_3[0]])
main_circ.u(param_0,-0.408000,param_1, qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.z(qreg_2[0])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.append(subcirc2,[qreg_3[0],qreg_2[0],qreg_1[0],qreg_0[0]])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],qreg_3[0],qreg_2[0]])
main_circ.u(param_0,param_1,param_0, qreg_2[0])
main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.z(qreg_2[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[0],qreg_1[0]])
main_circ.u(param_1,param_0,-0.648000, qreg_3[0])
main_circ.cx(qreg_2[0],qreg_1[0])
bindings = {param_0: -0.108000, param_1: -0.958000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
