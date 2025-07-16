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
subcirc0.rz(0.896000, qreg_0[0])
subcirc0.rx(0.032000, qreg_1[0])
subcirc0.rz(-0.611000, qreg_0[0])
subcirc0.ry(-0.923000, qreg_3[0])
subcirc0.rx(-0.297000, qreg_0[0])
subcirc0.rz(0.420000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.cx(qreg_0[3],qreg_0[2])
subcirc1.rx(-0.851000, qreg_0[0])
subcirc1.rz(-0.308000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.049000, qreg_0[0])
subcirc2.rx(0.319000, qreg_0[1])
subcirc2.rz(-0.866000, qreg_0[2])
subcirc2.ry(0.088000, qreg_0[2])
subcirc2.ry(0.767000, qreg_0[0])
subcirc2.rz(-0.024000, qreg_0[0])

main_circ = QuantumCircuit(1)
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

main_circ.ry(param_2, qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.rz(0.039000, qreg_0[2])
main_circ.ry(param_0, qreg_0[2])
main_circ.rz(param_1, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],0,qreg_0[0]])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],0,qreg_0[0],qreg_0[1]])
main_circ.ry(0.271000, qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_3[0],0)
main_circ.append(subcirc2,[qreg_0[1],0,qreg_3[0],qreg_0[2]])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.ry(-0.953000, qreg_0[2])
main_circ.rx(param_1, qreg_3[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
bindings = {param_0: 0.136000, param_1: 0.796000, param_2: 0.910000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1083")
