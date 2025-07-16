from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.cz(qreg_0[0],qreg_1[1])
subcirc0.rx(-0.565000, qreg_0[0])
subcirc0.rz(-0.840000, qreg_1[2])
subcirc0.rz(-0.561000, qreg_0[0])
subcirc0.rx(0.194000, qreg_1[1])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.956000, qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.rz(-0.661000, qreg_0[2])
subcirc1.rz(-0.576000, qreg_0[2])
subcirc1.rz(-0.323000, qreg_0[2])
subcirc1.y(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_2[1],qreg_1[0])
subcirc2.y(qreg_1[0])
subcirc2.rz(-0.803000, qreg_2[1])
subcirc2.rz(0.795000, qreg_2[1])
subcirc2.rz(0.340000, qreg_1[0])
subcirc2.rx(-0.017000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rz(-0.053000, qreg_1[0])
subcirc3.rz(-0.356000, qreg_1[2])
subcirc3.cz(qreg_1[1],qreg_0[0])
subcirc3.cz(qreg_1[0],qreg_0[0])
subcirc3.y(qreg_1[0])
subcirc3.cz(qreg_1[1],qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_3[0],qreg_0[2])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4.y(qreg_0[1])
subcirc4.rz(0.495000, qreg_3[0])
subcirc4.y(qreg_0[2])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.y(3)
main_circ.cz(qreg_0[1],0)
main_circ.rz(0.980000, 2)
main_circ.rx(0.312000, 2)
main_circ.append(subcirc0,[qreg_0[1],3,2,qreg_0[0]])
main_circ.cz(3,2)
main_circ.append(subcirc3,[qreg_0[0],0,1,3])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[1],3])
main_circ.append(subcirc0,[1,qreg_0[1],2,qreg_0[0]])
main_circ.y(1)
main_circ.cz(qreg_0[0],0)
main_circ.y(1)
main_circ.rz(0.410000, 2)
main_circ.append(subcirc0,[1,qreg_0[0],0,qreg_0[1]])
main_circ.cz(2,1)
main_circ.cz(2,qreg_0[0])
main_circ.cz(1,0)
main_circ.cz(qreg_0[0],1)
main_circ.rz(param_3, 0)
main_circ.rx(-0.652000, 0)
main_circ.y(2)
main_circ.cz(3,0)
main_circ.rz(0.407000, 3)
bindings = {param_3: -0.455000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1273")
