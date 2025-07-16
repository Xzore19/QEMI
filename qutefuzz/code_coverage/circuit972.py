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
subcirc0.u(pi/2,-0.310000,-0.913000, qreg_0[0])
subcirc0.u(pi/2,0.108000,-0.270000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.u(pi/2,0.656000,-0.901000, qreg_0[1])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.h(qreg_0[2])
subcirc1.s(qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.h(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.z(qreg_2[1])
subcirc2.s(qreg_2[0])
subcirc2.s(qreg_0[1])
subcirc2.h(qreg_0[0])

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

main_circ.append(subcirc0,[qreg_1[0],1,3,0,2])
main_circ.s(3)
main_circ.u(pi/2,param_1,param_0, 3)
main_circ.u(pi/2,param_1,param_1, 2)
main_circ.s(0)
main_circ.z(2)
main_circ.u(param_1,-0.056000,0.068000, 1)
main_circ.h(qreg_0[0])
main_circ.append(subcirc2,[0,2,1,qreg_0[0]])
main_circ.append(subcirc1,[3,2,qreg_0[0],0])
main_circ.append(subcirc2,[1,qreg_0[0],qreg_1[0],0])
main_circ.s(qreg_1[0])
main_circ.append(subcirc1,[qreg_1[0],1,2,qreg_0[0]])
main_circ.z(qreg_0[0])
main_circ.z(2)
main_circ.u(param_0,0.819000,param_2, 3)
main_circ.s(2)
main_circ.append(subcirc1,[qreg_0[0],3,2,1])
main_circ.h(qreg_0[0])
bindings = {param_0: -0.122000, param_1: 0.561000, param_2: 0.438000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "972")
