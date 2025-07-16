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
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.u(pi/2,-0.872000,-0.248000, qreg_0[0])
subcirc0.u(pi/2,-0.556000,-0.074000, qreg_0[1])
subcirc0.rx(-0.679000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.rx(-0.422000, qreg_0[1])
subcirc1.u(pi/2,-0.330000,0.256000, qreg_0[2])
subcirc1.rx(-0.391000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cy(qreg_1[1],qreg_0[0])
subcirc2.rz(0.374000, qreg_0[0])
subcirc2.rx(-0.555000, qreg_1[0])
subcirc2.rx(-0.762000, qreg_1[2])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.cy(qreg_1[2],qreg_1[1])
subcirc3.cy(qreg_1[1],qreg_1[2])
subcirc3.rx(0.012000, qreg_1[0])
subcirc3.u(pi/2,0.602000,-0.151000, qreg_1[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(pi/2,0.135000,0.284000, qreg_0[0])
subcirc4.rz(-0.241000, qreg_0[0])
subcirc4.rx(0.679000, qreg_0[1])
subcirc4.u(pi/2,-0.244000,0.578000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_3[0]])
main_circ.rx(-0.476000, qreg_2[0])
main_circ.rz(-0.213000, qreg_2[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],qreg_2[0],qreg_0[0]])
main_circ.u(param_1,param_1,0.241000, qreg_3[0])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.u(param_2,param_3,param_1, qreg_3[0])
main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.cy(qreg_0[1],qreg_2[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.rz(param_2, qreg_2[0])
main_circ.rx(-0.281000, qreg_0[1])
main_circ.u(param_3,param_1,param_1, qreg_0[0])
main_circ.rz(-0.912000, qreg_0[1])
main_circ.rx(-0.040000, qreg_2[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_2[0]])
main_circ.rx(0.609000, qreg_2[0])
bindings = {param_1: -0.408000, param_2: 0.077000, param_3: 0.106000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "692")
