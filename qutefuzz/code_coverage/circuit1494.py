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
subcirc0.u(-0.359000,-0.308000,-0.364000, qreg_0[1])
subcirc0.u(-0.146000,0.418000,0.436000, qreg_0[3])
subcirc0.h(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.h(qreg_0[3])
subcirc0.s(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.s(qreg_0[2])
subcirc1.x(qreg_3[0])
subcirc1.s(qreg_0[1])
subcirc1.u(-0.610000,-0.010000,-0.087000, qreg_3[0])
subcirc1.s(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[3])
subcirc2.x(qreg_0[0])
subcirc2.u(-0.512000,-0.894000,0.586000, qreg_0[2])
subcirc2.s(qreg_0[0])
subcirc2.u(0.086000,0.565000,-0.351000, qreg_0[0])
subcirc2.u(0.792000,-0.853000,0.757000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.x(qreg_0[1])
main_circ.s(qreg_0[2])
main_circ.x(qreg_3[0])
main_circ.x(qreg_3[0])
main_circ.u(param_1,-0.158000,param_0, 0)
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],1,0])
main_circ.s(qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.u(-0.696000,0.822000,-0.669000, qreg_3[0])
main_circ.h(qreg_0[2])
main_circ.s(qreg_0[2])
main_circ.u(0.709000,param_0,param_1, qreg_0[1])
main_circ.u(-0.080000,param_0,0.063000, 1)
main_circ.append(subcirc1,[0,qreg_3[0],1,qreg_0[0]])
main_circ.x(qreg_0[0])
main_circ.h(0)
main_circ.x(qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.append(subcirc2,[1,qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.s(qreg_3[0])
main_circ.x(qreg_3[0])
main_circ.x(qreg_3[0])
main_circ.u(0.264000,param_0,param_2, qreg_3[0])
main_circ.s(qreg_3[0])
main_circ.u(param_1,param_0,param_0, qreg_0[2])
bindings = {param_0: 0.790000, param_1: -0.115000, param_2: 0.923000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1494")
