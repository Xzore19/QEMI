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
subcirc0.y(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.ry(-0.314000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_1[1],qreg_1[2])
subcirc1.z(qreg_1[1])
subcirc1.y(qreg_1[2])
subcirc1.y(qreg_1[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_1[2])
subcirc2.ry(0.432000, qreg_1[2])
subcirc2.ry(-0.954000, qreg_1[1])
subcirc2.cz(qreg_1[1],qreg_1[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[3],qreg_0[2])
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3.y(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(qreg_0[0])
main_circ.cz(qreg_0[0],2)
main_circ.cz(3,2)
main_circ.append(subcirc3,[0,1,2,qreg_1[0]])
main_circ.append(subcirc2,[2,3,0,qreg_1[0]])
main_circ.append(subcirc3,[qreg_1[0],0,qreg_0[0],2])
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],1,3,2,0])
main_circ.append(subcirc3,[0,qreg_1[0],1,3])
main_circ.append(subcirc2,[qreg_0[0],3,2,qreg_1[0]])
main_circ.z(2)
main_circ.y(qreg_1[0])
main_circ.ry(param_0, qreg_1[0])
main_circ.z(qreg_1[0])
main_circ.cz(3,qreg_1[0])
main_circ.ry(-0.614000, 1)
main_circ.y(3)
main_circ.append(subcirc1,[0,3,1,2,qreg_0[0],qreg_1[0]])
main_circ.cz(3,qreg_0[0])
main_circ.cz(2,1)
main_circ.append(subcirc3,[1,qreg_1[0],3,2])
main_circ.ry(param_0, 3)
main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],0,3])
bindings = {param_0: 0.736000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "978")
