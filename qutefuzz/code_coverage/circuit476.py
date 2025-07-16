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
subcirc0.u(pi/2,-0.544000,0.298000, qreg_0[2])
subcirc0.h(qreg_0[3])
subcirc0.h(qreg_0[1])
subcirc0.cz(qreg_0[2],qreg_0[3])
subcirc0.u(pi/2,0.198000,-0.469000, qreg_0[2])

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

main_circ.cx(qreg_0[0],2)
main_circ.u(param_0,0.654000,param_0, 2)
main_circ.cz(2,3)
main_circ.cx(qreg_0[0],2)
main_circ.u(param_2,param_0,-0.116000, 0)
main_circ.cz(2,0)
main_circ.h(0)
main_circ.h(3)
main_circ.cz(qreg_0[0],2)
main_circ.u(pi/2,-0.480000,0.330000, 0)
main_circ.u(param_3,-0.162000,-0.928000, qreg_0[0])
main_circ.append(subcirc0,[1,qreg_0[0],2,0])
main_circ.u(pi/2,-0.247000,param_2, 3)
main_circ.h(qreg_0[0])
main_circ.u(param_2,param_1,param_3, 0)
main_circ.h(3)
main_circ.cz(0,3)
main_circ.cx(qreg_0[0],2)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.u(param_1,-0.076000,param_2, 3)
main_circ.append(subcirc0,[0,qreg_0[0],1,3])
main_circ.cx(0,2)
main_circ.cx(qreg_0[0],3)
main_circ.h(qreg_0[0])
main_circ.cz(qreg_0[0],1)
main_circ.append(subcirc0,[1,2,3,0])
bindings = {param_0: -0.980000, param_1: -0.944000, param_2: -0.688000, param_3: 0.004000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "476")
