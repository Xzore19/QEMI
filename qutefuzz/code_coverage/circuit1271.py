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
subcirc0.ry(0.374000, qreg_0[1])
subcirc0.rz(-0.276000, qreg_0[1])
subcirc0.rz(-0.280000, qreg_2[1])
subcirc0.z(qreg_2[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.ry(-0.436000, qreg_1[2])
subcirc1.cz(qreg_1[1],qreg_1[0])
subcirc1.z(qreg_1[1])
subcirc1.cz(qreg_1[1],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.ry(0.982000, qreg_2[1])
subcirc2.z(qreg_2[0])
subcirc2.z(qreg_2[0])
subcirc2.rz(-0.870000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(0.287000, qreg_0[3])
subcirc3.z(qreg_0[2])
subcirc3.rz(-0.640000, qreg_0[2])
subcirc3.z(qreg_0[3])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],1,qreg_3[0],qreg_1[1],0])
main_circ.ry(param_0, 1)
main_circ.ry(param_0, 0)
main_circ.append(subcirc1,[qreg_1[0],1,qreg_3[0],0])
main_circ.append(subcirc1,[qreg_1[0],0,qreg_0[0],qreg_1[1]])
main_circ.ry(param_0, qreg_1[0])
main_circ.cz(qreg_0[0],1)
main_circ.append(subcirc0,[0,qreg_1[0],1,qreg_1[1],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_1[0],1])
main_circ.cz(1,qreg_0[0])
main_circ.append(subcirc1,[1,qreg_1[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],1,0])
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.cz(qreg_1[1],qreg_1[0])
main_circ.rz(0.272000, qreg_1[0])
main_circ.append(subcirc3,[0,qreg_1[0],1,qreg_3[0]])
main_circ.ry(0.905000, 0)
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.rz(param_0, qreg_0[0])
bindings = {param_0: 0.187000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1271")
