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
subcirc0.cy(qreg_0[2],qreg_0[3])
subcirc0.u(0,0,0.515000, qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[1],qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[3])
subcirc1.u(0.837000,-0.782000,0.695000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.u(0,0,0.686000, qreg_0[1])
subcirc2.u(0,0,-0.977000, qreg_0[1])
subcirc2.u(0.930000,0.697000,0.539000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[1],qreg_0[0])
subcirc3.u(0,0,0.425000, qreg_0[0])
subcirc3.u(0.312000,0.707000,-0.792000, qreg_0[2])
subcirc3.u(-0.169000,-0.874000,0.285000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0.471000,0.605000,-0.919000, qreg_0[1])
subcirc4.u(0.606000,0.200000,-0.513000, qreg_0[0])
subcirc4.x(qreg_0[1])
subcirc4.x(qreg_0[3])

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
param_2 = Parameter("param_2")

main_circ.cy(2,3)
main_circ.append(subcirc1,[1,2,qreg_0[0],0])
main_circ.append(subcirc4,[0,2,qreg_0[0],1])
main_circ.cy(3,1)
main_circ.append(subcirc3,[qreg_0[1],1,2,qreg_0[0],3,0])
main_circ.x(0)
main_circ.append(subcirc0,[2,1,0,qreg_0[0]])
main_circ.append(subcirc4,[0,qreg_0[0],3,2])
main_circ.append(subcirc1,[1,3,0,2])
main_circ.x(1)
main_circ.append(subcirc1,[qreg_0[1],3,2,0])
main_circ.append(subcirc0,[2,qreg_0[0],1,qreg_0[1]])
main_circ.cy(3,1)
main_circ.cy(qreg_0[0],2)
main_circ.u(param_0,param_1,0.236000, qreg_0[1])
main_circ.append(subcirc3,[qreg_0[0],3,0,2,1,qreg_0[1]])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.append(subcirc4,[0,qreg_0[1],1,qreg_0[0]])
bindings = {param_0: 0.954000, param_1: -0.638000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1569")
