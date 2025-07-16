from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_1[1],qreg_0[0])
subcirc0.cy(qreg_1[0],qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(0.116000, qreg_0[0])
subcirc1.rx(-0.934000, qreg_0[0])
subcirc1.u(pi/2,0.717000,0.643000, qreg_1[0])
subcirc1.rx(-0.337000, qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.360000, qreg_0[1])
subcirc2.rx(0.168000, qreg_3[0])
subcirc2.x(qreg_0[0])
subcirc2.u(pi/2,0.016000,0.687000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rx(param_1, 1)
main_circ.append(subcirc2,[2,0,3,1])
main_circ.x(0)
main_circ.rx(param_0, 2)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.x(1)
main_circ.rx(0.645000, 3)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.cy(0,1)
main_circ.cy(1,2)
main_circ.cy(0,3)
main_circ.u(param_0,-0.805000,-0.208000, 3)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.x(3)
main_circ.rx(param_1, 2)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.cy(2,0)
main_circ.rx(-0.057000, 0)
main_circ.x(2)
main_circ.cy(0,1)
main_circ.cy(3,2)
main_circ.cy(3,2)
main_circ.cy(1,3)
main_circ.cy(1,0)
main_circ.cy(3,1)
main_circ.cy(3,2)
main_circ.cy(3,0)
main_circ.cy(3,2)
main_circ.cy(1,0)
main_circ.cy(0,3)
main_circ.append(subcirc1,[3,1,0,2])
bindings = {param_0: 0.777000, param_1: 0.177000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "275")
