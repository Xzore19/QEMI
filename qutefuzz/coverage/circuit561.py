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
subcirc0.x(qreg_0[3])
subcirc0.u(0,0,-0.667000, qreg_0[3])
subcirc0.rx(0.204000, qreg_0[3])
subcirc0.u(0,0,-0.833000, qreg_0[1])
subcirc0.u(0,0,0.998000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.333000, qreg_2[0])
subcirc1.ry(0.611000, qreg_2[0])
subcirc1.x(qreg_3[0])
subcirc1.rx(-0.024000, qreg_2[0])
subcirc1.u(0,0,0.575000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.496000, qreg_1[0])
subcirc2.u(0,0,-0.729000, qreg_3[0])
subcirc2.u(0,0,-0.633000, qreg_3[0])
subcirc2.rx(0.969000, qreg_1[0])
subcirc2.ry(-0.526000, qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.119000, qreg_3[0])
subcirc3.u(0,0,0.867000, qreg_0[1])
subcirc3.u(0,0,-0.313000, qreg_0[1])
subcirc3.rx(0.842000, qreg_0[1])
subcirc3.x(qreg_3[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(-0.356000, qreg_0[1])
subcirc4.rx(-0.588000, qreg_0[2])
subcirc4.ry(0.601000, qreg_0[1])
subcirc4.x(qreg_0[2])
subcirc4.u(0,0,-0.635000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.rx(param_0, 0)
main_circ.append(subcirc2,[0,qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.ry(param_0, qreg_0[3])
main_circ.x(qreg_0[1])
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[2])
main_circ.rx(-0.248000, qreg_0[3])
main_circ.ry(param_3, qreg_0[3])
main_circ.ry(-0.446000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[2],qreg_0[1],0])
main_circ.ry(param_1, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[3],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],0,qreg_0[2]])
main_circ.x(qreg_0[2])
main_circ.u(param_3,param_0,-0.867000, qreg_0[1])
main_circ.rx(-0.174000, qreg_0[1])
main_circ.u(0,param_0,param_1, qreg_0[3])
main_circ.rx(param_1, 0)
main_circ.x(qreg_0[0])
main_circ.x(0)
main_circ.rx(0.829000, qreg_0[2])
main_circ.rx(0.364000, qreg_0[0])
main_circ.ry(-0.895000, qreg_0[2])
main_circ.rx(-0.280000, 0)
main_circ.u(param_2,param_1,param_3, qreg_0[3])
main_circ.u(param_0,param_1,0.685000, qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.x(qreg_0[3])
bindings = {param_0: -0.995000, param_1: 0.799000, param_2: -0.252000, param_3: 0.377000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "561")
