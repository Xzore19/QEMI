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
subcirc0.u(pi/2,-0.359000,-0.095000, qreg_0[2])
subcirc0.u(pi/2,0.592000,-0.033000, qreg_0[0])
subcirc0.rx(-0.278000, qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.377000, qreg_2[1])
subcirc1.rx(-0.509000, qreg_0[1])
subcirc1.rx(0.085000, qreg_2[0])
subcirc1.cx(qreg_0[1],qreg_2[0])
subcirc1.cx(qreg_2[0],qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.773000, qreg_0[2])
subcirc2.rx(-0.279000, qreg_0[3])
subcirc2.cx(qreg_0[3],qreg_0[0])
subcirc2.u(0,0,0.318000, qreg_0[3])
subcirc2.u(0,0,-0.380000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,-0.697000,0.996000, qreg_0[2])
subcirc3.u(pi/2,0.475000,-0.128000, qreg_3[0])
subcirc3.u(0,0,-0.228000, qreg_0[0])
subcirc3.u(pi/2,0.004000,0.266000, qreg_0[1])
subcirc3.u(pi/2,-0.138000,-0.257000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cx(qreg_0[0],qreg_0[1])
subcirc4.cx(qreg_0[1],qreg_2[0])
subcirc4.u(0,0,-0.310000, qreg_2[1])
subcirc4.u(0,0,-0.257000, qreg_0[0])
subcirc4.rx(-0.536000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc1,[qreg_1[0],1,2,0])
main_circ.append(subcirc2,[1,3,0,2])
main_circ.cx(2,1)
main_circ.append(subcirc2,[1,qreg_1[0],qreg_0[0],0])
main_circ.append(subcirc2,[1,qreg_0[0],0,2])
main_circ.u(param_1,0,-0.664000, 3)
main_circ.append(subcirc1,[2,3,1,qreg_1[0]])
main_circ.u(param_2,param_2,param_1, 3)
main_circ.u(0,param_2,0.604000, qreg_1[0])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],1,0])
main_circ.cx(1,qreg_1[0])
main_circ.cx(1,2)
main_circ.cx(qreg_0[0],3)
main_circ.cx(1,qreg_0[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.u(pi/2,0.844000,param_1, 2)
main_circ.u(0,0,param_1, 3)
main_circ.u(param_2,0,-0.326000, 0)
main_circ.cx(qreg_1[0],2)
main_circ.rx(0.956000, qreg_0[0])
bindings = {param_1: 0.432000, param_2: 0.579000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "245")
