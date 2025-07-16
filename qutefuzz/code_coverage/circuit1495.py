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
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.rx(0.532000, qreg_0[2])
subcirc0.cz(qreg_0[1],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_1[0])
subcirc1.u(0,0,-0.548000, qreg_1[1])
subcirc1.rx(-0.255000, qreg_1[1])
subcirc1.cx(qreg_0[0],qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_1[0],qreg_1[1])
subcirc2.rx(-0.994000, qreg_1[2])
subcirc2.cx(qreg_1[1],qreg_1[2])
subcirc2.rx(0.618000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rx(0.554000, qreg_0[1])
subcirc3.rx(-0.061000, qreg_0[1])
subcirc3.cz(qreg_0[2],qreg_0[0])
subcirc3.cz(qreg_0[3],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.rx(0.804000, qreg_3[0])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],0,qreg_2[0]])
main_circ.rx(-0.587000, qreg_0[0])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.append(subcirc3,[qreg_0[1],qreg_2[0],0,qreg_0[0]])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.cz(0,qreg_0[1])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_3[0],0,qreg_0[1],qreg_2[0]])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[0],0,qreg_2[0]])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_2[0],0])
main_circ.append(subcirc3,[0,qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.append(subcirc3,[0,qreg_3[0],qreg_0[1],qreg_2[0]])
main_circ.rx(0.803000, qreg_2[0])
main_circ.u(0,param_2,param_3, qreg_0[0])
main_circ.rx(param_2, qreg_3[0])
main_circ.u(0,0,0.652000, qreg_2[0])
main_circ.cz(qreg_3[0],qreg_0[1])
main_circ.rx(-0.492000, qreg_3[0])
bindings = {param_2: 0.141000, param_3: -0.998000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1495")
