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
subcirc0.h(qreg_3[0])
subcirc0.cy(qreg_1[1],qreg_1[0])
subcirc0.u(0.192000,0.248000,0.470000, qreg_1[1])
subcirc0.rx(-0.947000, qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.u(0.527000,0.189000,0.390000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.249000, qreg_1[0])
subcirc1.u(-0.895000,0.579000,0.422000, qreg_3[0])
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.h(qreg_1[1])
subcirc1.rx(0.959000, qreg_1[1])
subcirc1.u(-0.279000,0.418000,-0.359000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.598000,-0.473000,0.933000, qreg_0[0])
subcirc2.cy(qreg_0[3],qreg_0[0])
subcirc2.u(0.118000,0.085000,-0.086000, qreg_0[3])
subcirc2.rx(0.627000, qreg_0[2])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.rx(-0.180000, qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(-0.914000,-0.648000,0.930000, qreg_0[2])
subcirc3.u(0.859000,-0.056000,-0.784000, qreg_0[1])
subcirc3.u(-0.253000,-0.820000,-0.367000, qreg_0[1])
subcirc3.u(0.664000,-0.899000,0.228000, qreg_0[3])
subcirc3.h(qreg_0[2])
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc2,[qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
main_circ.rx(-0.858000, qreg_1[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.rx(0.482000, qreg_1[1])
main_circ.cy(qreg_1[1],qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[1])
main_circ.append(subcirc2,[qreg_1[1],qreg_0[0],qreg_1[2],qreg_1[0]])
main_circ.u(0.003000,-0.617000,param_1, qreg_1[2])
main_circ.u(param_2,param_2,-0.959000, qreg_1[0])
main_circ.rx(-0.197000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[1],qreg_1[2],qreg_1[0]])
main_circ.h(qreg_0[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.cy(qreg_1[2],qreg_1[1])
main_circ.rx(0.785000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.rx(param_3, qreg_1[0])
main_circ.u(-0.487000,param_4,param_3, qreg_0[0])
main_circ.cy(qreg_1[2],qreg_1[1])
bindings = {param_1: 0.934000, param_2: -0.482000, param_3: -0.089000, param_4: 0.971000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
