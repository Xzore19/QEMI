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
subcirc0.x(qreg_3[0])
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0.u(0,0,-0.344000, qreg_2[0])
subcirc0.u(0,0,0.630000, qreg_0[1])
subcirc0.ry(0.186000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.119000, qreg_0[3])
subcirc1.u(0,0,-0.386000, qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.u(0,0,-0.884000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.u(0,0,-0.130000, qreg_0[1])
subcirc2.u(0,0,-0.348000, qreg_0[3])
subcirc2.u(0,0,0.832000, qreg_0[1])
subcirc2.cy(qreg_0[0],qreg_0[3])
subcirc2.u(0,0,0.694000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[2],qreg_0[0])
subcirc3.ry(-0.909000, qreg_0[2])
subcirc3.cy(qreg_0[2],qreg_0[1])
subcirc3.ry(-0.796000, qreg_0[3])
subcirc3.x(qreg_0[2])
subcirc3.u(0,0,0.553000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc1,[0,1,qreg_0[0],2])
main_circ.append(subcirc1,[1,qreg_0[0],3,0])
main_circ.append(subcirc0,[0,3,qreg_0[0],2])
main_circ.append(subcirc0,[3,qreg_0[0],1,0])
main_circ.append(subcirc1,[3,1,qreg_0[0],2])
main_circ.append(subcirc1,[qreg_0[0],1,3,0])
main_circ.cy(2,0)
main_circ.cy(1,2)
main_circ.cy(qreg_0[0],1)
main_circ.append(subcirc1,[0,2,qreg_0[0],3])
main_circ.cy(0,2)
main_circ.ry(param_0, 2)
main_circ.ry(-0.861000, qreg_0[0])
main_circ.u(0,param_1,param_1, 2)
main_circ.x(3)
main_circ.u(param_1,param_1,-0.679000, 0)
bindings = {param_0: -0.500000, param_1: -0.565000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
