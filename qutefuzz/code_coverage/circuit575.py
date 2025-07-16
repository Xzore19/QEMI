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
subcirc0.rx(0.970000, qreg_0[0])
subcirc0.rx(0.920000, qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.rx(-0.791000, qreg_3[0])
subcirc0.ry(0.652000, qreg_0[2])
subcirc0.ry(-0.180000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.557000, qreg_0[1])
subcirc1.rx(-0.811000, qreg_0[3])
subcirc1.ry(0.495000, qreg_0[0])
subcirc1.ry(-0.597000, qreg_0[2])
subcirc1.rx(0.838000, qreg_0[1])
subcirc1.rx(-0.628000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.500000,0.565000,-0.388000, qreg_0[3])
subcirc2.u(0.902000,0.979000,0.946000, qreg_0[0])
subcirc2.u(0.065000,0.861000,0.594000, qreg_0[3])
subcirc2.rx(0.618000, qreg_0[3])
subcirc2.ry(-0.971000, qreg_0[2])
subcirc2.u(-0.213000,-0.444000,0.615000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.612000, qreg_0[2])
subcirc3.h(qreg_0[0])
subcirc3.u(0.238000,-0.708000,0.897000, qreg_0[1])
subcirc3.ry(-0.727000, qreg_0[0])
subcirc3.u(0.769000,0.874000,-0.534000, qreg_0[0])
subcirc3.h(qreg_3[0])

main_circ = QuantumCircuit(0)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc2,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.ry(param_4, qreg_0[0])
main_circ.rx(0.344000, qreg_0[0])
main_circ.rx(-0.845000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.rx(param_3, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc3,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.h(qreg_0[1])
main_circ.ry(param_2, qreg_0[2])
main_circ.u(param_3,param_2,-0.491000, qreg_0[1])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.rx(param_4, qreg_3[0])
main_circ.ry(0.896000, qreg_0[2])
main_circ.rx(0.677000, qreg_0[2])
main_circ.rx(param_1, qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.rx(param_0, qreg_3[0])
bindings = {param_0: 0.351000, param_1: 0.329000, param_2: 0.639000, param_3: 0.183000, param_4: -0.975000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
