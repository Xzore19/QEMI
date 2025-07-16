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
subcirc0.u(0,0,0.147000, qreg_0[0])
subcirc0.s(qreg_1[1])
subcirc0.s(qreg_0[0])
subcirc0.rx(0.628000, qreg_0[0])
subcirc0.cz(qreg_1[2],qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.append(subcirc0,[qreg_0[0],2,0,qreg_0[1]])
main_circ.cz(qreg_0[0],0)
main_circ.s(3)
main_circ.s(3)
main_circ.append(subcirc0,[2,0,qreg_0[1],1])
main_circ.append(subcirc0,[1,0,qreg_0[1],3])
main_circ.s(3)
main_circ.rx(param_6, 3)
main_circ.u(param_2,param_2,-0.723000, qreg_0[1])
main_circ.s(0)
main_circ.s(0)
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],0,3,1])
main_circ.rx(0.961000, 3)
main_circ.s(1)
main_circ.s(qreg_0[0])
main_circ.cz(2,3)
main_circ.rx(0.102000, 0)
main_circ.cz(3,qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],2,1,qreg_0[1]])
main_circ.cz(qreg_0[1],3)
main_circ.cz(2,qreg_0[1])
main_circ.cz(1,3)
main_circ.cz(0,qreg_0[0])
main_circ.cz(2,1)
main_circ.cz(3,1)
main_circ.cz(qreg_0[1],0)
main_circ.u(0,param_0,param_6, 3)
main_circ.append(subcirc0,[2,qreg_0[0],3,0])
main_circ.rx(param_4, qreg_0[0])
main_circ.u(0,0,param_7, 0)
bindings = {param_0: -0.016000, param_2: 1.000000, param_4: 0.795000, param_6: 0.923000, param_7: 0.773000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
