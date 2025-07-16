from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_1[0])
subcirc0.cx(qreg_1[1],qreg_0[0])
subcirc0.y(qreg_1[1])
subcirc0.h(qreg_0[0])
subcirc0.u(pi/2,0.012000,0.535000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_2[0])
subcirc1.u(pi/2,0.671000,-0.382000, qreg_2[0])
subcirc1.y(qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.h(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.h(qreg_0[3])
subcirc2.y(qreg_0[1])
subcirc2.y(qreg_0[1])
subcirc2.u(pi/2,0.402000,0.189000, qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(pi/2,-0.269000,-0.694000, qreg_0[0])
subcirc3.y(qreg_1[0])
subcirc3.u(pi/2,0.687000,-0.787000, qreg_0[0])
subcirc3.h(qreg_1[2])
subcirc3.h(qreg_1[1])
subcirc3.cx(qreg_0[0],qreg_1[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[1],3,2,1])
main_circ.append(subcirc3,[qreg_0[1],2,qreg_0[0],1])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],0,3])
main_circ.u(param_0,0.455000,param_0, 1)
main_circ.y(qreg_0[1])
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],3,1])
main_circ.h(0)
main_circ.append(subcirc2,[2,qreg_0[1],1,qreg_0[0],3,0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(0,2)
main_circ.cx(3,qreg_0[1])
main_circ.cx(2,3)
main_circ.cx(3,0)
main_circ.cx(1,3)
main_circ.cx(2,3)
main_circ.cx(qreg_0[0],0)
main_circ.y(0)
main_circ.y(1)
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_0[1],2)
main_circ.h(3)
bindings = {param_0: -0.630000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
