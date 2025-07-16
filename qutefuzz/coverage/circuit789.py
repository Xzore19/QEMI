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
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0.u(-0.535000,0.043000,0.031000, qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.x(qreg_3[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1.y(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.y(qreg_1[0])
subcirc2.x(qreg_1[0])
subcirc2.y(qreg_2[1])
subcirc2.y(qreg_2[0])
subcirc2.u(-1.000000,0.419000,-0.336000, qreg_2[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_3[0])
subcirc3.u(-0.138000,-0.727000,0.550000, qreg_0[0])
subcirc3.x(qreg_1[1])
subcirc3.u(0.047000,-0.199000,-0.459000, qreg_0[0])
subcirc3.cy(qreg_1[1],qreg_1[0])
subcirc3.x(qreg_1[0])

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

main_circ.cy(2,1)
main_circ.append(subcirc2,[1,qreg_0[0],0,2])
main_circ.append(subcirc3,[2,qreg_0[0],1,3])
main_circ.y(1)
main_circ.append(subcirc3,[2,3,0,1])
main_circ.x(2)
main_circ.cy(3,1)
main_circ.x(1)
main_circ.u(param_0,param_3,0.252000, qreg_0[0])
main_circ.append(subcirc0,[3,1,0,2,qreg_0[0]])
main_circ.append(subcirc0,[2,0,qreg_0[0],3,1])
main_circ.append(subcirc2,[0,1,2,3])
main_circ.cy(qreg_0[0],0)
main_circ.cy(1,0)
main_circ.cy(1,3)
main_circ.cy(qreg_0[0],1)
main_circ.cy(1,2)
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[0],2)
main_circ.u(param_1,-0.596000,param_1, 0)
main_circ.u(param_1,0.325000,0.852000, 1)
main_circ.x(1)
main_circ.y(qreg_0[0])
bindings = {param_0: -0.266000, param_1: 0.211000, param_3: 0.019000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "789")
