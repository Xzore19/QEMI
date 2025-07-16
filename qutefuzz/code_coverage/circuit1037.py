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
subcirc0.ry(-0.430000, qreg_0[3])
subcirc0.u(0.743000,0.097000,-0.553000, qreg_0[3])
subcirc0.u(-0.567000,0.657000,0.374000, qreg_0[3])
subcirc0.ry(0.168000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_1[0])
subcirc1.u(-0.302000,-0.624000,-0.676000, qreg_1[0])
subcirc1.ry(-0.250000, qreg_0[0])
subcirc1.u(-0.975000,-0.206000,-0.925000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.138000, qreg_0[1])
subcirc2.ry(-0.802000, qreg_0[0])
subcirc2.cx(qreg_2[0],qreg_0[1])
subcirc2.cx(qreg_2[0],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.ry(0.224000, qreg_0[1])
subcirc3.s(qreg_0[1])
subcirc3.ry(-0.930000, qreg_2[1])
subcirc3.s(qreg_2[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.s(qreg_2[0])
subcirc4.s(qreg_3[0])
subcirc4.cx(qreg_0[1],qreg_3[0])
subcirc4.s(qreg_0[0])

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

main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_1[0],qreg_0[0]])
main_circ.cx(qreg_3[0],qreg_1[1])
main_circ.u(0.328000,param_1,param_0, qreg_1[1])
main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.append(subcirc4,[qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.ry(-0.938000, qreg_3[0])
main_circ.u(0.504000,-0.354000,-0.106000, qreg_0[0])
main_circ.s(qreg_1[1])
main_circ.append(subcirc4,[qreg_3[0],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.ry(param_2, qreg_0[0])
main_circ.s(qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.u(-0.017000,0.524000,param_2, qreg_1[1])
main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.append(subcirc4,[qreg_1[0],qreg_3[0],qreg_1[1],qreg_0[0]])
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.cx(qreg_0[0],qreg_1[1])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(qreg_0[0],qreg_1[1])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.ry(0.905000, qreg_3[0])
main_circ.ry(-0.625000, qreg_0[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(qreg_3[0],qreg_1[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_1[0],qreg_1[1],qreg_0[0]])
bindings = {param_0: 0.261000, param_1: -0.474000, param_2: -0.961000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1037")
