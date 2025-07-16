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
subcirc0.cz(qreg_3[0],qreg_0[2])
subcirc0.u(0.770000,0.581000,-0.009000, qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.append(subcirc0,[0,2,qreg_0[0],3,1])
main_circ.cx(0,qreg_0[0])
main_circ.cz(3,2)
main_circ.append(subcirc0,[1,3,qreg_0[0],0,2])
main_circ.x(1)
main_circ.append(subcirc0,[2,qreg_0[0],0,1,3])
main_circ.append(subcirc0,[0,qreg_0[0],2,1,3])
main_circ.x(2)
main_circ.u(param_0,param_0,-0.309000, 0)
main_circ.cz(0,2)
main_circ.cz(1,3)
main_circ.u(param_2,0.851000,-0.635000, 3)
main_circ.x(0)
main_circ.u(0.481000,0.965000,param_1, 3)
main_circ.cx(2,0)
main_circ.cx(1,3)
main_circ.u(-0.908000,param_1,param_1, 1)
main_circ.cz(2,qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.cx(2,qreg_0[0])
main_circ.cx(2,0)
main_circ.x(3)
main_circ.cz(2,1)
main_circ.u(param_1,param_0,-0.578000, qreg_0[0])
main_circ.u(0.811000,param_0,param_0, qreg_0[0])
main_circ.append(subcirc0,[1,qreg_0[0],2,0,3])
main_circ.x(2)
main_circ.x(2)
main_circ.cx(0,1)
bindings = {param_0: 0.430000, param_1: -0.415000, param_2: -0.348000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
