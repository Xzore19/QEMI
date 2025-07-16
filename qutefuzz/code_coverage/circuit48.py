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
subcirc0.cz(qreg_0[0],qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_3[0])
subcirc0.y(qreg_0[2])
subcirc0.u(0,0,0.135000, qreg_0[2])
subcirc0.y(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[3])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.u(0,0,-0.625000, qreg_0[0])
subcirc2.u(0,0,0.515000, qreg_0[0])
subcirc2.u(0,0,-0.260000, qreg_0[1])
subcirc2.y(qreg_0[0])
subcirc2.u(0,0,-0.569000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[3])
subcirc3.y(qreg_0[3])
subcirc3.u(0,0,-0.339000, qreg_0[3])
subcirc3.cz(qreg_0[1],qreg_0[3])
subcirc3.u(0,0,-0.860000, qreg_0[3])
subcirc3.cy(qreg_0[3],qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.y(qreg_0[1])
subcirc4.cz(qreg_0[0],qreg_0[1])
subcirc4.cz(qreg_0[3],qreg_0[0])
subcirc4.u(0,0,-0.255000, qreg_0[0])
subcirc4.cy(qreg_0[3],qreg_0[0])
subcirc4.y(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc3,[3,1,0,2])
main_circ.append(subcirc3,[0,1,3,2])
main_circ.u(param_1,param_5,param_1, 0)
main_circ.append(subcirc3,[0,1,3,2])
main_circ.cz(0,3)
main_circ.append(subcirc4,[3,2,0,1])
main_circ.u(param_4,0,param_4, 2)
main_circ.cz(1,2)
main_circ.append(subcirc4,[2,1,3,0])
main_circ.y(0)
main_circ.append(subcirc3,[1,3,0,2])
main_circ.cz(1,0)
bindings = {param_1: 0.181000, param_4: -0.844000, param_5: 0.533000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
