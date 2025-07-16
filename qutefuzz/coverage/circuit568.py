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
subcirc0.rx(-0.077000, qreg_3[0])
subcirc0.u(pi/2,-0.995000,0.120000, qreg_0[1])
subcirc0.s(qreg_2[0])
subcirc0.rx(0.273000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[2])
subcirc1.s(qreg_0[3])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.cx(qreg_0[3],qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[0,qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[3],qreg_0[1]])
main_circ.rx(param_4, qreg_0[2])
main_circ.rx(-0.336000, qreg_0[2])
main_circ.u(param_3,-0.013000,0.698000, 0)
main_circ.s(qreg_0[0])
main_circ.rx(-0.002000, qreg_0[2])
main_circ.rx(-0.884000, qreg_0[0])
main_circ.rx(0.232000, qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[2],0])
main_circ.u(pi/2,0.682000,param_0, 0)
main_circ.s(qreg_0[0])
main_circ.u(pi/2,param_0,0.104000, qreg_0[2])
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[0],qreg_0[3]])
main_circ.cx(qreg_0[3],0)
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[0],0)
main_circ.cx(qreg_0[0],0)
main_circ.cx(qreg_0[2],0)
main_circ.cx(0,qreg_0[3])
main_circ.s(qreg_0[3])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.cx(qreg_0[3],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.u(param_3,param_1,param_1, 0)
main_circ.cx(qreg_0[1],0)
bindings = {param_0: -0.625000, param_1: -0.832000, param_3: -0.234000, param_4: -0.082000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
