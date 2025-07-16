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
subcirc0.u(0.392000,0.202000,0.107000, qreg_0[0])
subcirc0.y(qreg_3[0])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[2])
subcirc0.z(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.552000, qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.u(0,0,0.507000, qreg_0[3])
subcirc1.u(0,0,0.938000, qreg_0[1])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_1[0])
subcirc2.z(qreg_1[2])
subcirc2.y(qreg_1[0])
subcirc2.z(qreg_1[1])
subcirc2.z(qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(2)
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

main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_0[1],1])
main_circ.append(subcirc2,[1,0,qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc2,[0,qreg_0[1],qreg_0[0],qreg_3[0],1])
main_circ.append(subcirc1,[qreg_0[1],1,qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.z(qreg_0[1])
main_circ.u(param_1,0.537000,param_1, 0)
main_circ.z(qreg_0[1])
main_circ.append(subcirc1,[qreg_0[1],0,1,qreg_0[2]])
main_circ.u(param_0,param_0,param_0, 1)
main_circ.append(subcirc2,[0,qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],0,1])
main_circ.y(qreg_0[2])
main_circ.append(subcirc1,[1,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.y(qreg_0[1])
main_circ.u(0.407000,param_1,param_1, qreg_0[2])
bindings = {param_0: -0.297000, param_1: -0.008000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1807")
