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
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.u(0.035000,0.929000,-0.433000, qreg_0[0])
subcirc0.y(qreg_3[0])
subcirc0.u(-0.450000,0.617000,0.360000, qreg_3[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.u(0.631000,-0.305000,0.660000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.y(qreg_0[0])
main_circ.u(param_0,-0.105000,-0.699000, qreg_1[1])
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.y(qreg_1[1])
main_circ.cz(qreg_1[1],qreg_1[0])
main_circ.cx(qreg_0[0],qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_1[0],qreg_0[0]])
main_circ.cz(qreg_3[0],qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_1[1]])
main_circ.u(param_2,0.527000,param_0, qreg_0[0])
main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.u(param_1,-0.769000,param_2, qreg_1[0])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.y(qreg_1[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.y(qreg_0[0])
main_circ.u(param_1,param_1,param_0, qreg_1[1])
main_circ.y(qreg_0[0])
main_circ.u(param_2,-0.421000,-0.147000, qreg_3[0])
bindings = {param_0: 0.994000, param_1: -0.485000, param_2: 0.608000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
