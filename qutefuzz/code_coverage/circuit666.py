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
subcirc0.u(pi/2,-0.627000,0.968000, qreg_0[0])
subcirc0.u(pi/2,0.450000,0.704000, qreg_0[1])
subcirc0.u(0,0,0.251000, qreg_0[0])
subcirc0.rz(0.360000, qreg_0[0])
subcirc0.u(0,0,-0.171000, qreg_0[0])
subcirc0.rz(-0.331000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,-0.430000,0.334000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.u(0,0,-0.675000, qreg_0[0])
subcirc1.u(0,0,-0.264000, qreg_0[2])
subcirc1.u(pi/2,-0.329000,-0.385000, qreg_0[0])
subcirc1.rz(0.379000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.rz(0.520000, qreg_1[2])
subcirc2.u(pi/2,-0.390000,0.953000, qreg_0[0])
subcirc2.u(pi/2,-0.828000,-0.666000, qreg_1[2])
subcirc2.z(qreg_1[1])
subcirc2.z(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,0.004000,-0.223000, qreg_0[1])
subcirc3.u(0,0,0.939000, qreg_0[1])
subcirc3.u(pi/2,0.560000,-0.508000, qreg_0[3])
subcirc3.z(qreg_0[0])
subcirc3.u(pi/2,-0.983000,0.446000, qreg_0[3])
subcirc3.z(qreg_0[3])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.362000,-0.559000, qreg_2[0])
subcirc4.u(0,0,-0.452000, qreg_0[0])
subcirc4.rz(0.489000, qreg_3[0])
subcirc4.z(qreg_2[0])
subcirc4.rz(-0.606000, qreg_0[1])
subcirc4.rz(-0.327000, qreg_0[1])

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

main_circ.append(subcirc4,[2,3,0,1])
main_circ.u(pi/2,param_2,param_1, 1)
main_circ.u(param_3,param_2,param_0, 0)
main_circ.u(0,0,param_2, 0)
main_circ.append(subcirc1,[2,qreg_0[0],3,0])
main_circ.rz(param_2, 3)
main_circ.u(param_1,0.321000,0.746000, 1)
main_circ.append(subcirc1,[1,0,3,2])
main_circ.z(qreg_0[0])
main_circ.append(subcirc3,[1,2,0,3])
main_circ.z(2)
main_circ.rz(0.398000, 3)
main_circ.rz(0.325000, 1)
main_circ.append(subcirc1,[0,3,1,qreg_0[0]])
main_circ.append(subcirc0,[3,0,qreg_0[0],1,2])
main_circ.append(subcirc4,[1,qreg_0[0],2,0])
main_circ.rz(param_2, 1)
main_circ.append(subcirc3,[0,2,3,1])
main_circ.rz(param_0, 2)
main_circ.z(qreg_0[0])
bindings = {param_0: -0.632000, param_1: 0.058000, param_2: -0.630000, param_3: 0.533000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
