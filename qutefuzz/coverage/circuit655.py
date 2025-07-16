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
subcirc0.h(qreg_0[2])
subcirc0.rx(0.214000, qreg_0[0])
subcirc0.u(0,0,-0.254000, qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1.cy(qreg_0[2],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[1])
subcirc2.h(qreg_0[1])
subcirc2.rx(-0.042000, qreg_0[0])
subcirc2.h(qreg_2[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_0[2])
subcirc3.u(0,0,-0.113000, qreg_0[2])
subcirc3.rx(0.251000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0,0,0.665000, qreg_0[1])
subcirc4.h(qreg_0[3])
subcirc4.rx(-0.498000, qreg_0[1])
subcirc4.cy(qreg_0[1],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rx(-0.404000, qreg_1[0])
main_circ.append(subcirc3,[0,qreg_3[0],qreg_1[0],qreg_1[1]])
main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],0,qreg_1[1]])
main_circ.h(0)
main_circ.u(param_0,param_1,-0.751000, qreg_0[0])
main_circ.u(0,0,param_0, qreg_1[1])
main_circ.append(subcirc4,[0,qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.h(qreg_1[1])
main_circ.h(0)
main_circ.cy(qreg_3[0],qreg_1[1])
main_circ.u(param_1,param_0,-0.684000, qreg_3[0])
main_circ.u(param_0,0,param_0, qreg_1[0])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.u(param_0,0,param_0, 0)
main_circ.append(subcirc2,[0,qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.cy(qreg_0[0],0)
main_circ.append(subcirc4,[qreg_3[0],0,qreg_1[1],qreg_0[0]])
main_circ.rx(param_0, qreg_3[0])
main_circ.rx(-0.283000, qreg_1[1])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_1[1],qreg_1[0]])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.cy(qreg_1[1],qreg_3[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(0,qreg_1[1])
main_circ.cy(qreg_1[1],qreg_1[0])
main_circ.cy(0,qreg_3[0])
main_circ.cy(qreg_1[0],qreg_1[1])
main_circ.cy(qreg_0[0],0)
main_circ.append(subcirc4,[qreg_1[1],qreg_3[0],0,qreg_1[0]])
main_circ.rx(-0.835000, qreg_1[0])
main_circ.cy(qreg_1[1],qreg_0[0])
bindings = {param_0: -0.168000, param_1: -0.351000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "655")
