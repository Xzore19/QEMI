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
subcirc0.h(qreg_0[3])
subcirc0.rx(-0.944000, qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0.rx(-0.256000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.rx(-0.891000, qreg_0[0])
subcirc1.h(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.716000, qreg_3[0])
subcirc2.rx(0.939000, qreg_0[0])
subcirc2.z(qreg_2[0])
subcirc2.rx(-0.217000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(-0.693000, qreg_0[2])
subcirc3.z(qreg_3[0])
subcirc3.rx(0.721000, qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rx(-0.066000, qreg_0[3])
subcirc4.y(qreg_0[1])
subcirc4.h(qreg_0[0])
subcirc4.y(qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.append(subcirc4,[0,qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_3[0],0])
main_circ.y(qreg_3[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc3,[0,qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.rx(-0.294000, qreg_3[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0],0])
main_circ.append(subcirc0,[qreg_3[0],0,qreg_0[2],qreg_0[1]])
main_circ.append(subcirc2,[qreg_3[0],qreg_0[2],0,qreg_0[1]])
main_circ.rx(param_1, qreg_0[2])
main_circ.rx(0.221000, qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.z(0)
main_circ.z(qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],0,qreg_0[0],qreg_0[2]])
main_circ.append(subcirc0,[0,qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.append(subcirc4,[qreg_0[1],qreg_0[0],0,qreg_3[0]])
main_circ.z(0)
main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.append(subcirc3,[qreg_3[0],0,qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.z(0)
bindings = {param_1: -0.934000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1757")
