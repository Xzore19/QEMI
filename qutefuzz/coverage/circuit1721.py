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
subcirc0.u(0,0,0.427000, qreg_2[1])
subcirc0.rz(-0.470000, qreg_0[0])
subcirc0.cy(qreg_2[1],qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.924000,-0.636000, qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.u(0,0,0.451000, qreg_3[0])
subcirc1.cy(qreg_0[0],qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.u(0,param_2,param_4, 2)
main_circ.cy(3,1)
main_circ.cy(1,2)
main_circ.cy(1,3)
main_circ.u(0,0,0.103000, 2)
main_circ.u(param_1,param_1,param_4, 3)
main_circ.append(subcirc1,[2,3,0,1])
main_circ.u(pi/2,param_5,param_4, 1)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.u(param_4,-0.418000,param_5, 1)
main_circ.cy(3,1)
main_circ.rz(param_2, 0)
main_circ.u(param_2,0.613000,param_2, 1)
main_circ.u(pi/2,0.590000,param_5, 3)
main_circ.u(pi/2,0.370000,-0.229000, 3)
main_circ.u(0,param_3,-0.815000, 3)
main_circ.u(pi/2,param_5,param_2, 2)
main_circ.u(0,0,param_2, 0)
main_circ.u(param_1,param_1,-0.559000, 0)
main_circ.cy(3,2)
main_circ.rz(0.696000, 0)
main_circ.rz(param_1, 2)
main_circ.u(0,param_1,0.168000, 0)
main_circ.append(subcirc1,[0,1,2,3])
main_circ.cy(2,0)
main_circ.u(param_5,param_2,param_3, 1)
main_circ.rz(-0.319000, 1)
main_circ.u(param_3,0,param_3, 3)
main_circ.u(param_5,param_1,param_5, 1)
main_circ.u(pi/2,-0.861000,0.895000, 2)
main_circ.u(pi/2,0.792000,-0.568000, 1)
main_circ.u(param_5,0.949000,param_5, 1)
main_circ.rz(param_0, 3)
main_circ.u(param_1,param_0,param_3, 2)
bindings = {param_0: -0.017000, param_1: 0.322000, param_2: 0.992000, param_3: 0.893000, param_4: -0.362000, param_5: 0.770000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1721")
