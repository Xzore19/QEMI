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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.u(pi/2,0.986000,-0.576000, qreg_3[0])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.x(qreg_0[2])
subcirc0.u(pi/2,0.815000,0.962000, qreg_3[0])
subcirc0.x(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[2])
subcirc2.z(qreg_0[1])
subcirc2.u(pi/2,0.706000,-0.812000, qreg_0[1])
subcirc2.u(pi/2,0.768000,0.042000, qreg_0[3])
subcirc2.x(qreg_0[3])
subcirc2.cx(qreg_0[2],qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.z(qreg_1[2])
subcirc3.z(qreg_1[2])
subcirc3.z(qreg_1[0])
subcirc3.u(pi/2,0.820000,0.937000, qreg_0[0])
subcirc3.cx(qreg_0[0],qreg_1[2])
subcirc3.z(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_1[1])
subcirc4.x(qreg_0[0])
subcirc4.u(pi/2,-0.516000,-0.914000, qreg_1[0])
subcirc4.u(pi/2,-0.461000,-0.055000, qreg_0[0])
subcirc4.x(qreg_1[1])
subcirc4.cx(qreg_0[0],qreg_1[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,-0.639000,param_1, qreg_1[1])
main_circ.u(param_1,param_1,param_1, qreg_3[0])
main_circ.z(qreg_1[1])
main_circ.x(qreg_1[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_1[1],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],qreg_1[1],qreg_3[0]])
main_circ.z(qreg_1[0])
main_circ.append(subcirc1,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.x(qreg_3[0])
main_circ.append(subcirc1,[qreg_1[1],qreg_1[0],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc1,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.u(param_1,param_0,param_0, qreg_0[0])
main_circ.append(subcirc4,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.z(qreg_3[0])
main_circ.append(subcirc1,[qreg_1[0],qreg_3[0],qreg_1[1],qreg_0[0]])
main_circ.x(qreg_1[1])
main_circ.z(qreg_0[0])
main_circ.u(param_1,-0.655000,param_1, qreg_1[0])
bindings = {param_0: 0.309000, param_1: 0.170000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "623")
