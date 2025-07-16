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
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.cy(qreg_0[3],qreg_0[2])
subcirc0.u(pi/2,-0.162000,0.277000, qreg_0[3])
subcirc0.cx(qreg_0[1],qreg_0[3])

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

main_circ.h(1)
main_circ.h(2)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.append(subcirc0,[0,2,3,1])
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cy(2,1)
main_circ.cy(0,2)
main_circ.u(pi/2,param_0,param_3, 3)
main_circ.cx(2,1)
main_circ.cx(3,1)
main_circ.cy(0,3)
main_circ.u(param_3,0.971000,-0.651000, 2)
main_circ.cy(1,2)
main_circ.cy(0,3)
main_circ.cy(1,0)
main_circ.cx(3,0)
main_circ.u(pi/2,0.285000,param_1, 1)
main_circ.u(pi/2,param_0,-0.783000, 1)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.cy(2,1)
main_circ.cy(3,1)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.h(3)
main_circ.u(param_3,-0.476000,0.990000, 3)
main_circ.cy(3,0)
main_circ.cy(1,3)
main_circ.cx(0,3)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.cy(1,0)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cx(0,2)
main_circ.cy(3,0)
main_circ.cx(2,0)
main_circ.u(pi/2,param_2,0.866000, 0)
main_circ.u(param_3,param_0,0.900000, 2)
bindings = {param_0: 0.461000, param_1: 0.588000, param_2: -0.867000, param_3: 0.602000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
