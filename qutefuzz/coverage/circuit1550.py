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
subcirc0.u(0,0,0.391000, qreg_0[1])
subcirc0.rx(-0.566000, qreg_0[0])
subcirc0.rx(-0.971000, qreg_0[0])
subcirc0.u(0,0,0.452000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_1[0],qreg_0[0])
subcirc1.rx(0.333000, qreg_1[0])
subcirc1.rx(-0.065000, qreg_1[1])
subcirc1.cz(qreg_0[0],qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.480000, qreg_0[2])
subcirc2.u(0,0,-0.603000, qreg_0[1])
subcirc2.rx(-0.784000, qreg_0[3])
subcirc2.rx(-0.385000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[0,2,1,qreg_0[0],3])
main_circ.append(subcirc2,[3,1,2,qreg_0[0]])
main_circ.append(subcirc1,[2,1,0,qreg_0[0],qreg_0[1]])
main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.append(subcirc2,[1,2,0,qreg_0[1]])
main_circ.z(qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],3])
main_circ.u(param_0,0,0.952000, 0)
main_circ.z(1)
main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[0],2])
main_circ.cz(0,qreg_0[1])
main_circ.append(subcirc1,[3,1,qreg_0[0],qreg_0[1],2])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(2,3)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(0,3)
main_circ.cz(1,0)
main_circ.append(subcirc2,[0,3,1,qreg_0[0]])
main_circ.rx(param_0, 1)
bindings = {param_0: 0.865000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1550")
