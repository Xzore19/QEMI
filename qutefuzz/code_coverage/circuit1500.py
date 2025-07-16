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
subcirc0.u(0,0,-0.718000, qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0.ry(-0.672000, qreg_0[0])
subcirc0.x(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.405000, qreg_0[1])
subcirc1.x(qreg_0[2])
subcirc1.u(0,0,-0.280000, qreg_0[1])
subcirc1.u(0,0,-0.571000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.427000, qreg_0[1])
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.u(0,0,0.889000, qreg_0[2])
subcirc2.u(0,0,0.029000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[2],qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.u(0,0,-0.684000, qreg_0[2])
subcirc3.x(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.271000, qreg_0[0])
subcirc4.cy(qreg_0[0],qreg_2[0])
subcirc4.u(0,0,-0.874000, qreg_2[0])
subcirc4.x(qreg_2[0])

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

main_circ.x(2)
main_circ.append(subcirc4,[3,1,2,0])
main_circ.x(2)
main_circ.append(subcirc1,[0,1,2,3])
main_circ.x(3)
main_circ.cy(0,1)
main_circ.cy(3,1)
main_circ.append(subcirc1,[2,1,3,0])
main_circ.cy(3,2)
main_circ.cy(2,3)
main_circ.append(subcirc4,[3,2,0,1])
main_circ.append(subcirc4,[0,3,1,2])
main_circ.append(subcirc1,[1,2,0,3])
main_circ.append(subcirc4,[2,3,0,1])
main_circ.cy(1,0)
main_circ.cy(0,3)
main_circ.cy(3,0)
main_circ.cy(3,1)
main_circ.cy(0,1)
main_circ.cy(0,2)
main_circ.cy(0,2)
main_circ.x(3)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.u(0,param_1,-0.323000, 1)
main_circ.x(0)
main_circ.ry(0.018000, 0)
bindings = {param_1: 0.383000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1500")
