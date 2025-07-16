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
subcirc0.x(qreg_1[1])
subcirc0.u(0,0,0.790000, qreg_0[0])
subcirc0.u(0,0,-0.330000, qreg_0[0])
subcirc0.u(0,0,0.375000, qreg_1[0])
subcirc0.x(qreg_1[0])
subcirc0.u(0,0,-0.880000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.249000, qreg_0[1])
subcirc1.h(qreg_0[2])
subcirc1.rx(-0.079000, qreg_0[1])
subcirc1.u(0,0,0.020000, qreg_0[2])
subcirc1.u(0,0,0.535000, qreg_0[0])
subcirc1.h(qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.h(qreg_0[1])
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.h(qreg_0[1])
main_circ.x(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.h(qreg_0[3])
main_circ.u(0,param_0,param_0, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.h(qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.u(0,0,0.076000, qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.rx(0.289000, qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.u(param_0,0,param_0, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.x(qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.h(qreg_0[0])
bindings = {param_0: -0.338000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1749")
