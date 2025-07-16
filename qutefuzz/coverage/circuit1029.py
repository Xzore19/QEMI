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
subcirc0.cz(qreg_3[0],qreg_1[1])
subcirc0.x(qreg_1[1])
subcirc0.u(pi/2,-0.126000,0.311000, qreg_0[0])
subcirc0.z(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.890000,-0.648000, qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[0])
subcirc1.z(qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.658000,0.636000, qreg_3[0])
subcirc2.u(pi/2,-0.742000,-0.047000, qreg_0[2])
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.u(pi/2,-0.759000,0.498000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.u(pi/2,-0.765000,0.592000, qreg_0[1])
subcirc3.x(qreg_3[0])
subcirc3.cz(qreg_0[0],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_1[1],qreg_3[0])
subcirc4.z(qreg_1[0])
subcirc4.cz(qreg_1[0],qreg_0[0])
subcirc4.u(pi/2,-0.499000,-0.688000, qreg_1[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],0,qreg_0[1]])
main_circ.z(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[3],0,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.u(param_0,-0.390000,param_1, qreg_0[3])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[2],0])
main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],0,qreg_0[1],qreg_0[2]])
main_circ.x(0)
main_circ.u(pi/2,0.782000,-0.123000, qreg_0[2])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.cz(qreg_0[2],0)
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.z(0)
main_circ.u(param_0,-0.027000,0.816000, 0)
main_circ.x(qreg_0[2])
main_circ.z(qreg_0[1])
bindings = {param_0: -0.329000, param_1: 0.683000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1029")
