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
subcirc0.rz(0.340000, qreg_1[0])
subcirc0.u(-0.669000,0.421000,-0.323000, qreg_1[2])
subcirc0.rz(0.292000, qreg_1[1])
subcirc0.u(-0.022000,0.431000,-0.069000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.709000,0.167000,0.081000, qreg_0[1])
subcirc1.rz(-0.218000, qreg_0[1])
subcirc1.rz(-0.473000, qreg_0[2])
subcirc1.y(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.rz(-0.791000, qreg_3[0])
subcirc2.rz(-0.388000, qreg_3[0])
subcirc2.y(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.y(qreg_1[0])
subcirc3.y(qreg_1[2])
subcirc3.y(qreg_1[2])
subcirc3.y(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(-0.084000,0.792000,0.493000, qreg_3[0])
subcirc4.cz(qreg_3[0],qreg_0[0])
subcirc4.y(qreg_0[2])
subcirc4.cz(qreg_0[0],qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(0.407000,param_0,-0.954000, qreg_0[0])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.u(param_0,0.117000,param_0, qreg_2[1])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.rz(0.281000, qreg_0[1])
main_circ.u(0.089000,0.058000,-0.945000, qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.append(subcirc1,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.u(-0.248000,param_0,-0.874000, qreg_0[0])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.cz(qreg_2[1],qreg_0[1])
main_circ.cz(qreg_2[1],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.y(qreg_2[0])
main_circ.y(qreg_2[0])
bindings = {param_0: 0.993000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
