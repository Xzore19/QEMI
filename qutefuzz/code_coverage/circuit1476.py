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
subcirc0.y(qreg_0[1])
subcirc0.rx(-0.888000, qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.u(0.099000,-0.374000,-0.647000, qreg_0[1])
subcirc2.rx(-0.292000, qreg_0[2])
subcirc2.u(-0.139000,-0.482000,-0.101000, qreg_0[2])
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
param_5 = Parameter("param_5")

main_circ.rx(-0.179000, qreg_0[2])
main_circ.x(qreg_0[2])
main_circ.x(1)
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],1])
main_circ.y(1)
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[0],1,qreg_3[0],qreg_0[1]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc1,[1,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],1])
main_circ.u(param_0,param_3,param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],0])
main_circ.x(qreg_0[1])
main_circ.rx(param_0, qreg_3[0])
main_circ.append(subcirc1,[1,qreg_3[0],0,qreg_0[1]])
main_circ.x(qreg_0[0])
main_circ.y(qreg_3[0])
main_circ.x(qreg_0[2])
main_circ.rx(0.068000, qreg_0[0])
main_circ.u(0.996000,param_0,param_5, qreg_0[0])
main_circ.y(0)
main_circ.u(param_0,param_3,0.525000, qreg_3[0])
main_circ.rx(0.243000, qreg_3[0])
main_circ.u(0.811000,param_5,param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],1])
main_circ.u(param_5,-0.775000,param_2, qreg_0[2])
main_circ.x(qreg_3[0])
main_circ.rx(param_5, qreg_0[0])
bindings = {param_0: 0.163000, param_2: -0.648000, param_3: 0.945000, param_5: -0.593000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
