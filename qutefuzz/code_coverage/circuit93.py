from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.cz(qreg_1[0],qreg_1[1])
subcirc0.cz(qreg_1[0],qreg_1[2])
subcirc0.u(0,0,0.277000, qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,0.318000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[3])
subcirc1.h(qreg_0[2])
subcirc1.u(0,0,-0.096000, qreg_0[0])
subcirc1.h(qreg_0[2])
subcirc1.h(qreg_0[3])
subcirc1.u(0,0,0.383000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_3[0])
subcirc2.u(0,0,-0.693000, qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_2[0])
subcirc2.y(qreg_2[0])
subcirc2.h(qreg_2[0])
subcirc2.y(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.y(qreg_2[1])
subcirc3.h(qreg_0[0])
subcirc3.y(qreg_2[0])
subcirc3.u(0,0,-0.269000, qreg_2[0])
subcirc3.h(qreg_2[1])
subcirc3.u(0,0,0.629000, qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cz(qreg_0[1],qreg_0[0])
subcirc4.y(qreg_0[3])
subcirc4.h(qreg_0[1])
subcirc4.h(qreg_0[2])
subcirc4.cz(qreg_0[3],qreg_0[0])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc2,[0,3,1,2])
main_circ.cz(2,1)
main_circ.h(2)
main_circ.append(subcirc2,[0,3,2,1])
main_circ.h(1)
main_circ.y(0)
main_circ.append(subcirc3,[3,1,2,0])
main_circ.append(subcirc0,[2,1,0,3])
main_circ.y(3)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.cz(0,1)
main_circ.cz(0,2)
main_circ.cz(3,2)
main_circ.cz(2,0)
main_circ.cz(3,1)
main_circ.cz(3,0)
main_circ.y(3)
main_circ.y(0)
main_circ.y(1)
main_circ.u(param_0,param_0,-0.193000, 1)
main_circ.y(3)
bindings = {param_0: -0.218000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
