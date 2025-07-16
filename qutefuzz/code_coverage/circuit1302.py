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
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.rx(-0.574000, qreg_0[1])
subcirc0.rx(-0.054000, qreg_0[3])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.x(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.rx(-0.661000, qreg_2[0])
subcirc1.rx(0.676000, qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.x(qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_0[3])
subcirc2.rx(-0.740000, qreg_0[1])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.x(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.rx(0.800000, qreg_0[3])
subcirc3.rx(0.099000, qreg_0[1])
subcirc3.cy(qreg_0[1],qreg_0[2])
subcirc3.cz(qreg_0[2],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.cy(3,2)
main_circ.cy(1,2)
main_circ.rx(param_5, qreg_0[0])
main_circ.x(1)
main_circ.cz(3,1)
main_circ.cz(3,0)
main_circ.cy(qreg_0[0],1)
main_circ.cz(3,0)
main_circ.rx(param_3, 0)
main_circ.x(qreg_0[0])
main_circ.x(1)
main_circ.append(subcirc1,[1,2,0,3])
main_circ.cz(3,2)
main_circ.rx(param_1, 1)
main_circ.cy(2,0)
main_circ.append(subcirc1,[0,2,3,qreg_0[0]])
main_circ.append(subcirc1,[0,3,2,qreg_0[0]])
main_circ.cz(2,1)
main_circ.append(subcirc1,[0,qreg_0[0],2,1])
main_circ.rx(param_3, qreg_0[0])
main_circ.cy(0,qreg_0[0])
main_circ.cy(0,3)
main_circ.cy(1,0)
main_circ.x(1)
main_circ.x(0)
bindings = {param_1: -0.398000, param_3: -0.131000, param_5: -0.249000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
