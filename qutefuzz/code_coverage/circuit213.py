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
subcirc0.h(qreg_0[0])
subcirc0.x(qreg_0[2])
subcirc0.rz(0.315000, qreg_0[0])
subcirc0.rz(-0.327000, qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[3])
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.rz(-0.939000, qreg_0[2])
subcirc1.z(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.rz(0.257000, qreg_1[0])
subcirc2.rz(-0.544000, qreg_1[2])
subcirc2.z(qreg_0[0])
subcirc2.h(qreg_1[1])
subcirc2.x(qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_1[1])
subcirc3.h(qreg_3[0])
subcirc3.z(qreg_3[0])
subcirc3.z(qreg_1[0])
subcirc3.h(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.append(subcirc0,[qreg_0[0],1,0,qreg_0[1],qreg_0[2]])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_0[1],qreg_0[3],1])
main_circ.z(qreg_0[3])
main_circ.append(subcirc3,[0,1,qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc2,[0,1,qreg_0[0],qreg_0[3]])
main_circ.append(subcirc3,[qreg_0[1],0,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.h(1)
main_circ.rz(param_1, qreg_0[3])
main_circ.z(qreg_0[1])
main_circ.x(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],1,qreg_0[3]])
main_circ.append(subcirc0,[0,1,qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.x(qreg_0[1])
bindings = {param_1: -0.688000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "213")
