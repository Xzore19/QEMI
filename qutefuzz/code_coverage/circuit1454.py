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
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.ry(0.604000, qreg_0[0])
subcirc0.u(-0.043000,0.703000,0.661000, qreg_2[0])
subcirc0.ry(0.268000, qreg_2[0])
subcirc0.u(-0.351000,-0.470000,0.106000, qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.x(qreg_1[2])
subcirc1.cy(qreg_1[1],qreg_1[0])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.cy(qreg_1[0],qreg_1[1])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0.627000,0.019000,-0.772000, qreg_0[3])
subcirc2.ry(-0.617000, qreg_0[0])
subcirc2.u(-0.722000,-0.549000,-0.543000, qreg_0[3])
subcirc2.x(qreg_0[3])
subcirc2.x(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.085000, qreg_0[0])
subcirc3.cy(qreg_0[2],qreg_0[1])
subcirc3.x(qreg_0[1])
subcirc3.x(qreg_3[0])
subcirc3.x(qreg_3[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.489000,-0.482000,0.290000, qreg_0[2])
subcirc4.ry(0.109000, qreg_3[0])
subcirc4.cy(qreg_0[1],qreg_3[0])
subcirc4.x(qreg_3[0])
subcirc4.ry(-0.563000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

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
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[2,0,3,1])
main_circ.ry(0.881000, qreg_0[0])
main_circ.append(subcirc0,[2,qreg_0[0],0,1])
main_circ.append(subcirc0,[2,1,0,qreg_0[0]])
main_circ.ry(param_0, 2)
main_circ.x(0)
main_circ.cy(qreg_0[0],2)
main_circ.append(subcirc1,[qreg_0[0],3,0,1])
main_circ.append(subcirc1,[3,qreg_0[0],1,2])
main_circ.x(0)
main_circ.x(3)
main_circ.ry(-0.618000, qreg_0[0])
main_circ.ry(param_3, 2)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.append(subcirc0,[2,1,qreg_0[0],3])
main_circ.u(-0.356000,-0.260000,param_0, 1)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.append(subcirc1,[3,1,0,qreg_0[0]])
main_circ.ry(-0.552000, 0)
main_circ.ry(0.651000, 1)
bindings = {param_0: 0.342000, param_3: 0.212000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
