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
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.rx(0.607000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rx(param_0, 1)
main_circ.cx(qreg_0[3],qreg_0[2])
main_circ.u(param_2,0,param_0, qreg_0[2])
main_circ.x(qreg_0[3])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[3],1,0,qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],0,qreg_0[0],1,qreg_0[3]])
main_circ.x(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0],1,0])
main_circ.x(1)
main_circ.rx(-0.374000, qreg_0[0])
main_circ.u(param_2,0,param_0, qreg_0[0])
main_circ.u(0,0,param_3, qreg_0[3])
main_circ.u(0,param_0,-0.152000, qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.append(subcirc0,[1,qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0],0])
main_circ.rx(param_3, qreg_0[2])
main_circ.cx(qreg_0[0],1)
main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[2],qreg_0[3],1,qreg_0[0]])
main_circ.cx(1,qreg_0[1])
main_circ.rx(param_0, qreg_0[1])
main_circ.rx(0.574000, qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.u(0,0,-0.207000, qreg_0[0])
main_circ.u(0,0,0.236000, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_0[2],qreg_0[3],1])
main_circ.rx(-0.732000, qreg_0[2])
main_circ.x(1)
main_circ.x(qreg_0[2])
main_circ.x(qreg_0[3])
main_circ.x(qreg_0[1])
main_circ.u(0,param_0,param_3, qreg_0[1])
main_circ.rx(-0.571000, qreg_0[2])
main_circ.cx(qreg_0[1],1)
main_circ.u(0,0,param_3, qreg_0[1])
bindings = {param_0: 0.530000, param_2: 0.177000, param_3: 0.746000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
