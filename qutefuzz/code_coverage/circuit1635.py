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
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.u(0.944000,-0.472000,-0.473000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.u(-0.403000,0.757000,-0.761000, qreg_0[1])
subcirc1.h(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.804000,-0.334000,0.884000, qreg_0[0])
subcirc2.u(0.980000,-0.698000,-0.898000, qreg_3[0])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2.u(-0.410000,-0.332000,-0.851000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.h(qreg_0[1])
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.h(qreg_0[0])
subcirc4.cy(qreg_2[0],qreg_2[1])
subcirc4.cy(qreg_0[0],qreg_2[0])
subcirc4.cy(qreg_1[0],qreg_2[1])

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

main_circ.append(subcirc1,[2,3,qreg_0[0],0])
main_circ.append(subcirc0,[3,2,0,1,qreg_0[0]])
main_circ.append(subcirc0,[0,3,2,1,qreg_0[0]])
main_circ.h(3)
main_circ.h(1)
main_circ.cz(2,0)
main_circ.h(3)
main_circ.append(subcirc2,[2,3,1,0])
main_circ.cz(2,1)
main_circ.append(subcirc1,[0,3,qreg_0[0],1])
main_circ.append(subcirc4,[2,1,3,qreg_0[0]])
main_circ.h(1)
main_circ.append(subcirc2,[2,3,qreg_0[0],0])
main_circ.append(subcirc1,[2,0,1,qreg_0[0]])
main_circ.append(subcirc0,[2,0,1,3,qreg_0[0]])
main_circ.cz(qreg_0[0],1)
main_circ.u(0.610000,param_1,param_0, 3)
main_circ.cy(0,1)
bindings = {param_0: -0.535000, param_1: 0.264000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
