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
subcirc0.u(-0.598000,-0.441000,0.366000, qreg_1[1])
subcirc0.ry(-0.188000, qreg_1[1])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.886000, qreg_0[0])
subcirc1.rz(0.933000, qreg_3[0])
subcirc1.rz(0.999000, qreg_3[0])
subcirc1.rz(0.606000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.rz(0.597000, qreg_0[2])
subcirc2.y(qreg_3[0])
subcirc2.rz(0.293000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.y(qreg_1[1])
subcirc3.u(0.657000,0.862000,-0.401000, qreg_0[0])
subcirc3.ry(-0.286000, qreg_1[2])
subcirc3.rz(-0.287000, qreg_1[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.append(subcirc0,[1,0,qreg_0[0],qreg_2[1],qreg_0[1]])
main_circ.rz(0.894000, qreg_0[1])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],0,qreg_0[1],qreg_2[1],1])
main_circ.y(qreg_2[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_2[1],qreg_0[0],0])
main_circ.append(subcirc3,[qreg_0[0],0,1,qreg_2[0]])
main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_2[0],0,qreg_0[1],1])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.u(param_3,0.701000,-0.272000, qreg_2[0])
main_circ.u(0.560000,param_2,param_3, 0)
main_circ.append(subcirc0,[0,qreg_2[1],qreg_0[0],qreg_2[0],1])
main_circ.append(subcirc2,[1,qreg_0[1],qreg_0[0],0,qreg_2[1],qreg_2[0]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,qreg_2[1],qreg_2[0],1])
main_circ.ry(0.828000, 0)
main_circ.append(subcirc3,[qreg_2[0],qreg_0[0],0,1])
main_circ.u(param_0,-0.772000,param_2, qreg_0[1])
main_circ.y(qreg_2[1])
bindings = {param_0: 0.902000, param_2: 0.430000, param_3: -0.646000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
