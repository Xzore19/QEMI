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
subcirc0.y(qreg_0[0])
subcirc0.rz(0.929000, qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.rz(0.420000, qreg_0[0])
subcirc0.rx(0.307000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.496000, qreg_0[0])
subcirc1.rz(0.408000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.491000, qreg_2[0])
subcirc2.y(qreg_3[0])
subcirc2.z(qreg_2[0])
subcirc2.z(qreg_0[1])
subcirc2.rx(-0.352000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(0.179000, qreg_3[0])
subcirc3.rz(0.014000, qreg_0[2])
subcirc3.y(qreg_0[1])
subcirc3.z(qreg_0[1])
subcirc3.y(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.869000, qreg_0[0])
subcirc4.z(qreg_3[0])
subcirc4.y(qreg_2[0])
subcirc4.z(qreg_0[0])
subcirc4.z(qreg_0[0])

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

main_circ.rz(param_3, 3)
main_circ.y(1)
main_circ.append(subcirc4,[0,1,2,3])
main_circ.append(subcirc4,[1,0,3,2])
main_circ.rx(0.588000, 2)
main_circ.y(3)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.rx(0.150000, 2)
main_circ.rz(-0.566000, 3)
main_circ.rx(-0.644000, 2)
main_circ.y(0)
main_circ.rx(param_1, 2)
main_circ.z(3)
main_circ.rx(param_4, 1)
main_circ.append(subcirc4,[2,1,3,0])
main_circ.y(0)
main_circ.rz(-0.263000, 2)
main_circ.y(2)
main_circ.y(0)
main_circ.z(0)
main_circ.y(0)
main_circ.rx(param_2, 3)
main_circ.append(subcirc4,[2,0,1,3])
main_circ.y(2)
main_circ.append(subcirc4,[3,1,2,0])
main_circ.y(0)
main_circ.append(subcirc4,[1,3,0,2])
main_circ.append(subcirc1,[2,0,3,1])
bindings = {param_1: 0.235000, param_2: 0.804000, param_3: 0.381000, param_4: -0.442000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1734")
