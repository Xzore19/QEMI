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
subcirc0.cz(qreg_2[0],qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_2[0])
subcirc0.u(-0.304000,-0.111000,-0.687000, qreg_2[0])
subcirc0.u(0.520000,0.641000,-0.310000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.537000,0.270000,0.269000, qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.u(0.777000,-0.290000,0.011000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.y(qreg_2[1])
subcirc2.z(qreg_2[1])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_2[1])
subcirc2.u(0.305000,0.408000,-0.097000, qreg_0[1])
subcirc2.y(qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.u(-0.402000,0.269000,-0.143000, qreg_0[0])
subcirc3.u(-0.632000,0.805000,-0.938000, qreg_3[0])
subcirc3.u(0.147000,0.007000,0.597000, qreg_3[0])
subcirc3.u(0.191000,0.003000,0.418000, qreg_0[2])
subcirc3.cz(qreg_0[2],qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[1],qreg_3[0])
subcirc4.cz(qreg_2[0],qreg_0[0])
subcirc4.cz(qreg_0[0],qreg_0[1])
subcirc4.z(qreg_0[1])
subcirc4.cz(qreg_2[0],qreg_0[1])
subcirc4.z(qreg_3[0])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.cz(1,0)
main_circ.u(param_1,0.116000,param_0, 2)
main_circ.z(qreg_0[1])
main_circ.append(subcirc4,[3,1,2,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[3,qreg_0[1],1,0,qreg_0[0],2])
main_circ.append(subcirc2,[qreg_0[0],1,qreg_0[1],2,3,0])
main_circ.append(subcirc0,[qreg_0[1],2,3,qreg_0[0],0])
main_circ.y(qreg_0[0])
main_circ.u(param_1,-0.823000,0.789000, 3)
main_circ.append(subcirc0,[2,0,qreg_0[0],qreg_0[1],3])
main_circ.append(subcirc2,[2,1,qreg_0[0],qreg_0[1],0,3])
main_circ.append(subcirc0,[2,0,3,1,qreg_0[1]])
main_circ.u(param_1,param_2,0.999000, qreg_0[0])
main_circ.y(1)
main_circ.u(0.242000,-0.376000,param_2, 1)
main_circ.u(-0.739000,0.801000,param_2, qreg_0[1])
bindings = {param_0: -0.365000, param_1: 0.410000, param_2: 0.458000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "686")
