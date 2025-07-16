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
subcirc0.u(0.264000,0.569000,-0.430000, qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.ry(0.785000, qreg_0[2])
subcirc0.ry(-0.964000, qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.ry(0.886000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.313000, qreg_0[0])
subcirc1.rz(-0.252000, qreg_0[3])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.rz(0.855000, qreg_0[2])
subcirc1.ry(-0.345000, qreg_0[1])
subcirc1.rz(0.495000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.729000, qreg_2[0])
subcirc2.cz(qreg_2[0],qreg_0[1])
subcirc2.u(-0.666000,0.104000,0.560000, qreg_2[0])
subcirc2.u(0.729000,-0.036000,-0.268000, qreg_3[0])
subcirc2.ry(-0.002000, qreg_0[1])
subcirc2.u(-0.019000,-0.327000,0.539000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(0.044000, qreg_0[0])
subcirc3.rz(0.209000, qreg_3[0])
subcirc3.u(-0.565000,0.417000,-0.248000, qreg_0[2])
subcirc3.cz(qreg_3[0],qreg_0[2])
subcirc3.ry(0.165000, qreg_0[0])
subcirc3.cz(qreg_0[2],qreg_3[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.append(subcirc0,[qreg_2[0],1,qreg_0[0],qreg_3[0]])
main_circ.cz(qreg_0[1],1)
main_circ.rz(0.647000, 1)
main_circ.ry(param_1, 1)
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.cz(qreg_0[0],0)
main_circ.u(param_4,-0.349000,param_3, qreg_0[1])
main_circ.rz(0.215000, 1)
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],0,qreg_2[0],qreg_3[0],1])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.append(subcirc2,[qreg_3[0],0,qreg_0[0],qreg_0[1],qreg_2[0],1])
main_circ.append(subcirc1,[1,qreg_0[0],0,qreg_2[0]])
main_circ.rz(param_4, qreg_3[0])
main_circ.append(subcirc0,[0,qreg_2[0],qreg_0[1],1])
main_circ.u(param_1,param_2,-0.165000, 0)
main_circ.cz(qreg_0[1],0)
main_circ.cz(0,qreg_0[1])
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_2[0],qreg_3[0])
main_circ.cz(qreg_0[1],0)
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.cz(1,qreg_3[0])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],1,qreg_2[0]])
main_circ.ry(param_2, qreg_0[0])
main_circ.ry(-0.990000, qreg_0[0])
main_circ.u(param_0,-0.367000,param_2, qreg_2[0])
bindings = {param_0: 0.332000, param_1: 0.170000, param_2: -0.102000, param_3: -0.434000, param_4: -0.552000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "937")
