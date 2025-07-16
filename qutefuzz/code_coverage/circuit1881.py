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
subcirc0.u(pi/2,0.198000,0.529000, qreg_2[0])
subcirc0.u(pi/2,-0.553000,-0.062000, qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.rx(0.819000, qreg_0[1])
subcirc0.rx(0.153000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.983000,-0.886000, qreg_1[0])
subcirc1.s(qreg_1[1])
subcirc1.rx(-0.724000, qreg_0[0])
subcirc1.x(qreg_1[0])
subcirc1.s(qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.354000,0.742000, qreg_0[1])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2.rx(-0.011000, qreg_0[1])
subcirc2.s(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.rx(-0.892000, qreg_0[1])
subcirc3.u(pi/2,0.951000,0.673000, qreg_0[0])
subcirc3.x(qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,0.917000,-0.010000, qreg_0[1])
subcirc4.u(pi/2,0.384000,0.760000, qreg_3[0])
subcirc4.u(pi/2,0.020000,0.776000, qreg_0[2])
subcirc4.rx(-0.403000, qreg_0[2])
subcirc4.u(pi/2,-0.788000,0.352000, qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,0.330000,0.533000, 1)
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],1,qreg_0[1],qreg_0[0],0])
main_circ.s(1)
main_circ.append(subcirc1,[qreg_3[0],1,0,qreg_0[0]])
main_circ.u(param_1,param_0,param_1, 1)
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],1,0,qreg_0[0]])
main_circ.s(qreg_0[2])
main_circ.append(subcirc0,[1,qreg_0[2],0,qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[2],1])
main_circ.u(param_1,0.303000,-0.971000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[2],1])
main_circ.rx(param_0, 0)
main_circ.s(qreg_0[2])
main_circ.append(subcirc3,[0,qreg_0[1],qreg_0[0],1,qreg_3[0],qreg_0[2]])
main_circ.s(0)
main_circ.rx(-0.364000, qreg_3[0])
main_circ.x(qreg_0[0])
main_circ.s(1)
main_circ.x(1)
main_circ.append(subcirc2,[0,qreg_0[1],1,qreg_0[0],qreg_3[0]])
main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],0,qreg_0[0],qreg_0[2]])
main_circ.s(qreg_0[1])
main_circ.s(qreg_3[0])
bindings = {param_0: -0.396000, param_1: 0.467000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
