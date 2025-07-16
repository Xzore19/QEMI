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
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.u(pi/2,-0.669000,-0.700000, qreg_0[0])
subcirc0.u(pi/2,-0.338000,-0.930000, qreg_2[1])
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.u(0.874000,-0.748000,-0.576000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.465000,0.827000,-0.779000, qreg_0[2])
subcirc1.y(qreg_0[2])
subcirc1.u(0.382000,-0.998000,-0.685000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.u(-0.660000,-0.092000,0.368000, qreg_0[0])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0.125000,0.494000,-0.469000, qreg_0[2])
subcirc3.u(pi/2,0.285000,0.750000, qreg_0[1])
subcirc3.y(qreg_0[2])
subcirc3.y(qreg_0[3])
subcirc3.u(0.388000,-0.327000,0.471000, qreg_0[3])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.y(qreg_3[0])
subcirc4.y(qreg_0[0])
subcirc4.u(0.431000,0.828000,-0.497000, qreg_0[1])
subcirc4.y(qreg_3[0])
subcirc4.cy(qreg_0[2],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(qreg_1[1])
main_circ.u(pi/2,-0.142000,-0.498000, qreg_1[2])
main_circ.u(-0.162000,-0.183000,0.152000, qreg_1[1])
main_circ.u(-0.508000,param_0,0.355000, qreg_1[2])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[1],qreg_1[2]])
main_circ.y(qreg_1[1])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.append(subcirc3,[qreg_1[2],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.y(qreg_1[2])
main_circ.u(param_2,param_1,-0.922000, qreg_1[2])
main_circ.u(pi/2,param_2,param_2, qreg_1[2])
main_circ.u(param_0,-0.233000,param_2, qreg_1[0])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.cy(qreg_1[0],qreg_1[2])
main_circ.cy(qreg_1[1],qreg_0[0])
main_circ.cy(qreg_1[2],qreg_1[1])
main_circ.cy(qreg_1[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_1[2],qreg_0[0]])
bindings = {param_0: 0.830000, param_1: 0.093000, param_2: -0.652000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "744")
