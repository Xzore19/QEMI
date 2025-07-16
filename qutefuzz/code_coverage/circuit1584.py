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
subcirc0.u(pi/2,0.028000,0.525000, qreg_0[0])
subcirc0.u(pi/2,0.789000,-0.902000, qreg_0[1])
subcirc0.u(pi/2,-0.188000,0.510000, qreg_0[2])
subcirc0.rx(0.300000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.847000,0.663000, qreg_0[3])
subcirc1.u(pi/2,-0.554000,-0.627000, qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.u(pi/2,-0.116000,-0.822000, qreg_0[0])
subcirc1.u(pi/2,-0.784000,-0.405000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[2])
subcirc2.u(pi/2,0.870000,0.936000, qreg_0[0])
subcirc2.rx(-0.520000, qreg_0[1])
subcirc2.u(pi/2,-0.644000,0.763000, qreg_0[1])
subcirc2.h(qreg_0[1])

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
param_3 = Parameter("param_3")

main_circ.append(subcirc2,[1,2,0,3])
main_circ.append(subcirc2,[3,2,1,0])
main_circ.u(param_1,0.597000,0.547000, 3)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.h(3)
main_circ.append(subcirc1,[0,2,3,1])
main_circ.cy(2,1)
main_circ.u(param_2,0.459000,0.028000, 0)
main_circ.append(subcirc2,[3,1,2,0])
main_circ.u(pi/2,0.350000,-0.550000, 2)
main_circ.h(2)
main_circ.rx(param_0, 3)
main_circ.rx(param_1, 0)
main_circ.append(subcirc1,[3,2,0,1])
main_circ.cy(0,2)
main_circ.cy(2,1)
main_circ.cy(3,2)
main_circ.cy(0,2)
main_circ.cy(0,3)
main_circ.cy(3,2)
main_circ.cy(0,2)
main_circ.cy(1,3)
main_circ.cy(3,0)
main_circ.cy(1,2)
main_circ.cy(2,0)
main_circ.cy(1,3)
main_circ.rx(param_1, 0)
main_circ.h(2)
main_circ.cy(3,1)
main_circ.cy(2,0)
bindings = {param_0: -0.799000, param_1: 0.020000, param_2: 0.122000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1584")
