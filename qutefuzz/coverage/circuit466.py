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
subcirc0.y(qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_1[2])
subcirc0.rx(-0.724000, qreg_0[0])
subcirc0.rx(-0.191000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.y(qreg_0[0])
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_3[0])
subcirc2.cy(qreg_0[1],qreg_3[0])
subcirc2.rx(-0.573000, qreg_0[2])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[3])
subcirc3.rx(-0.417000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(2)
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
param_1 = Parameter("param_1")

main_circ.append(subcirc3,[1,qreg_0[0],0,qreg_2[0],qreg_2[1],qreg_0[1]])
main_circ.z(1)
main_circ.rx(param_0, qreg_0[1])
main_circ.y(qreg_2[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(0,1)
main_circ.append(subcirc1,[0,qreg_0[1],1,qreg_2[0]])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],1,0])
main_circ.z(qreg_2[0])
main_circ.append(subcirc3,[qreg_0[0],0,1,qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.rx(param_0, qreg_2[1])
main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[1],qreg_2[0]])
main_circ.z(qreg_2[0])
main_circ.rx(0.228000, 0)
main_circ.cy(qreg_2[0],0)
main_circ.cy(0,qreg_0[1])
main_circ.append(subcirc1,[qreg_2[1],1,qreg_0[0],qreg_2[0]])
main_circ.append(subcirc0,[0,qreg_0[0],1,qreg_2[1]])
main_circ.append(subcirc3,[qreg_2[0],1,0,qreg_2[1],qreg_0[0],qreg_0[1]])
main_circ.cy(0,qreg_2[1])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.cy(qreg_0[1],1)
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.append(subcirc3,[qreg_0[0],1,qreg_2[0],qreg_0[1],qreg_2[1],0])
main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_0, qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.rx(param_0, qreg_2[1])
main_circ.rx(-0.797000, 1)
bindings = {param_0: 0.563000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "466")
