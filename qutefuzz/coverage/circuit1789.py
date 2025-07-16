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
subcirc0.z(qreg_0[1])
subcirc0.u(0,0,0.997000, qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_0[1])

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

main_circ.cx(3,0)
main_circ.z(2)
main_circ.cx(2,1)
main_circ.u(0,param_4,-0.306000, 1)
main_circ.cx(1,3)
main_circ.h(3)
main_circ.z(3)
main_circ.u(0,0,-0.787000, 2)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.cx(2,3)
main_circ.u(param_4,0,param_3, 2)
main_circ.cx(3,1)
main_circ.z(1)
main_circ.cx(3,2)
main_circ.z(1)
main_circ.h(0)
main_circ.z(0)
main_circ.u(param_0,param_2,0.630000, 0)
main_circ.h(2)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.u(param_3,0,-0.806000, 3)
main_circ.cx(1,3)
main_circ.z(0)
main_circ.append(subcirc0,[1,2,3,0])
main_circ.cx(0,2)
main_circ.cx(1,2)
main_circ.cx(1,3)
main_circ.cx(1,3)
main_circ.cx(3,0)
main_circ.cx(2,1)
main_circ.cx(3,2)
main_circ.cx(2,0)
main_circ.z(3)
main_circ.cx(0,2)
bindings = {param_0: 0.391000, param_2: 0.318000, param_3: 0.092000, param_4: -0.584000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
