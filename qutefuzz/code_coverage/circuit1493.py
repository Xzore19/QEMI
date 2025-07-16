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
subcirc0.x(qreg_0[2])
subcirc0.rx(-0.470000, qreg_0[0])
subcirc0.y(qreg_0[3])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.460000, qreg_0[1])
subcirc1.rx(0.417000, qreg_0[2])
subcirc1.ry(0.564000, qreg_0[2])
subcirc1.ry(-0.644000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.080000, qreg_3[0])
subcirc2.y(qreg_3[0])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_3[0])
subcirc3.rx(0.787000, qreg_3[0])
subcirc3.y(qreg_0[1])
subcirc3.x(qreg_3[0])

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
param_3 = Parameter("param_3")

main_circ.append(subcirc2,[0,qreg_0[0],3,1])
main_circ.append(subcirc3,[0,2,1,3])
main_circ.x(2)
main_circ.rx(-0.100000, 0)
main_circ.y(3)
main_circ.ry(param_0, 2)
main_circ.ry(param_3, 3)
main_circ.y(qreg_0[0])
main_circ.ry(param_0, 0)
main_circ.y(1)
main_circ.ry(param_0, 3)
main_circ.ry(0.004000, 2)
main_circ.rx(param_1, qreg_0[0])
main_circ.ry(param_1, 1)
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[3,qreg_0[0],0,2])
main_circ.append(subcirc2,[2,0,3,1])
main_circ.y(1)
main_circ.append(subcirc3,[1,2,qreg_0[0],0])
main_circ.append(subcirc2,[qreg_0[0],1,3,0])
main_circ.x(0)
main_circ.ry(param_3, 3)
main_circ.y(1)
main_circ.append(subcirc3,[2,qreg_0[0],0,3])
bindings = {param_0: 0.296000, param_1: 0.210000, param_3: 0.388000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1493")
