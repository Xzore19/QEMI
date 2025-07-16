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
subcirc0.rx(0.878000, qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0.ry(-0.427000, qreg_0[1])
subcirc0.cy(qreg_2[0],qreg_3[0])
subcirc0.ry(-0.161000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.996000, qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.x(qreg_0[3])
subcirc1.ry(0.997000, qreg_0[3])
subcirc1.ry(0.245000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.311000, qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.ry(0.934000, qreg_0[1])
subcirc2.ry(-0.316000, qreg_0[2])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.x(qreg_0[2])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.ry(0.377000, qreg_0[3])
main_circ.rx(0.018000, qreg_0[3])
main_circ.ry(param_2, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],1,qreg_0[3],0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],1,qreg_0[3],qreg_0[2]])
main_circ.append(subcirc0,[1,qreg_0[3],0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1],1])
main_circ.rx(param_0, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],1,qreg_0[2],qreg_0[1]])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.cy(qreg_0[2],0)
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(0,qreg_0[0])
main_circ.cy(1,0)
main_circ.cy(qreg_0[0],1)
main_circ.x(qreg_0[3])
main_circ.append(subcirc2,[0,qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
bindings = {param_0: 0.338000, param_2: -0.139000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
