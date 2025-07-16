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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.u(0,0,-0.256000, qreg_0[3])
subcirc0.s(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.u(0,0,0.236000, qreg_2[1])
subcirc1.s(qreg_1[0])
subcirc1.s(qreg_2[1])
subcirc1.u(0,0,0.223000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0,0,-0.239000, qreg_1[2])
subcirc2.u(0,0,-0.913000, qreg_1[2])
subcirc2.cx(qreg_1[2],qreg_1[1])
subcirc2.z(qreg_1[2])
subcirc2.s(qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.s(qreg_0[2])
subcirc3.u(0,0,-0.380000, qreg_0[3])
subcirc3.u(0,0,-0.593000, qreg_0[3])
subcirc3.u(0,0,-0.592000, qreg_0[1])
subcirc3.u(0,0,0.027000, qreg_0[3])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.z(qreg_2[0])
subcirc4.z(qreg_0[0])
subcirc4.z(qreg_2[1])
subcirc4.z(qreg_2[1])
subcirc4.cx(qreg_2[0],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(0,0,param_2, qreg_0[2])
main_circ.append(subcirc1,[1,qreg_0[1],0,qreg_0[3]])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.s(qreg_0[1])
main_circ.u(param_2,0,param_1, qreg_0[3])
main_circ.u(param_2,0,-0.122000, qreg_0[2])
main_circ.append(subcirc3,[0,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.z(1)
main_circ.cx(1,qreg_0[1])
main_circ.u(param_2,0,param_2, qreg_0[3])
main_circ.s(qreg_0[0])
main_circ.append(subcirc3,[1,qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[2],1,0,qreg_0[3],qreg_0[1]])
main_circ.u(param_2,param_1,param_0, qreg_0[1])
main_circ.u(param_1,param_0,param_0, qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[3])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,qreg_0[2],qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],1,qreg_0[0]])
main_circ.cx(1,qreg_0[1])
main_circ.cx(0,qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(1,qreg_0[1])
main_circ.cx(1,qreg_0[3])
main_circ.cx(qreg_0[0],0)
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[1],0)
main_circ.append(subcirc3,[qreg_0[0],qreg_0[3],qreg_0[2],1])
main_circ.cx(qreg_0[3],qreg_0[2])
bindings = {param_0: 0.447000, param_1: -0.453000, param_2: -0.413000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1719")
