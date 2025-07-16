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
subcirc0.z(qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.rx(-0.217000, qreg_0[1])
subcirc0.u(0,0,-0.567000, qreg_0[2])
subcirc0.u(0,0,-0.647000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[2])
subcirc1.z(qreg_3[0])
subcirc1.h(qreg_0[0])

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

main_circ.u(0,param_1,param_1, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],2,0,1])
main_circ.u(0,param_0,0.308000, 0)
main_circ.h(2)
main_circ.u(0,0,param_0, 3)
main_circ.rx(-0.775000, 2)
main_circ.h(2)
main_circ.rx(0.347000, qreg_0[0])
main_circ.append(subcirc1,[3,0,1,2])
main_circ.append(subcirc1,[2,1,3,qreg_0[0]])
main_circ.append(subcirc1,[0,2,qreg_0[0],3])
main_circ.append(subcirc1,[3,1,0,2])
main_circ.append(subcirc1,[3,1,0,qreg_0[0]])
main_circ.z(qreg_0[0])
main_circ.z(1)
main_circ.append(subcirc1,[3,qreg_0[0],0,1])
main_circ.z(1)
main_circ.append(subcirc1,[1,0,qreg_0[0],2])
main_circ.h(3)
main_circ.z(0)
main_circ.rx(param_0, 3)
main_circ.h(0)
main_circ.rx(param_0, qreg_0[0])
bindings = {param_0: 0.778000, param_1: 0.797000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1128")
