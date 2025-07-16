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
subcirc0.cz(qreg_0[1],qreg_0[3])
subcirc0.y(qreg_0[2])
subcirc0.s(qreg_0[3])
subcirc0.y(qreg_0[2])
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.s(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_0[3])
subcirc1.y(qreg_0[1])
subcirc1.u(0.126000,-0.641000,0.626000, qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.s(qreg_0[2])
main_circ.u(param_7,param_4,param_7, qreg_0[2])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.u(-0.994000,-0.057000,param_1, qreg_0[2])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0],0])
main_circ.u(param_4,param_0,param_4, 0)
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_0[2],0])
main_circ.y(0)
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],0,qreg_0[1]])
main_circ.u(0.318000,0.056000,param_3, qreg_0[0])
main_circ.s(0)
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1],0])
main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.cz(qreg_0[2],qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0],0])
main_circ.y(qreg_0[0])
main_circ.y(0)
main_circ.s(0)
main_circ.u(param_2,param_4,param_6, qreg_0[1])
bindings = {param_0: -0.118000, param_1: 0.800000, param_2: -0.500000, param_3: 0.508000, param_4: -0.281000, param_6: -0.611000, param_7: -0.721000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1986")
