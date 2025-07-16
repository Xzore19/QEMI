from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0,0,-0.204000, qreg_2[0])
subcirc0.ry(-0.084000, qreg_1[0])
subcirc0.u(0,0,0.451000, qreg_2[1])
subcirc0.ry(-0.961000, qreg_2[0])
subcirc0.u(pi/2,-0.349000,0.538000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[0])
subcirc1.ry(0.844000, qreg_0[3])
subcirc1.u(pi/2,-0.924000,0.547000, qreg_0[1])
subcirc1.x(qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,0.115000,0.061000, qreg_0[1])
subcirc2.x(qreg_0[0])
subcirc2.u(pi/2,0.419000,-0.957000, qreg_0[0])
subcirc2.ry(-0.225000, qreg_0[1])
subcirc2.u(pi/2,-0.920000,-0.190000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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

main_circ.u(0,0,-0.401000, qreg_0[3])
main_circ.x(0)
main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
main_circ.u(pi/2,0.494000,param_3, qreg_0[1])
main_circ.ry(param_4, 0)
main_circ.u(pi/2,-0.352000,param_1, qreg_0[1])
main_circ.x(qreg_0[3])
main_circ.append(subcirc2,[qreg_0[2],0,qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.x(0)
main_circ.x(qreg_0[2])
main_circ.ry(0.093000, 0)
main_circ.append(subcirc2,[qreg_0[3],0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.u(0,0,-0.976000, qreg_0[2])
main_circ.u(param_3,0,0.396000, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[3],qreg_0[0],0,qreg_0[1]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0],0])
main_circ.ry(-0.306000, qreg_0[2])
main_circ.u(param_2,param_0,-0.740000, qreg_0[3])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,qreg_0[3],qreg_0[2]])
main_circ.append(subcirc2,[qreg_0[2],0,qreg_0[0],qreg_0[3],qreg_0[1]])
main_circ.ry(param_4, qreg_0[1])
main_circ.u(param_3,0,0.650000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[3],0,qreg_0[2]])
main_circ.u(0,param_2,param_1, qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.u(param_2,-0.568000,param_0, qreg_0[1])
main_circ.ry(-0.566000, qreg_0[2])
bindings = {param_0: 0.491000, param_1: -0.204000, param_2: -0.001000, param_3: 0.281000, param_4: 0.870000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "237")
