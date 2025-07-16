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
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.rx(0.980000, qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.rx(0.670000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_3[0],qreg_0[1])
subcirc1.s(qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1.rx(-0.473000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.cx(qreg_3[0],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[0])
subcirc2.s(qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cx(3,qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],3,2,qreg_1[0]])
main_circ.s(0)
main_circ.rx(param_0, 1)
main_circ.rx(-0.523000, 1)
main_circ.s(0)
main_circ.cx(2,qreg_1[0])
main_circ.rx(0.049000, 0)
main_circ.cz(1,0)
main_circ.append(subcirc2,[1,0,2,3])
main_circ.cz(3,2)
main_circ.append(subcirc0,[0,qreg_0[0],2,qreg_1[0]])
main_circ.rx(-0.564000, 0)
main_circ.cx(qreg_1[0],2)
main_circ.append(subcirc0,[0,1,qreg_0[0],3])
main_circ.append(subcirc0,[qreg_0[0],0,1,3])
main_circ.append(subcirc2,[2,qreg_0[0],1,qreg_1[0]])
main_circ.rx(-0.177000, qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.s(qreg_1[0])
main_circ.append(subcirc0,[2,3,qreg_1[0],0])
main_circ.cz(3,2)
main_circ.cz(1,0)
main_circ.cx(qreg_1[0],1)
main_circ.append(subcirc2,[qreg_0[0],3,1,qreg_1[0]])
main_circ.append(subcirc2,[qreg_1[0],3,qreg_0[0],2])
main_circ.cx(1,2)
main_circ.rx(param_1, 0)
bindings = {param_0: 0.402000, param_1: 0.575000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1148")
