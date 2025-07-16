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
subcirc0.s(qreg_0[0])
subcirc0.rx(-0.791000, qreg_0[1])
subcirc0.rx(0.730000, qreg_2[1])
subcirc0.rx(0.053000, qreg_0[1])
subcirc0.u(0,0,0.825000, qreg_0[1])

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
subcirc1.u(-0.350000,-0.875000,-0.094000, qreg_3[0])
subcirc1.u(0.704000,-0.415000,0.911000, qreg_3[0])
subcirc1.u(0,0,-0.744000, qreg_2[0])
subcirc1.u(0,0,0.013000, qreg_1[0])
subcirc1.rx(-0.883000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.841000, qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.u(0,0,-0.052000, qreg_3[0])
subcirc2.rx(-0.532000, qreg_0[1])
subcirc2.u(0,0,-0.821000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rx(0.370000, qreg_2[1])
subcirc3.s(qreg_2[0])
subcirc3.rx(-0.328000, qreg_0[1])
subcirc3.u(-0.320000,-0.380000,-0.973000, qreg_2[0])
subcirc3.rx(0.363000, qreg_2[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,0.812000, qreg_2[0])
subcirc4.s(qreg_2[0])
subcirc4.u(0,0,-0.916000, qreg_0[1])
subcirc4.u(-0.597000,-0.487000,0.484000, qreg_0[0])
subcirc4.s(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rx(param_1, qreg_3[0])
main_circ.rx(-0.864000, qreg_0[1])
main_circ.u(param_0,0,0.888000, qreg_0[1])
main_circ.rx(-0.079000, qreg_0[2])
main_circ.u(0,param_1,param_1, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],0])
main_circ.u(param_0,-0.186000,param_0, qreg_0[2])
main_circ.u(param_0,param_1,-0.647000, qreg_0[0])
main_circ.rx(param_0, qreg_3[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],0,qreg_0[2]])
main_circ.s(qreg_0[0])
main_circ.u(-0.744000,param_1,-0.073000, qreg_0[2])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_0[1],qreg_3[0]])
main_circ.u(param_0,param_1,param_1, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],0,qreg_3[0],qreg_0[0]])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.u(param_0,-0.428000,0.311000, qreg_3[0])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_3[0],0])
main_circ.rx(-0.698000, qreg_0[2])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],0,qreg_3[0]])
main_circ.u(param_1,param_1,param_0, qreg_0[2])
bindings = {param_0: 0.784000, param_1: 0.882000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
