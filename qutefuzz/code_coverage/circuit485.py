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
subcirc0.z(qreg_2[1])
subcirc0.rx(0.099000, qreg_0[1])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.u(0.299000,-0.030000,-0.108000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.x(qreg_0[0])
subcirc1.u(0.218000,0.815000,0.326000, qreg_0[1])
subcirc1.u(0.089000,-0.091000,-0.688000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0.477000,0.887000,0.184000, qreg_2[1])
subcirc2.u(0.095000,-0.731000,-0.017000, qreg_2[0])
subcirc2.u(-0.029000,-0.793000,-0.160000, qreg_1[0])
subcirc2.rx(0.282000, qreg_2[0])
subcirc2.rx(0.847000, qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rx(-0.619000, 0)
main_circ.append(subcirc2,[qreg_3[0],qreg_0[0],0,qreg_0[2]])
main_circ.x(qreg_0[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[2],0])
main_circ.rx(param_2, 0)
main_circ.u(-0.159000,param_0,0.152000, qreg_3[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0],0])
main_circ.z(qreg_3[0])
main_circ.rx(0.287000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0],0])
main_circ.u(param_1,param_2,0.374000, qreg_0[1])
main_circ.rx(param_0, 0)
main_circ.rx(-0.494000, 0)
main_circ.rx(param_2, 0)
main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],0,qreg_0[0]])
main_circ.z(0)
main_circ.append(subcirc2,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.u(-0.170000,-0.806000,param_2, qreg_0[2])
main_circ.u(param_0,param_1,-0.996000, qreg_0[1])
bindings = {param_0: -0.509000, param_1: -0.456000, param_2: -0.085000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
