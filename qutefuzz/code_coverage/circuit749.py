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
subcirc0.rx(0.452000, qreg_0[1])
subcirc0.u(0.115000,-0.818000,-0.595000, qreg_3[0])
subcirc0.u(0.277000,-0.032000,0.899000, qreg_0[2])
subcirc0.rx(0.882000, qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.451000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.u(-0.403000,0.082000,-0.942000, qreg_0[0])
subcirc1.u(-0.235000,-0.483000,0.607000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0.574000,0.938000,0.232000, qreg_1[1])
subcirc2.rx(-0.695000, qreg_1[2])
subcirc2.u(0.816000,-0.149000,-0.884000, qreg_0[0])
subcirc2.y(qreg_1[1])
subcirc2.y(qreg_1[1])
subcirc2.u(0.323000,-0.148000,0.970000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[1],qreg_2[0]])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.u(-0.715000,param_3,-0.191000, qreg_0[1])
main_circ.u(0.947000,0.271000,-0.487000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.y(qreg_2[1])
main_circ.y(qreg_0[1])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.rx(-0.439000, qreg_0[1])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.rx(param_1, qreg_0[1])
main_circ.u(param_2,0.388000,-0.795000, qreg_0[1])
main_circ.u(param_2,param_0,param_1, qreg_0[1])
main_circ.rx(param_1, qreg_0[0])
main_circ.u(0.710000,0.216000,param_3, qreg_2[1])
main_circ.rx(param_0, qreg_0[1])
main_circ.cz(qreg_2[0],qreg_2[1])
main_circ.rx(0.989000, qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_2[1],qreg_2[0])
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.cz(qreg_0[1],qreg_2[1])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_2[1])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.cz(qreg_2[1],qreg_2[0])
main_circ.y(qreg_2[0])
main_circ.rx(0.140000, qreg_0[0])
bindings = {param_0: -0.177000, param_1: 0.910000, param_2: 0.890000, param_3: 0.810000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "749")
