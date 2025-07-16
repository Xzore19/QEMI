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
subcirc0.u(pi/2,-0.867000,0.333000, qreg_2[1])
subcirc0.u(0,0,-0.865000, qreg_2[1])
subcirc0.ry(0.255000, qreg_0[1])
subcirc0.cy(qreg_2[1],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.u(pi/2,0.645000,-0.073000, qreg_0[2])
subcirc1.u(pi/2,0.300000,-0.582000, qreg_0[1])
subcirc1.u(0,0,-0.961000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_1[1])
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.ry(-0.871000, qreg_1[0])
subcirc2.ry(-0.062000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,0.361000,0.328000, qreg_0[2])
subcirc3.u(0,0,-0.089000, qreg_0[1])
subcirc3.u(0,0,0.611000, qreg_0[2])
subcirc3.cy(qreg_0[3],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.append(subcirc0,[1,qreg_0[0],0,qreg_0[1],2,3])
main_circ.append(subcirc0,[3,qreg_0[1],1,qreg_0[0],2,0])
main_circ.append(subcirc3,[0,3,qreg_0[0],qreg_0[1],2])
main_circ.append(subcirc0,[qreg_0[1],2,0,1,qreg_0[0],3])
main_circ.u(param_0,0.875000,param_2, 3)
main_circ.append(subcirc0,[0,1,qreg_0[1],2,qreg_0[0],3])
main_circ.cy(qreg_0[1],1)
main_circ.append(subcirc3,[3,2,qreg_0[1],0,qreg_0[0]])
main_circ.u(0,param_4,param_4, qreg_0[0])
main_circ.u(0,param_2,-0.593000, 0)
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],2,0,1,3])
main_circ.cy(2,0)
main_circ.cy(qreg_0[0],0)
main_circ.cy(2,qreg_0[1])
main_circ.u(0,0,-0.399000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],1,2,qreg_0[1],3,0])
main_circ.cy(qreg_0[1],1)
main_circ.u(0,param_2,param_3, 0)
bindings = {param_0: -0.567000, param_2: -0.873000, param_3: 0.669000, param_4: 0.706000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1462")
