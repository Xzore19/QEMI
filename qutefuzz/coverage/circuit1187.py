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
subcirc0.u(0,0,-0.341000, qreg_0[3])
subcirc0.u(0,0,0.405000, qreg_0[0])
subcirc0.x(qreg_0[2])
subcirc0.rz(-0.385000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.697000, qreg_1[0])
subcirc1.rz(-0.277000, qreg_1[0])
subcirc1.x(qreg_1[0])
subcirc1.rz(0.804000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.284000, qreg_3[0])
subcirc2.rz(-0.678000, qreg_1[0])
subcirc2.u(0,0,-0.476000, qreg_1[0])
subcirc2.u(0,0,-0.766000, qreg_1[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc1,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_1[0]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_1[0],qreg_2[0]])
main_circ.rx(param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.x(qreg_2[0])
main_circ.u(0,param_2,0.193000, qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.rx(param_0, qreg_2[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_2[1],qreg_2[0]])
main_circ.rz(param_4, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[qreg_2[1],qreg_1[0],qreg_0[0],qreg_2[0]])
main_circ.append(subcirc1,[qreg_2[0],qreg_1[0],qreg_0[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_1[0],qreg_2[0]])
main_circ.append(subcirc1,[qreg_2[1],qreg_1[0],qreg_0[0],qreg_2[0]])
main_circ.rz(param_4, qreg_2[0])
main_circ.u(param_1,param_2,param_4, qreg_2[1])
main_circ.rz(-0.783000, qreg_2[1])
main_circ.rx(0.186000, qreg_1[0])
main_circ.rx(0.588000, qreg_2[0])
main_circ.u(param_4,param_0,param_1, qreg_0[0])
main_circ.u(param_1,param_1,0.855000, qreg_2[0])
bindings = {param_0: -0.649000, param_1: -0.323000, param_2: -0.668000, param_4: -0.767000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1187")
