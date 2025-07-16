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
subcirc0.x(qreg_0[0])
subcirc0.rx(0.215000, qreg_0[2])
subcirc0.rx(0.921000, qreg_3[0])
subcirc0.u(0.598000,-0.158000,0.776000, qreg_0[1])
subcirc0.x(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(0.473000, qreg_0[0])
subcirc1.rx(-0.693000, qreg_1[0])
subcirc1.x(qreg_2[0])
subcirc1.u(-0.342000,-0.608000,0.126000, qreg_2[0])
subcirc1.x(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.133000,0.809000,-0.876000, qreg_0[1])
subcirc2.x(qreg_3[0])
subcirc2.u(-0.245000,-0.883000,-0.180000, qreg_0[0])
subcirc2.rx(0.359000, qreg_2[0])
subcirc2.rx(-0.278000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_2[0],qreg_0[0])
subcirc3.rx(0.646000, qreg_2[0])
subcirc3.x(qreg_0[0])
subcirc3.cx(qreg_0[0],qreg_2[0])
subcirc3.cx(qreg_3[0],qreg_2[0])

main_circ = QuantumCircuit(0)
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

main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_0, qreg_0[1])
main_circ.x(qreg_3[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.u(param_1,param_1,0.803000, qreg_0[1])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.rx(param_1, qreg_3[0])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.x(qreg_0[2])
bindings = {param_0: 0.488000, param_1: 0.165000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1552")
