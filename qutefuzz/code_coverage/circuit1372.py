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
subcirc0.ry(-0.206000, qreg_0[1])
subcirc0.y(qreg_0[2])
subcirc0.y(qreg_0[2])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_1[0])
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_2[0])
subcirc1.y(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(0.039000, qreg_0[1])
subcirc2.ry(-0.285000, qreg_0[3])
subcirc2.rx(-0.560000, qreg_0[3])
subcirc2.rx(-0.127000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rx(0.828000, qreg_1[0])
subcirc3.rx(-0.012000, qreg_0[0])
subcirc3.cy(qreg_1[1],qreg_1[0])
subcirc3.cy(qreg_0[0],qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
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

main_circ.append(subcirc3,[2,qreg_0[0],0,3])
main_circ.append(subcirc3,[1,0,3,qreg_0[0]])
main_circ.y(2)
main_circ.y(2)
main_circ.ry(param_4, 3)
main_circ.rx(param_3, 0)
main_circ.rx(-0.603000, 3)
main_circ.cy(2,0)
main_circ.append(subcirc3,[qreg_0[0],1,3,2])
main_circ.rx(0.884000, qreg_0[0])
main_circ.y(0)
main_circ.ry(param_2, 2)
main_circ.ry(-0.503000, 2)
main_circ.append(subcirc3,[0,1,qreg_0[0],2])
main_circ.append(subcirc3,[0,3,qreg_0[0],1])
main_circ.cy(0,2)
main_circ.y(1)
main_circ.cy(0,1)
main_circ.y(2)
main_circ.cy(0,qreg_0[0])
main_circ.ry(0.612000, 2)
main_circ.append(subcirc3,[1,0,2,3])
main_circ.ry(param_2, 3)
bindings = {param_2: -0.956000, param_3: 0.431000, param_4: 0.367000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1372")
