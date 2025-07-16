from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.h(qreg_2[0])
subcirc0.u(0.064000,-0.526000,-0.757000, qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_2[1])
subcirc0.u(0.573000,0.795000,-0.928000, qreg_2[0])
subcirc0.h(qreg_2[1])
subcirc0.cx(qreg_2[1],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_1[0],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_1[0])
subcirc1.u(0.967000,-0.497000,0.990000, qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.u(-0.435000,-0.612000,0.278000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2.rx(0.150000, qreg_0[2])
subcirc2.h(qreg_0[2])
subcirc2.h(qreg_0[2])
subcirc2.u(-0.292000,0.811000,-0.749000, qreg_0[1])
subcirc2.u(0.535000,0.547000,0.688000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[1])
subcirc3.cx(qreg_0[2],qreg_0[3])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_0[0])
subcirc3.u(0.016000,0.961000,-0.292000, qreg_0[1])
subcirc3.rx(0.099000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc3,[2,3,1,0])
main_circ.append(subcirc3,[1,3,0,2])
main_circ.append(subcirc2,[3,2,0,1])
main_circ.u(-0.741000,param_3,param_2, 0)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.append(subcirc2,[1,2,0,3])
main_circ.cx(1,0)
main_circ.cx(2,3)
main_circ.cx(0,2)
main_circ.cx(1,2)
main_circ.cx(2,0)
main_circ.h(0)
main_circ.rx(-0.443000, 0)
main_circ.rx(param_3, 2)
main_circ.cx(1,2)
main_circ.u(param_0,0.034000,0.211000, 0)
main_circ.h(3)
bindings = {param_0: -0.074000, param_2: -0.305000, param_3: 0.539000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
