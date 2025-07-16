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
subcirc0.h(qreg_3[0])
subcirc0.cx(qreg_0[0],qreg_0[2])
subcirc0.rx(0.689000, qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.rx(0.020000, qreg_0[1])
subcirc0.h(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_3[0],qreg_1[1])
subcirc1.cz(qreg_1[1],qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_1[1])
subcirc1.cz(qreg_1[0],qreg_3[0])
subcirc1.rx(0.079000, qreg_3[0])
subcirc1.rx(-0.225000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.cz(2,0)
main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[0],0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc0,[2,1,qreg_0[0],0])
main_circ.rx(param_1, 2)
main_circ.cx(qreg_0[0],3)
main_circ.h(3)
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.rx(param_1, qreg_0[0])
main_circ.cx(qreg_0[0],2)
main_circ.h(3)
main_circ.rx(param_2, 2)
main_circ.h(qreg_0[1])
main_circ.rx(0.456000, qreg_0[0])
main_circ.cx(3,qreg_0[0])
main_circ.append(subcirc0,[1,3,qreg_0[0],2])
main_circ.cz(qreg_0[1],2)
main_circ.append(subcirc0,[1,3,0,qreg_0[0]])
main_circ.cz(0,qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.h(3)
main_circ.h(qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.cz(2,qreg_0[0])
main_circ.cx(0,3)
main_circ.cz(2,0)
main_circ.cx(qreg_0[1],2)
main_circ.cx(0,2)
main_circ.h(qreg_0[1])
main_circ.rx(0.654000, 3)
main_circ.cx(2,qreg_0[1])
bindings = {param_1: 0.768000, param_2: 0.268000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1357")
