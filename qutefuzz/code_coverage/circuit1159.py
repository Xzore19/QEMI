from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.u(0.218000,-0.182000,-0.833000, qreg_0[0])
subcirc0.u(0,0,-0.129000, qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.cy(qreg_3[0],qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.655000, qreg_0[2])
subcirc1.u(-0.606000,-0.691000,0.690000, qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[2])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.u(0.837000,-0.443000,param_1, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.cy(qreg_3[0],qreg_0[1])
main_circ.u(0,0,0.798000, qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.u(-0.821000,param_0,0.188000, qreg_3[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.u(-0.619000,-0.455000,-0.762000, qreg_0[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.u(param_1,0,-0.937000, qreg_0[1])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.u(param_1,0.210000,param_0, qreg_3[0])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.u(param_2,param_3,param_0, qreg_0[0])
main_circ.u(-0.167000,param_4,-0.943000, qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.u(param_3,0.443000,param_4, qreg_0[2])
main_circ.u(0.945000,-0.062000,param_0, qreg_0[2])
main_circ.u(0,0,param_4, qreg_0[2])
main_circ.u(param_1,0.850000,param_0, qreg_0[2])
bindings = {param_0: -0.137000, param_1: 0.018000, param_2: 0.563000, param_3: 0.899000, param_4: -0.357000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1159")
