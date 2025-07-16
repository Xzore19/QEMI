from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_0[0],qreg_2[0])
subcirc0.u(0,0,-0.110000, qreg_2[0])
subcirc0.cz(qreg_1[0],qreg_2[0])
subcirc0.cz(qreg_3[0],qreg_1[0])
subcirc0.x(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_2[0],qreg_0[1])
subcirc1.x(qreg_2[0])
subcirc1.s(qreg_2[0])
subcirc1.x(qreg_2[1])
subcirc1.s(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_2[1],qreg_0[0])
subcirc2.u(0,0,0.382000, qreg_0[0])
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.u(0,0,0.480000, qreg_2[0])
subcirc2.s(qreg_1[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.599000, qreg_1[0])
subcirc3.cz(qreg_1[0],qreg_3[0])
subcirc3.s(qreg_3[0])
subcirc3.s(qreg_3[0])
subcirc3.u(0,0,-0.615000, qreg_2[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,param_0,param_1, qreg_1[0])
main_circ.x(qreg_0[0])
main_circ.cz(qreg_2[1],0)
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],0,qreg_2[1]])
main_circ.s(qreg_2[0])
main_circ.cz(qreg_2[0],qreg_1[0])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_1[0],qreg_2[1]])
main_circ.s(qreg_2[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_1[0],qreg_0[0]])
main_circ.x(qreg_2[1])
main_circ.append(subcirc0,[qreg_2[1],qreg_2[0],0,qreg_1[0]])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],0,qreg_2[0]])
main_circ.u(param_0,0,param_0, qreg_2[0])
main_circ.u(0,param_1,param_1, qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_1[0]])
main_circ.x(qreg_1[0])
main_circ.s(qreg_0[0])
main_circ.s(qreg_2[1])
main_circ.u(0,param_1,param_0, qreg_2[1])
main_circ.cz(qreg_2[1],0)
main_circ.x(qreg_2[1])
bindings = {param_0: -0.151000, param_1: -0.097000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "514")
