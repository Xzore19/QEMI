from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.843000,0.174000, qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0.u(pi/2,0.838000,0.070000, qreg_3[0])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.ry(-0.453000, qreg_0[1])
subcirc1.ry(-0.255000, qreg_0[2])
subcirc1.u(pi/2,0.566000,-0.810000, qreg_0[1])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.u(pi/2,-0.182000,0.729000, qreg_1[2])
subcirc2.x(qreg_1[2])
subcirc2.x(qreg_1[0])
subcirc2.ry(0.489000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.x(qreg_0[2])
subcirc3.x(qreg_0[2])
subcirc3.x(qreg_0[2])
subcirc3.x(qreg_0[1])
subcirc3.x(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.x(qreg_0[0])
main_circ.z(qreg_1[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],qreg_3[0],qreg_1[0],0])
main_circ.x(qreg_1[0])
main_circ.append(subcirc0,[qreg_3[0],0,qreg_0[0],qreg_1[1],qreg_1[0]])
main_circ.append(subcirc1,[0,qreg_3[0],qreg_1[0],qreg_1[1]])
main_circ.u(param_0,param_0,0.678000, qreg_1[1])
main_circ.append(subcirc1,[0,qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.ry(param_0, qreg_3[0])
main_circ.x(0)
main_circ.x(qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.z(qreg_1[1])
main_circ.z(qreg_1[0])
main_circ.ry(param_0, qreg_1[1])
main_circ.ry(param_0, 0)
main_circ.x(qreg_1[0])
main_circ.x(qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],0,qreg_0[0]])
main_circ.ry(param_0, qreg_0[0])
main_circ.ry(0.656000, 0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],0,qreg_1[0]])
bindings = {param_0: 0.156000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1676")
