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
subcirc0.rz(0.171000, qreg_0[3])
subcirc0.u(0,0,-0.828000, qreg_0[2])
subcirc0.u(0,0,0.944000, qreg_0[2])
subcirc0.rz(-0.574000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.rz(0.009000, qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_1[1])
subcirc1.rz(0.456000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2.u(0,0,0.622000, qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[3])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(-0.691000, qreg_0[2])
subcirc3.u(0,0,0.269000, qreg_0[1])
subcirc3.u(0,0,0.036000, qreg_0[1])
subcirc3.rz(-0.633000, qreg_0[3])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rz(0.973000, 1)
main_circ.append(subcirc3,[qreg_0[3],qreg_0[0],0,qreg_0[1]])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.rz(param_0, qreg_0[2])
main_circ.cy(0,qreg_0[2])
main_circ.append(subcirc3,[qreg_0[3],0,1,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[2],1])
main_circ.cy(0,qreg_0[0])
main_circ.cz(qreg_0[3],1)
main_circ.append(subcirc0,[1,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.cy(1,0)
main_circ.append(subcirc0,[1,qreg_0[1],0,qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[3],0,qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],0,1])
main_circ.cy(qreg_0[2],1)
main_circ.cy(1,qreg_0[1])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.cy(qreg_0[3],1)
main_circ.cy(qreg_0[1],0)
main_circ.cy(qreg_0[1],1)
main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],1,0,qreg_0[3]])
bindings = {param_0: -0.888000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
