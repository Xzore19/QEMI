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
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.ry(0.032000, qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_1[0],qreg_1[1])
subcirc1.ry(-0.012000, qreg_1[0])
subcirc1.u(0,0,-0.977000, qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],0,qreg_0[3]])
main_circ.cy(0,qreg_0[3])
main_circ.cx(qreg_0[1],0)
main_circ.u(param_3,param_1,0.050000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,qreg_0[3]])
main_circ.u(0,0,0.567000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[3],qreg_0[2]])
main_circ.cy(qreg_0[2],qreg_0[3])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[2],0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],0,qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[3],0,qreg_0[2],qreg_0[1]])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],0,qreg_0[1]])
main_circ.cx(qreg_0[2],0)
main_circ.cx(qreg_0[3],qreg_0[1])
main_circ.u(param_1,0,param_3, qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.u(param_1,param_0,param_0, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_0[3]])
main_circ.cx(qreg_0[2],qreg_0[1])
bindings = {param_0: 0.581000, param_1: 0.841000, param_3: 0.625000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1879")
