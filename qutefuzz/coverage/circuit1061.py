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
subcirc0.u(pi/2,0.964000,-0.937000, qreg_2[0])
subcirc0.cx(qreg_0[1],qreg_2[1])
subcirc0.u(pi/2,0.249000,0.157000, qreg_0[1])
subcirc0.u(-0.672000,-0.731000,0.273000, qreg_2[0])
subcirc0.u(pi/2,0.327000,-0.482000, qreg_2[0])
subcirc0.u(pi/2,-0.679000,0.946000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cx(qreg_1[0],qreg_1[2])
subcirc1.u(pi/2,0.586000,-0.156000, qreg_1[0])
subcirc1.u(-0.225000,0.938000,-0.896000, qreg_1[1])
subcirc1.cx(qreg_1[2],qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_0[0])
subcirc1.x(qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2.u(pi/2,0.234000,-0.709000, qreg_3[0])
subcirc2.u(pi/2,0.659000,-0.589000, qreg_3[0])
subcirc2.u(pi/2,0.216000,-0.492000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
main_circ.u(pi/2,param_2,-0.962000, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.x(qreg_0[3])
main_circ.u(-0.601000,param_2,param_3, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.cx(qreg_0[1],qreg_0[3])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.cx(qreg_0[3],qreg_0[0])
main_circ.u(param_4,param_4,param_5, qreg_0[1])
main_circ.u(0.116000,0.745000,-0.855000, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[3])
main_circ.x(qreg_0[2])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.u(pi/2,param_3,-0.346000, qreg_0[0])
main_circ.u(param_5,0.278000,param_4, qreg_0[3])
main_circ.cx(qreg_0[0],qreg_0[2])
bindings = {param_2: 0.085000, param_3: -0.232000, param_4: 0.688000, param_5: -0.409000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
