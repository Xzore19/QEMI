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
subcirc0.u(-0.806000,0.799000,-0.815000, qreg_0[0])
subcirc0.u(-0.842000,0.262000,0.914000, qreg_0[1])
subcirc0.u(-0.479000,0.009000,-0.468000, qreg_0[3])
subcirc0.rz(-0.032000, qreg_0[1])
subcirc0.u(-0.076000,-0.184000,-0.022000, qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.676000,0.826000,0.690000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.u(0.165000,-0.372000,-0.235000, qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.rz(0.507000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(1)
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

main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.cy(0,qreg_0[3])
main_circ.u(0.154000,param_4,-0.093000, 0)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.u(0.260000,param_4,-0.503000, qreg_0[1])
main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.cy(qreg_0[0],0)
main_circ.cx(0,qreg_0[2])
main_circ.u(param_3,-0.040000,-0.061000, qreg_0[3])
main_circ.cy(0,qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cx(qreg_0[3],qreg_0[0])
main_circ.rz(0.734000, qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],0])
main_circ.cx(0,qreg_0[1])
main_circ.rz(0.219000, qreg_0[0])
main_circ.u(-0.685000,param_3,param_3, 0)
main_circ.rz(0.818000, qreg_0[3])
main_circ.cy(qreg_0[2],0)
main_circ.rz(0.279000, qreg_0[2])
main_circ.cx(qreg_0[1],0)
main_circ.rz(param_1, qreg_0[3])
main_circ.append(subcirc0,[0,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.rz(param_1, qreg_0[3])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.rz(param_0, qreg_0[1])
main_circ.rz(-0.381000, qreg_0[3])
main_circ.cy(0,qreg_0[0])
main_circ.cy(0,qreg_0[1])
main_circ.cy(qreg_0[0],qreg_0[2])
bindings = {param_0: 0.493000, param_1: -0.977000, param_3: -0.387000, param_4: -0.392000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
