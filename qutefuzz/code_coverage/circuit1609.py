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
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.ry(-0.333000, qreg_3[0])
subcirc0.ry(-0.888000, qreg_2[0])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0.ry(0.664000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.cx(qreg_2[0],qreg_3[0])
subcirc1.cx(qreg_2[0],qreg_3[0])
subcirc1.cx(qreg_2[0],qreg_3[0])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.u(-0.704000,0.566000,-0.426000, qreg_2[0])
subcirc2.u(0.174000,-0.623000,-0.972000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.539000,0.605000,-0.564000, qreg_0[0])
subcirc3.ry(0.778000, qreg_2[0])
subcirc3.cx(qreg_3[0],qreg_0[0])
subcirc3.ry(0.959000, qreg_3[0])
subcirc3.ry(0.818000, qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cx(qreg_0[1],qreg_0[2])
subcirc4.cy(qreg_0[2],qreg_0[0])
subcirc4.u(-0.294000,0.800000,0.870000, qreg_0[2])
subcirc4.ry(-0.638000, qreg_0[3])
subcirc4.cx(qreg_0[3],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.ry(0.087000, 2)
main_circ.append(subcirc3,[qreg_0[0],2,3,1])
main_circ.cx(3,0)
main_circ.ry(0.864000, qreg_0[0])
main_circ.cx(3,1)
main_circ.ry(0.206000, 3)
main_circ.cx(qreg_0[0],2)
main_circ.u(0.374000,param_2,param_1, qreg_0[0])
main_circ.ry(param_2, 2)
main_circ.cx(0,3)
main_circ.cx(2,qreg_0[0])
main_circ.ry(0.489000, 1)
main_circ.cy(qreg_0[0],0)
main_circ.cx(2,3)
main_circ.ry(param_3, 0)
main_circ.append(subcirc3,[1,0,3,2])
main_circ.cx(1,3)
main_circ.append(subcirc3,[1,qreg_0[0],2,0])
main_circ.cx(3,1)
main_circ.cy(2,0)
main_circ.ry(-0.623000, qreg_0[0])
main_circ.ry(param_3, qreg_0[0])
main_circ.ry(param_2, 0)
main_circ.u(param_3,param_0,param_3, 0)
main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[0],3)
main_circ.cy(3,qreg_0[0])
main_circ.cx(2,0)
main_circ.u(param_3,param_3,-0.035000, 3)
main_circ.cx(qreg_0[0],1)
main_circ.u(0.657000,0.339000,-0.192000, 0)
main_circ.append(subcirc3,[qreg_0[0],1,0,2])
main_circ.append(subcirc3,[0,qreg_0[0],3,1])
main_circ.ry(0.050000, qreg_0[0])
main_circ.ry(-0.280000, qreg_0[0])
main_circ.u(param_3,param_3,-0.981000, 1)
bindings = {param_0: 0.184000, param_1: -0.512000, param_2: -0.377000, param_3: -0.525000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
