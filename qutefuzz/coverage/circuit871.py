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
subcirc0.u(-0.765000,0.599000,0.947000, qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0.u(0,0,0.833000, qreg_0[2])
subcirc0.u(0,0,0.764000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[2],qreg_3[0])
subcirc1.u(0,0,0.438000, qreg_0[1])
subcirc1.u(0,0,0.347000, qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.u(0,0,0.585000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.537000,0.724000,-0.021000, qreg_3[0])
subcirc2.u(0,0,0.466000, qreg_3[0])
subcirc2.u(-0.808000,-0.667000,0.704000, qreg_3[0])
subcirc2.cx(qreg_0[2],qreg_0[0])
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(0.408000,0.895000,-0.845000, qreg_3[0])
main_circ.u(0,param_3,param_0, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],0,qreg_0[0],1])
main_circ.u(param_3,param_4,-0.847000, qreg_0[1])
main_circ.cx(0,qreg_0[0])
main_circ.u(param_0,0,-0.902000, 1)
main_circ.cx(0,qreg_3[0])
main_circ.cx(qreg_0[1],1)
main_circ.append(subcirc1,[qreg_0[2],0,1,qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],0,qreg_0[2],1])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],0,qreg_0[1],qreg_0[0],1])
main_circ.u(param_1,param_4,param_2, 1)
main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[0],0,qreg_0[2],qreg_3[0]])
main_circ.s(qreg_0[0])
main_circ.cx(1,qreg_3[0])
main_circ.cx(qreg_3[0],1)
main_circ.cx(qreg_3[0],0)
main_circ.cx(1,0)
main_circ.s(qreg_0[0])
main_circ.s(1)
main_circ.u(0,0,-0.150000, qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],0,1,qreg_0[2]])
main_circ.s(qreg_0[1])
bindings = {param_0: 0.119000, param_1: 0.998000, param_2: 0.322000, param_3: -0.910000, param_4: -0.953000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "871")
