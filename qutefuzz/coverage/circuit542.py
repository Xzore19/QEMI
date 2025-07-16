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
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.rz(-0.755000, qreg_2[0])
subcirc0.x(qreg_2[0])
subcirc0.ry(-0.798000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.rz(0.827000, qreg_0[2])
subcirc1.cz(qreg_0[1],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.ry(0.274000, qreg_1[1])
subcirc2.x(qreg_1[1])
subcirc2.ry(0.393000, qreg_0[0])
subcirc2.rz(-0.670000, qreg_1[0])
subcirc2.ry(-0.878000, qreg_1[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rz(0.315000, qreg_0[0])
subcirc3.x(qreg_1[0])
subcirc3.cz(qreg_1[0],qreg_1[1])
subcirc3.ry(0.337000, qreg_1[0])
subcirc3.x(qreg_1[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[1],qreg_0[2])
subcirc4.ry(0.345000, qreg_0[2])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4.cz(qreg_3[0],qreg_0[1])
subcirc4.rz(-0.166000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc4,[1,3,2,0])
main_circ.x(2)
main_circ.ry(-0.430000, 0)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.ry(-0.601000, 0)
main_circ.rz(param_2, 1)
main_circ.append(subcirc4,[1,3,2,0])
main_circ.ry(param_0, 0)
main_circ.x(0)
main_circ.x(0)
main_circ.append(subcirc4,[1,2,3,0])
main_circ.append(subcirc0,[1,0,3,2])
main_circ.append(subcirc4,[1,2,0,3])
main_circ.append(subcirc0,[1,3,2,0])
main_circ.cz(2,1)
main_circ.cz(2,1)
main_circ.rz(param_2, 3)
main_circ.append(subcirc4,[2,3,1,0])
main_circ.rz(-0.227000, 1)
main_circ.rz(-0.080000, 3)
main_circ.rz(-0.943000, 2)
main_circ.ry(param_2, 1)
main_circ.rz(param_0, 3)
main_circ.cz(1,2)
main_circ.cz(3,0)
main_circ.rz(-0.130000, 0)
main_circ.ry(param_0, 0)
bindings = {param_0: -0.291000, param_2: 0.750000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "542")
