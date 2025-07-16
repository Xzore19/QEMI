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
subcirc0.rx(-0.955000, qreg_0[0])
subcirc0.y(qreg_0[2])
subcirc0.u(0,0,0.865000, qreg_0[1])
subcirc0.y(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.532000, qreg_0[1])
subcirc1.y(qreg_2[0])
subcirc1.rx(0.139000, qreg_0[0])
subcirc1.rx(0.360000, qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.u(param_7,0,param_3, 1)
main_circ.rx(0.116000, qreg_1[1])
main_circ.y(qreg_0[0])
main_circ.u(param_6,param_5,0.076000, qreg_1[2])
main_circ.y(qreg_1[2])
main_circ.append(subcirc0,[qreg_1[1],0,1,qreg_1[2]])
main_circ.append(subcirc1,[qreg_1[0],1,qreg_1[1],qreg_0[0]])
main_circ.u(0,0,0.010000, 1)
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[2],qreg_1[0]])
main_circ.u(param_3,param_2,param_6, qreg_0[0])
main_circ.y(qreg_1[1])
main_circ.rx(param_7, 0)
main_circ.rz(0.241000, qreg_1[0])
main_circ.u(0,0,param_6, qreg_1[0])
main_circ.u(param_3,0,-0.994000, qreg_1[2])
main_circ.y(1)
main_circ.rx(param_1, qreg_1[2])
main_circ.u(0,0,param_1, qreg_0[0])
main_circ.y(1)
main_circ.rz(param_0, 1)
main_circ.y(1)
main_circ.u(param_1,0,-0.306000, 1)
main_circ.rz(0.066000, qreg_1[2])
main_circ.rz(param_2, 0)
main_circ.rz(0.984000, qreg_0[0])
main_circ.rx(param_3, qreg_0[0])
main_circ.append(subcirc1,[0,qreg_1[1],1,qreg_0[0]])
main_circ.rz(param_4, 0)
main_circ.rz(param_3, qreg_1[2])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.rx(0.602000, 0)
main_circ.u(0,0,param_3, 0)
main_circ.rx(-0.883000, 0)
bindings = {param_0: -0.032000, param_1: 0.898000, param_2: 0.297000, param_3: -0.110000, param_4: 0.109000, param_5: 0.629000, param_6: -0.040000, param_7: -0.809000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "33")
