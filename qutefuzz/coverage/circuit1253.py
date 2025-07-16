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
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.x(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.126000,-0.177000, qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,0.216000,0.806000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.x(qreg_0[2])
subcirc2.y(qreg_0[1])
subcirc2.z(qreg_0[3])
subcirc2.u(pi/2,0.306000,-0.252000, qreg_0[3])
subcirc2.z(qreg_0[3])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.y(qreg_1[0])
subcirc3.u(pi/2,0.010000,-0.156000, qreg_0[0])
subcirc3.z(qreg_1[1])
subcirc3.u(pi/2,0.489000,-0.109000, qreg_1[2])
subcirc3.y(qreg_1[2])
subcirc3.x(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.z(qreg_0[0])
subcirc4.x(qreg_0[1])
subcirc4.u(pi/2,-0.788000,0.956000, qreg_0[0])
subcirc4.y(qreg_0[0])
subcirc4.x(qreg_0[0])
subcirc4.y(qreg_0[3])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[qreg_0[1],3,1,2,0,qreg_0[0]])
main_circ.append(subcirc1,[2,1,qreg_0[1],qreg_0[0],3,0])
main_circ.x(2)
main_circ.u(pi/2,param_0,param_3, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],2])
main_circ.u(pi/2,0.894000,-0.912000, 3)
main_circ.x(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.z(2)
main_circ.u(param_1,0.923000,param_3, qreg_0[0])
main_circ.u(param_2,param_0,0.839000, 1)
main_circ.u(param_1,param_2,-0.081000, 2)
main_circ.append(subcirc1,[2,qreg_0[0],1,0,3,qreg_0[1]])
main_circ.z(3)
main_circ.append(subcirc1,[qreg_0[1],3,1,2,0,qreg_0[0]])
main_circ.append(subcirc0,[3,1,0,qreg_0[1]])
main_circ.y(3)
main_circ.y(0)
main_circ.append(subcirc1,[3,2,qreg_0[1],0,qreg_0[0],1])
main_circ.x(2)
main_circ.x(0)
main_circ.u(pi/2,param_0,param_0, 1)
main_circ.u(param_1,0.347000,0.315000, 0)
bindings = {param_0: 0.935000, param_1: -0.761000, param_2: -0.151000, param_3: 0.421000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
