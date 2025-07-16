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
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.u(0,0,0.776000, qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.ry(0.408000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_1[0])
subcirc1.ry(-0.509000, qreg_1[0])
subcirc1.u(0,0,-0.259000, qreg_1[0])
subcirc1.u(0,0,0.474000, qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.ry(-0.404000, 0)
main_circ.ry(0.780000, 1)
main_circ.cy(3,2)
main_circ.z(2)
main_circ.z(1)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.ry(param_0, 1)
main_circ.cy(2,0)
main_circ.ry(param_0, 1)
main_circ.cy(3,0)
main_circ.u(0,0,0.252000, 0)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.cy(1,0)
main_circ.u(0,param_0,-0.151000, 0)
main_circ.u(param_0,0,-0.572000, 1)
main_circ.z(1)
main_circ.u(0,param_0,-0.853000, 0)
main_circ.u(0,param_0,param_0, 3)
main_circ.z(0)
main_circ.cy(3,1)
main_circ.u(0,0,-0.549000, 1)
main_circ.z(0)
main_circ.u(0,0,0.409000, 3)
main_circ.z(0)
main_circ.z(2)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.u(0,0,-0.782000, 0)
main_circ.cy(0,3)
main_circ.cy(3,1)
main_circ.cy(3,1)
main_circ.cy(2,0)
main_circ.cy(1,2)
main_circ.cy(1,3)
main_circ.cy(3,2)
main_circ.cy(1,2)
main_circ.cy(0,3)
main_circ.ry(-0.374000, 1)
main_circ.u(0,param_0,param_0, 0)
main_circ.u(0,0,-0.995000, 3)
main_circ.cy(0,1)
main_circ.ry(param_0, 2)
bindings = {param_0: 0.052000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
