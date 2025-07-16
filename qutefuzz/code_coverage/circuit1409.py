from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.h(qreg_2[0])
subcirc0.cy(qreg_2[0],qreg_2[1])
subcirc0.h(qreg_0[1])
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.h(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.ry(-0.819000, qreg_2[0])
subcirc1.h(qreg_3[0])
subcirc1.cy(qreg_2[0],qreg_0[1])
subcirc1.ry(0.087000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(0.425000, 1)
main_circ.append(subcirc0,[0,1,3,qreg_0[0]])
main_circ.h(2)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.append(subcirc0,[qreg_0[0],3,0,2])
main_circ.append(subcirc0,[0,3,2,1])
main_circ.ry(-0.688000, 0)
main_circ.cy(qreg_0[0],0)
main_circ.ry(param_1, 0)
main_circ.cy(2,0)
main_circ.rz(-0.023000, 2)
main_circ.rz(param_0, 3)
main_circ.rz(0.402000, 1)
main_circ.append(subcirc0,[1,0,qreg_0[0],2])
main_circ.cy(2,qreg_0[0])
main_circ.append(subcirc0,[1,2,0,qreg_0[0]])
main_circ.h(3)
main_circ.h(qreg_0[0])
main_circ.h(3)
main_circ.cy(0,3)
main_circ.h(3)
main_circ.append(subcirc0,[0,qreg_0[0],2,1])
main_circ.h(qreg_0[0])
bindings = {param_0: 0.870000, param_1: -0.511000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1409")
