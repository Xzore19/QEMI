from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.x(qreg_1[1])
subcirc0.x(qreg_1[0])
subcirc0.u(pi/2,-0.276000,0.463000, qreg_0[0])
subcirc0.cx(qreg_1[2],qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,-0.364000,0.595000, qreg_0[1])
subcirc1.rz(0.510000, qreg_2[0])
subcirc1.x(qreg_2[0])
subcirc1.u(pi/2,-0.344000,-0.839000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

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

main_circ.rz(param_0, 1)
main_circ.cx(3,1)
main_circ.cx(2,3)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.append(subcirc0,[2,0,3,1])
main_circ.append(subcirc0,[1,0,3,2])
main_circ.u(param_1,0.528000,-0.261000, 1)
main_circ.cx(2,3)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.rz(param_2, 3)
main_circ.cx(3,0)
main_circ.append(subcirc0,[2,3,1,0])
main_circ.u(pi/2,0.906000,0.769000, 2)
main_circ.cx(0,1)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.rz(param_2, 0)
main_circ.cx(2,0)
main_circ.append(subcirc0,[3,1,0,2])
main_circ.cx(0,3)
main_circ.cx(2,1)
main_circ.cx(1,3)
main_circ.x(1)
main_circ.x(2)
main_circ.cx(0,3)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.rz(0.303000, 1)
main_circ.cx(0,2)
main_circ.cx(1,2)
main_circ.x(1)
bindings = {param_0: -0.713000, param_1: 0.683000, param_2: -0.437000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "581")
