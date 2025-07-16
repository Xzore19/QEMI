from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_0[1])
subcirc0.u(0.148000,0.822000,-0.386000, qreg_2[1])
subcirc0.u(-0.912000,-0.328000,-0.712000, qreg_2[1])
subcirc0.cz(qreg_2[0],qreg_2[1])
subcirc0.u(-0.682000,-0.669000,0.446000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(-0.760000,-0.932000,0.454000, qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.z(qreg_2[1])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.cz(qreg_2[0],qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[2])
subcirc2.u(0.423000,0.204000,-0.470000, qreg_0[3])
subcirc2.s(qreg_0[0])
subcirc2.cz(qreg_0[3],qreg_0[0])
subcirc2.z(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.z(qreg_0[1])
subcirc3.u(-0.961000,-0.440000,-0.206000, qreg_2[0])
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.s(qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.cz(1,2)
main_circ.cz(2,1)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.cz(2,0)
main_circ.s(1)
main_circ.cz(3,0)
main_circ.z(0)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.s(0)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.append(subcirc3,[3,1,0,2])
main_circ.append(subcirc3,[0,1,3,2])
main_circ.append(subcirc0,[0,3,1,2])
main_circ.u(0.113000,param_3,param_2, 1)
main_circ.cz(3,1)
main_circ.cz(2,0)
main_circ.append(subcirc3,[2,1,0,3])
main_circ.z(2)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.s(3)
main_circ.z(0)
main_circ.s(0)
bindings = {param_2: 0.628000, param_3: 0.592000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "344")
