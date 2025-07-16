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
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.cx(qreg_2[1],qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_2[0])
subcirc1.rz(-0.070000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.214000, qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.rz(-0.097000, qreg_0[1])
subcirc2.s(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.s(qreg_2[0])
subcirc3.rz(0.292000, qreg_0[1])
subcirc3.cx(qreg_2[0],qreg_0[1])
subcirc3.rz(0.013000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cx(qreg_0[3],qreg_0[1])
subcirc4.s(qreg_0[0])
subcirc4.cx(qreg_0[0],qreg_0[3])
subcirc4.u(-0.290000,0.285000,0.247000, qreg_0[0])

main_circ = QuantumCircuit(2)
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

main_circ.cx(qreg_0[3],qreg_0[1])
main_circ.s(1)
main_circ.s(0)
main_circ.cx(qreg_0[3],qreg_0[2])
main_circ.s(0)
main_circ.rz(-0.383000, qreg_0[1])
main_circ.s(qreg_0[1])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_0[2],1])
main_circ.u(0.228000,param_1,0.596000, 1)
main_circ.append(subcirc4,[qreg_0[1],0,qreg_0[0],qreg_0[2]])
main_circ.append(subcirc4,[qreg_0[1],1,0,qreg_0[2]])
main_circ.append(subcirc2,[qreg_0[1],1,qreg_0[3],qreg_0[2]])
main_circ.append(subcirc3,[qreg_0[3],0,qreg_0[0],1])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc4,[qreg_0[1],0,1,qreg_0[3]])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.cx(0,qreg_0[1])
main_circ.cx(1,qreg_0[1])
main_circ.cx(qreg_0[1],qreg_0[3])
main_circ.cx(1,qreg_0[2])
main_circ.u(-0.947000,0.883000,param_0, 1)
main_circ.append(subcirc3,[qreg_0[1],0,qreg_0[0],qreg_0[2]])
main_circ.s(1)
main_circ.append(subcirc2,[1,qreg_0[1],0,qreg_0[0]])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.rz(param_0, 1)
main_circ.u(-0.774000,-0.423000,0.145000, qreg_0[0])
bindings = {param_0: 0.847000, param_1: -0.090000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1627")
