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
subcirc0.rx(0.804000, qreg_0[0])
subcirc0.u(-0.890000,0.751000,-0.743000, qreg_0[1])
subcirc0.u(-0.846000,-0.285000,-0.778000, qreg_3[0])
subcirc0.rx(-0.598000, qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.184000,0.308000,0.783000, qreg_0[2])
subcirc1.y(qreg_0[0])
subcirc1.rx(0.493000, qreg_0[1])
subcirc1.cx(qreg_0[3],qreg_0[1])
subcirc1.cx(qreg_0[0],qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.274000, qreg_0[3])
subcirc2.cx(qreg_0[3],qreg_0[0])
subcirc2.y(qreg_0[3])
subcirc2.y(qreg_0[0])
subcirc2.rx(0.777000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_3[0],qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_3[0])
subcirc3.rx(-0.414000, qreg_0[1])
subcirc3.cx(qreg_0[2],qreg_0[1])
subcirc3.cx(qreg_3[0],qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(1)
main_circ.rx(0.876000, 1)
main_circ.cx(2,0)
main_circ.rx(param_1, 1)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.rx(-0.125000, 1)
main_circ.append(subcirc2,[0,2,1,3])
main_circ.cx(0,1)
main_circ.append(subcirc2,[0,2,1,3])
main_circ.append(subcirc1,[1,3,2,0])
main_circ.y(1)
main_circ.u(0.194000,param_2,param_0, 0)
main_circ.u(param_2,-0.607000,param_2, 2)
main_circ.u(-0.855000,param_0,0.016000, 1)
main_circ.append(subcirc3,[2,3,0,1])
main_circ.append(subcirc3,[3,1,2,0])
main_circ.cx(1,0)
main_circ.y(2)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.append(subcirc3,[2,1,0,3])
main_circ.y(1)
main_circ.rx(param_2, 2)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.rx(-0.161000, 1)
main_circ.rx(-0.295000, 1)
bindings = {param_0: 0.724000, param_1: -0.401000, param_2: 0.872000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "465")
