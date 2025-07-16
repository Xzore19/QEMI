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
subcirc0.u(0,0,-0.037000, qreg_0[2])
subcirc0.cz(qreg_3[0],qreg_0[2])
subcirc0.u(0,0,-0.131000, qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.h(qreg_1[1])
subcirc1.u(0,0,0.616000, qreg_0[0])
subcirc1.u(0,0,-0.504000, qreg_1[2])
subcirc1.h(qreg_1[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.u(0,0,-0.650000, qreg_0[3])
subcirc2.h(qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0,0,-0.405000, qreg_0[1])
subcirc3.h(qreg_0[0])
subcirc3.u(0,0,-0.971000, qreg_0[3])
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.cz(2,3)
main_circ.x(3)
main_circ.append(subcirc1,[1,2,3,0])
main_circ.h(2)
main_circ.h(1)
main_circ.x(2)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.append(subcirc1,[1,0,2,3])
main_circ.u(param_4,0,-0.100000, 1)
main_circ.cz(3,0)
main_circ.cz(2,0)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.u(param_5,0,param_3, 0)
main_circ.append(subcirc1,[3,1,2,0])
main_circ.cz(3,2)
main_circ.h(1)
main_circ.u(0,param_0,param_3, 3)
main_circ.u(0,param_1,-0.154000, 1)
main_circ.cz(2,0)
main_circ.cz(2,3)
main_circ.cz(2,3)
main_circ.cz(2,1)
main_circ.cz(3,2)
main_circ.cz(0,3)
main_circ.cz(3,0)
main_circ.cz(3,2)
main_circ.cz(0,3)
main_circ.cz(3,0)
main_circ.u(param_0,param_2,0.190000, 2)
main_circ.x(1)
main_circ.h(1)
main_circ.h(2)
bindings = {param_0: 0.151000, param_1: 0.527000, param_2: 0.214000, param_3: 0.039000, param_4: -0.546000, param_5: 0.636000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "272")
