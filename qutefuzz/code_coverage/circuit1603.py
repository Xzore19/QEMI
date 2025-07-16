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
subcirc0.y(qreg_0[2])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_1[0])
subcirc2.h(qreg_0[0])
subcirc2.cy(qreg_1[1],qreg_0[0])
subcirc2.cy(qreg_1[2],qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_3[0])
subcirc3.cy(qreg_3[0],qreg_0[0])
subcirc3.cy(qreg_3[0],qreg_0[0])
subcirc3.x(qreg_3[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(qreg_3[0])
main_circ.h(qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.cy(qreg_2[0],qreg_3[0])
main_circ.x(qreg_2[0])
main_circ.h(qreg_3[0])
main_circ.y(0)
main_circ.x(qreg_3[0])
main_circ.x(qreg_3[0])
main_circ.cy(qreg_0[0],0)
main_circ.y(qreg_2[0])
main_circ.cy(0,qreg_2[0])
main_circ.x(qreg_0[1])
main_circ.cy(0,qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.h(0)
main_circ.h(0)
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.y(qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.x(qreg_2[0])
main_circ.x(qreg_0[0])
main_circ.x(qreg_3[0])
main_circ.h(qreg_2[0])
main_circ.y(qreg_0[1])
main_circ.cy(qreg_2[0],qreg_3[0])
main_circ.cy(qreg_3[0],qreg_2[0])
main_circ.cy(0,qreg_2[0])
main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.cy(qreg_2[0],0)
main_circ.y(qreg_3[0])
main_circ.cy(qreg_3[0],qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.x(qreg_0[1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1603")
