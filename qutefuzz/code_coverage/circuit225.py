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
subcirc0.x(qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.x(qreg_0[0])
subcirc0.u(pi/2,-0.239000,-0.108000, qreg_0[3])
subcirc0.rz(-0.765000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1.x(qreg_0[2])
subcirc1.rz(-0.313000, qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.u(pi/2,-0.682000,-0.312000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[2])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.rz(-0.968000, qreg_0[0])
subcirc2.u(pi/2,-0.832000,0.535000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.x(qreg_2[0])
subcirc3.cz(qreg_0[0],qreg_2[0])
subcirc3.u(pi/2,-0.691000,0.627000, qreg_0[0])
subcirc3.x(qreg_2[0])
subcirc3.rz(0.056000, qreg_2[0])

main_circ = QuantumCircuit(0)
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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_2[0],qreg_0[1]])
main_circ.rz(param_1, qreg_2[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],qreg_2[0],qreg_0[0]])
main_circ.rz(param_0, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
main_circ.append(subcirc3,[qreg_3[0],qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.x(qreg_3[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.u(pi/2,-0.438000,-0.459000, qreg_3[0])
main_circ.cz(qreg_2[0],qreg_3[0])
main_circ.x(qreg_0[0])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.cz(qreg_3[0],qreg_2[0])
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_2[0],qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.rz(param_2, qreg_3[0])
main_circ.u(param_0,param_2,param_2, qreg_0[1])
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.x(qreg_2[0])
bindings = {param_0: 0.159000, param_1: 0.453000, param_2: 0.068000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "225")
