from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(-0.749000, qreg_3[0])
subcirc0.cx(qreg_1[0],qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_3[0])
subcirc0.cz(qreg_3[0],qreg_1[0])
subcirc0.cz(qreg_1[1],qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cx(0,1)
main_circ.ry(0.231000, qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.ry(param_1, qreg_0[1])
main_circ.ry(-0.171000, 0)
main_circ.ry(-0.080000, qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.y(1)
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.ry(-0.398000, qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_3[0],qreg_0[1])
main_circ.cz(qreg_3[0],qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],0,qreg_0[2],qreg_0[0]])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.y(0)
main_circ.cx(1,0)
main_circ.ry(0.128000, qreg_3[0])
main_circ.ry(-0.974000, qreg_0[2])
main_circ.cx(1,0)
main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],1])
main_circ.y(qreg_0[2])
main_circ.cx(0,qreg_0[2])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.ry(param_2, qreg_0[1])
main_circ.cz(qreg_3[0],0)
main_circ.ry(0.008000, 0)
main_circ.ry(0.689000, qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.ry(param_0, 0)
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],0])
main_circ.ry(param_0, 0)
main_circ.cx(qreg_0[0],qreg_0[2])
bindings = {param_0: 0.537000, param_1: 0.630000, param_2: 0.512000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1389")
