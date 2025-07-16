from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,0.485000, qreg_0[0])
subcirc0.ry(-0.322000, qreg_0[0])
subcirc0.u(0,0,-0.806000, qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.102000,-0.246000,-0.249000, qreg_0[3])
subcirc1.ry(-0.137000, qreg_0[2])
subcirc1.cz(qreg_0[2],qreg_0[3])
subcirc1.u(0,0,0.667000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.010000, qreg_3[0])
subcirc2.ry(0.371000, qreg_3[0])
subcirc2.u(-0.626000,-0.987000,-0.588000, qreg_3[0])
subcirc2.cz(qreg_0[0],qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.030000,0.398000,0.984000, qreg_0[0])
subcirc3.u(0,0,0.254000, qreg_0[1])
subcirc3.ry(0.727000, qreg_0[2])
subcirc3.u(-0.335000,-0.266000,0.057000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[2,1,3,0])
main_circ.u(param_1,param_1,0.192000, 2)
main_circ.append(subcirc2,[qreg_0[0],0,3,2])
main_circ.u(param_1,0.075000,param_1, 2)
main_circ.append(subcirc3,[qreg_1[0],2,1,0,3,qreg_0[0]])
main_circ.ry(param_0, qreg_0[0])
main_circ.u(param_0,0.415000,-0.756000, 1)
main_circ.append(subcirc1,[qreg_0[0],2,qreg_1[0],0])
main_circ.append(subcirc2,[2,0,qreg_1[0],qreg_0[0]])
main_circ.append(subcirc1,[2,0,qreg_1[0],qreg_0[0]])
main_circ.cz(1,qreg_0[0])
main_circ.cz(3,qreg_0[0])
main_circ.cz(qreg_1[0],3)
main_circ.cz(0,3)
main_circ.cz(qreg_0[0],0)
main_circ.cz(2,qreg_1[0])
main_circ.cz(3,2)
main_circ.ry(-0.914000, 1)
main_circ.append(subcirc3,[qreg_1[0],1,qreg_0[0],3,0,2])
main_circ.u(param_1,param_1,param_0, 2)
bindings = {param_0: -0.589000, param_1: 0.186000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
