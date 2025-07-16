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
subcirc0.rx(-0.489000, qreg_2[0])
subcirc0.z(qreg_2[1])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_0[1],qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1.z(qreg_0[0])
subcirc1.rx(-0.490000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

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

main_circ.z(1)
main_circ.cz(0,2)
main_circ.rx(0.829000, 0)
main_circ.rx(param_0, 2)
main_circ.cy(0,1)
main_circ.rx(param_0, 1)
main_circ.cz(0,1)
main_circ.cz(3,1)
main_circ.rx(-0.171000, 1)
main_circ.rx(-0.682000, 0)
main_circ.cy(3,2)
main_circ.cy(3,0)
main_circ.z(0)
main_circ.cz(2,3)
main_circ.rx(0.528000, 1)
main_circ.z(2)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.rx(param_1, 3)
main_circ.z(0)
main_circ.rx(-0.717000, 2)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.cz(0,3)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.z(3)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.cy(1,0)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.rx(-0.959000, 3)
main_circ.cy(1,2)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cy(2,1)
main_circ.cy(2,3)
bindings = {param_0: -0.044000, param_1: -0.863000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "708")
