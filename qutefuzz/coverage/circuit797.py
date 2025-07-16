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
subcirc0.z(qreg_0[1])
subcirc0.rx(0.472000, qreg_2[1])
subcirc0.ry(-0.720000, qreg_0[1])
subcirc0.ry(0.526000, qreg_2[0])
subcirc0.ry(-0.708000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.866000, qreg_0[3])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.rx(0.141000, qreg_0[0])
subcirc1.rx(-0.678000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(-0.767000, qreg_0[0])
subcirc2.rx(0.513000, qreg_0[2])
subcirc2.ry(0.122000, qreg_0[1])
subcirc2.ry(-0.961000, qreg_0[0])
subcirc2.x(qreg_0[3])

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
subcirc3.ry(0.857000, qreg_0[1])
subcirc3.z(qreg_0[1])
subcirc3.z(qreg_2[0])
subcirc3.rx(0.620000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc0,[3,1,2,0])
main_circ.append(subcirc0,[1,2,3,0])
main_circ.append(subcirc3,[0,3,1,2])
main_circ.x(0)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.ry(param_6, 3)
main_circ.rx(param_0, 2)
main_circ.z(1)
main_circ.ry(param_2, 3)
main_circ.x(0)
main_circ.append(subcirc3,[1,0,3,2])
main_circ.append(subcirc3,[0,2,3,1])
main_circ.append(subcirc0,[0,3,2,1])
main_circ.append(subcirc3,[2,1,3,0])
main_circ.rx(-0.244000, 0)
main_circ.z(0)
main_circ.append(subcirc2,[0,3,1,2])
main_circ.rx(param_3, 3)
main_circ.rx(param_4, 2)
bindings = {param_0: 0.122000, param_2: -0.301000, param_3: -0.998000, param_4: 0.493000, param_6: 0.474000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
