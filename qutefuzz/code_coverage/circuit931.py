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
subcirc0.h(qreg_0[3])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.rz(-0.090000, qreg_0[1])
subcirc0.rz(0.258000, qreg_0[1])
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.rz(0.981000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.158000, qreg_0[3])
subcirc1.rx(0.447000, qreg_0[3])
subcirc1.rz(-0.743000, qreg_0[0])
subcirc1.rx(0.927000, qreg_0[1])
subcirc1.rz(0.179000, qreg_0[1])
subcirc1.rx(0.909000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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
param_5 = Parameter("param_5")

main_circ.rx(param_3, 2)
main_circ.h(1)
main_circ.rx(param_5, qreg_1[0])
main_circ.append(subcirc1,[qreg_1[0],0,3,2])
main_circ.cx(0,qreg_1[0])
main_circ.rx(0.057000, qreg_1[0])
main_circ.cx(0,qreg_0[0])
main_circ.h(qreg_1[0])
main_circ.rz(param_3, qreg_1[0])
main_circ.cx(2,0)
main_circ.rx(-0.941000, qreg_0[0])
main_circ.rx(-0.353000, 0)
main_circ.rx(0.712000, 0)
main_circ.append(subcirc1,[qreg_0[0],1,qreg_1[0],2])
main_circ.cx(qreg_1[0],3)
main_circ.rx(0.652000, qreg_0[0])
main_circ.rx(param_5, qreg_0[0])
main_circ.rz(param_4, 3)
main_circ.rx(param_4, qreg_1[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(1,0)
main_circ.cx(qreg_0[0],1)
main_circ.cx(qreg_1[0],2)
main_circ.cx(qreg_1[0],2)
main_circ.cx(2,3)
main_circ.cx(1,qreg_0[0])
main_circ.cx(2,1)
main_circ.h(qreg_1[0])
main_circ.rz(param_3, 1)
main_circ.rx(param_2, 1)
bindings = {param_2: 0.397000, param_3: 0.963000, param_4: -0.745000, param_5: 0.533000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "931")
