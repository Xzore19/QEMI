from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(-0.500000,-0.164000,-0.100000, qreg_0[0])
subcirc0.u(-0.560000,-0.053000,-0.793000, qreg_3[0])
subcirc0.cz(qreg_3[0],qreg_2[0])
subcirc0.u(0.785000,0.376000,-0.381000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0.033000,0.962000,-0.001000, qreg_0[0])
subcirc1.cy(qreg_1[2],qreg_0[0])
subcirc1.ry(0.665000, qreg_1[0])
subcirc1.cz(qreg_1[2],qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_3[0])
subcirc2.cz(qreg_2[0],qreg_0[1])
subcirc2.cy(qreg_3[0],qreg_2[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.816000,0.779000,-0.587000, qreg_0[1])
subcirc3.ry(0.341000, qreg_3[0])
subcirc3.u(0.004000,-0.433000,0.755000, qreg_3[0])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(-0.701000, qreg_3[0])
subcirc4.cz(qreg_0[0],qreg_1[0])
subcirc4.ry(0.887000, qreg_2[0])
subcirc4.cz(qreg_2[0],qreg_1[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[1,2,0,3,qreg_0[1]])
main_circ.cy(qreg_0[1],3)
main_circ.append(subcirc2,[1,3,2,qreg_0[1],0])
main_circ.append(subcirc3,[1,qreg_0[1],2,qreg_0[0],0])
main_circ.cy(qreg_0[1],2)
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],1,3,2])
main_circ.cz(2,0)
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,1,2])
main_circ.u(-0.688000,0.039000,0.488000, qreg_0[1])
main_circ.ry(param_2, 0)
main_circ.cy(qreg_0[1],2)
main_circ.cy(qreg_0[0],2)
main_circ.cz(2,qreg_0[1])
main_circ.append(subcirc4,[qreg_0[0],1,qreg_0[1],2,0,3])
main_circ.append(subcirc4,[0,2,qreg_0[1],qreg_0[0],1,3])
main_circ.append(subcirc3,[0,2,1,qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_0[0],1)
main_circ.append(subcirc1,[qreg_0[0],2,3,qreg_0[1]])
main_circ.cz(1,3)
bindings = {param_2: 0.507000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1443")
