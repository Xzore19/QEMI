from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,0.180000,-0.150000, qreg_0[1])
subcirc0.rx(0.727000, qreg_2[1])
subcirc0.h(qreg_2[1])
subcirc0.rx(0.219000, qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.u(pi/2,0.571000,-0.790000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.h(qreg_0[0])
main_circ.u(param_1,param_0,param_2, qreg_0[1])
main_circ.rz(param_0, qreg_0[1])
main_circ.rz(param_1, qreg_2[0])
main_circ.h(qreg_2[0])
main_circ.append(subcirc0,[qreg_2[1],qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.h(qreg_0[0])
main_circ.rz(-0.776000, qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
main_circ.h(qreg_0[0])
main_circ.h(qreg_2[0])
main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.rz(0.725000, qreg_2[0])
main_circ.h(qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.rz(0.954000, qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.rz(-0.665000, qreg_2[1])
main_circ.rx(0.162000, qreg_0[1])
main_circ.u(param_1,param_0,param_1, qreg_0[1])
bindings = {param_0: 0.223000, param_1: 0.528000, param_2: 0.865000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "406")
