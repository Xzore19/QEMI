from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(-0.835000,-0.235000,-0.808000, qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.u(pi/2,-0.465000,0.391000, qreg_0[1])
subcirc0.u(pi/2,0.791000,-0.143000, qreg_3[0])
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0.u(pi/2,0.468000,0.656000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.720000,-0.168000,-0.460000, qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.u(-0.674000,-0.660000,-0.642000, qreg_0[0])
subcirc1.u(pi/2,0.363000,0.538000, qreg_0[2])
subcirc1.u(pi/2,-0.949000,-0.102000, qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_0[2],qreg_3[0])
subcirc2.cx(qreg_0[2],qreg_0[0])
subcirc2.u(-0.840000,0.441000,-0.774000, qreg_0[1])
subcirc2.cx(qreg_0[0],qreg_3[0])
subcirc2.cx(qreg_0[2],qreg_3[0])
subcirc2.u(pi/2,-0.386000,0.861000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[2],qreg_0[1])
subcirc3.u(pi/2,-0.238000,-0.020000, qreg_0[0])
subcirc3.x(qreg_0[2])
subcirc3.u(0.986000,0.785000,-0.052000, qreg_0[0])
subcirc3.u(0.032000,-0.574000,0.429000, qreg_0[0])
subcirc3.cx(qreg_0[2],qreg_3[0])

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

main_circ.u(0.458000,param_0,-0.767000, 0)
main_circ.cx(qreg_0[2],1)
main_circ.x(qreg_0[2])
main_circ.append(subcirc3,[qreg_0[3],0,qreg_0[2],qreg_0[0]])
main_circ.u(0.324000,-0.467000,0.731000, 0)
main_circ.append(subcirc2,[qreg_0[0],1,qreg_0[2],qreg_0[3],0])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],1,0])
main_circ.append(subcirc3,[qreg_0[2],1,qreg_0[0],qreg_0[3]])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[2],1,qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[3],qreg_0[0],0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_0[1],qreg_0[3]])
main_circ.u(param_1,param_0,-0.221000, qreg_0[3])
main_circ.u(pi/2,-0.689000,-0.152000, qreg_0[2])
main_circ.cx(qreg_0[2],qreg_0[0])
bindings = {param_0: -0.461000, param_1: 0.877000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
