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
subcirc0.u(0,0,-0.547000, qreg_0[1])
subcirc0.u(0,0,-0.460000, qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.rz(0.345000, qreg_3[0])
subcirc0.u(0,0,0.558000, qreg_0[1])
subcirc0.u(0,0,0.672000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.589000, qreg_0[0])
subcirc1.rz(0.646000, qreg_0[1])
subcirc1.rx(0.075000, qreg_3[0])
subcirc1.u(0,0,0.876000, qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.479000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(param_3,param_0,param_1, 1)
main_circ.append(subcirc1,[1,qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1],0])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[3],1])
main_circ.rx(-0.276000, 1)
main_circ.u(0,param_0,0.174000, qreg_0[3])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],1,qreg_0[0],0,qreg_0[1]])
main_circ.append(subcirc0,[1,0,qreg_0[0],qreg_0[1]])
main_circ.rz(-0.409000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[3],1,0,qreg_0[2]])
main_circ.rx(0.566000, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[0],qreg_0[3],qreg_0[1],0])
main_circ.u(0,param_0,param_1, qreg_0[0])
main_circ.rx(param_2, qreg_0[2])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],qreg_0[3],1,qreg_0[2]])
main_circ.rz(0.797000, qreg_0[0])
main_circ.z(qreg_0[2])
main_circ.rx(param_1, 0)
bindings = {param_0: -0.977000, param_1: 0.960000, param_2: 0.214000, param_3: 0.628000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "862")
