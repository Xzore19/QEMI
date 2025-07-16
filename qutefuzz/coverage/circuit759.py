from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.u(pi/2,-0.333000,-0.046000, qreg_0[2])
subcirc0.ry(-0.787000, qreg_0[2])
subcirc0.x(qreg_0[0])
subcirc0.u(pi/2,-0.689000,0.911000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.536000,-0.048000, qreg_1[1])
subcirc1.x(qreg_1[1])
subcirc1.u(pi/2,-0.401000,0.596000, qreg_1[1])
subcirc1.u(pi/2,-0.797000,0.375000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.527000, qreg_3[0])
subcirc2.ry(-0.779000, qreg_1[0])
subcirc2.x(qreg_0[0])
subcirc2.ry(0.615000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.x(qreg_0[1])
subcirc3.u(pi/2,0.877000,-0.038000, qreg_0[0])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.ry(-0.149000, qreg_0[1])

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

main_circ.cy(3,1)
main_circ.append(subcirc3,[3,qreg_0[0],2,1])
main_circ.ry(param_0, qreg_0[0])
main_circ.u(param_0,param_0,0.436000, 1)
main_circ.append(subcirc0,[3,qreg_0[0],0,1])
main_circ.append(subcirc0,[qreg_0[0],0,2,1])
main_circ.append(subcirc1,[2,qreg_0[0],3,0,1])
main_circ.append(subcirc1,[2,qreg_0[0],1,3,0])
main_circ.append(subcirc3,[2,1,3,0])
main_circ.append(subcirc1,[qreg_0[0],2,1,3,0])
main_circ.append(subcirc1,[3,0,2,1,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],2,1,3])
main_circ.ry(0.196000, qreg_0[0])
main_circ.cy(1,0)
main_circ.cy(2,1)
main_circ.cy(1,qreg_0[0])
main_circ.cy(3,2)
main_circ.cy(3,qreg_0[0])
main_circ.cy(1,2)
main_circ.cy(1,0)
main_circ.cy(2,1)
main_circ.cy(1,0)
main_circ.cy(3,1)
main_circ.cy(qreg_0[0],1)
main_circ.cy(1,3)
main_circ.cy(1,3)
main_circ.cy(0,2)
main_circ.x(3)
main_circ.x(3)
bindings = {param_0: 0.577000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
