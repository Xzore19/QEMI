from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_1[1],qreg_3[0])
subcirc0.y(qreg_3[0])
subcirc0.u(-0.123000,-0.996000,-0.739000, qreg_1[1])
subcirc0.u(pi/2,-0.524000,0.881000, qreg_0[0])
subcirc0.u(-0.589000,0.668000,-0.007000, qreg_3[0])
subcirc0.y(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.448000,0.380000,-0.601000, qreg_0[0])
subcirc1.u(0.868000,0.500000,0.022000, qreg_0[1])
subcirc1.u(0.201000,0.105000,-0.927000, qreg_0[3])
subcirc1.y(qreg_0[1])
subcirc1.u(0.116000,-0.446000,-0.283000, qreg_0[0])
subcirc1.u(0.933000,0.742000,0.978000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.092000,-0.142000,0.323000, qreg_3[0])
subcirc2.y(qreg_3[0])
subcirc2.u(-0.498000,0.361000,0.563000, qreg_3[0])
subcirc2.u(pi/2,0.756000,0.634000, qreg_0[0])
subcirc2.y(qreg_3[0])
subcirc2.y(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_2[0])
subcirc3.u(pi/2,-0.346000,0.296000, qreg_2[1])
subcirc3.u(0.352000,0.884000,-0.702000, qreg_2[1])
subcirc3.u(-0.948000,0.335000,-0.415000, qreg_2[0])
subcirc3.y(qreg_2[0])
subcirc3.cz(qreg_2[0],qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cz(2,qreg_0[0])
main_circ.u(0.461000,param_1,-0.122000, qreg_0[0])
main_circ.append(subcirc2,[3,qreg_0[0],1,2])
main_circ.append(subcirc2,[2,1,qreg_0[0],3])
main_circ.y(qreg_0[0])
main_circ.cz(1,0)
main_circ.append(subcirc3,[qreg_0[0],0,2,1,qreg_0[1]])
main_circ.append(subcirc1,[0,1,3,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],3,2,1])
main_circ.append(subcirc2,[0,2,qreg_0[0],3])
main_circ.cz(qreg_0[1],0)
main_circ.cz(3,2)
main_circ.cz(0,2)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(0,qreg_0[1])
main_circ.cz(qreg_0[1],3)
main_circ.cz(0,3)
main_circ.cz(0,qreg_0[1])
main_circ.cz(qreg_0[1],0)
main_circ.cz(qreg_0[1],qreg_0[0])
bindings = {param_1: -0.722000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1785")
