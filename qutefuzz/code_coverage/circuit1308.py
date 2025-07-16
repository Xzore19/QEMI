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
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.y(qreg_2[0])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.u(0,0,-0.849000, qreg_0[2])
subcirc1.z(qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.y(qreg_1[0])
subcirc2.u(0,0,0.533000, qreg_1[1])
subcirc2.u(0,0,-0.696000, qreg_1[2])
subcirc2.y(qreg_1[0])

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

main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_1[1],qreg_3[0]])
main_circ.u(0,param_0,0.601000, 0)
main_circ.z(qreg_3[0])
main_circ.append(subcirc2,[1,qreg_0[0],qreg_3[0],qreg_1[1]])
main_circ.y(1)
main_circ.y(qreg_1[1])
main_circ.z(qreg_3[0])
main_circ.append(subcirc2,[1,qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc2,[qreg_1[0],qreg_1[1],qreg_3[0],1])
main_circ.y(qreg_1[0])
main_circ.append(subcirc0,[0,1,qreg_3[0],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc2,[0,qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.cy(qreg_0[0],0)
main_circ.u(0,0,param_0, 1)
main_circ.y(qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[1],0,1,qreg_1[0]])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.cy(1,0)
main_circ.cy(qreg_1[0],qreg_1[1])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cy(1,qreg_3[0])
main_circ.cy(qreg_1[1],1)
main_circ.cy(1,qreg_1[1])
main_circ.cy(qreg_1[1],1)
main_circ.cy(0,qreg_1[1])
main_circ.cy(1,qreg_1[1])
main_circ.cy(0,qreg_1[1])
main_circ.cy(qreg_0[0],qreg_3[0])
bindings = {param_0: -0.041000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1308")
