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
subcirc0.z(qreg_0[3])
subcirc0.rz(-0.214000, qreg_0[3])
subcirc0.rz(0.526000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.rz(0.942000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(0.742000, qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.y(qreg_2[0])
subcirc2.z(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.rz(-0.645000, qreg_0[0])
subcirc2.y(qreg_2[0])
subcirc2.rz(0.796000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(-0.349000, qreg_0[1])
subcirc3.x(qreg_0[1])
subcirc3.z(qreg_0[3])
subcirc3.x(qreg_0[2])
subcirc3.z(qreg_0[0])
subcirc3.y(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_0[1])
subcirc4.y(qreg_3[0])
subcirc4.x(qreg_0[2])
subcirc4.rz(0.237000, qreg_0[1])
subcirc4.z(qreg_3[0])
subcirc4.rz(0.369000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc4,[qreg_0[0],1,3,0])
main_circ.append(subcirc4,[3,1,0,qreg_0[0]])
main_circ.z(0)
main_circ.append(subcirc0,[qreg_0[0],3,0,2,1])
main_circ.z(0)
main_circ.append(subcirc0,[3,1,qreg_0[0],0,2])
main_circ.append(subcirc4,[1,0,2,3])
main_circ.rz(param_0, 0)
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[1,0,3,qreg_0[0],2])
main_circ.append(subcirc4,[1,0,qreg_0[0],3])
main_circ.z(2)
main_circ.x(3)
main_circ.z(qreg_0[0])
main_circ.x(2)
main_circ.x(2)
bindings = {param_0: -0.075000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
