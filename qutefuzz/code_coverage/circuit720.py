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
subcirc0.y(qreg_0[3])
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.y(qreg_0[3])
subcirc0.rx(-0.345000, qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.ry(0.575000, qreg_0[0])
subcirc1.rx(-0.927000, qreg_0[0])
subcirc1.ry(0.427000, qreg_2[0])
subcirc1.cx(qreg_0[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.469000, qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[1])
subcirc2.ry(-0.329000, qreg_1[0])
subcirc2.cx(qreg_1[0],qreg_0[0])
subcirc2.cx(qreg_1[0],qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.y(qreg_1[0])
subcirc3.y(qreg_2[1])
subcirc3.y(qreg_2[0])
subcirc3.ry(-0.609000, qreg_2[0])
subcirc3.rx(-0.182000, qreg_2[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.ry(-0.306000, qreg_0[0])
subcirc4.ry(-0.861000, qreg_1[2])
subcirc4.y(qreg_1[2])
subcirc4.ry(-0.640000, qreg_1[2])
subcirc4.y(qreg_1[1])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.y(3)
main_circ.rx(-0.962000, 0)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.rx(param_3, 2)
main_circ.append(subcirc1,[1,2,3,0])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.append(subcirc2,[2,3,0,1])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.y(2)
main_circ.append(subcirc2,[1,0,2,3])
main_circ.ry(param_2, 2)
main_circ.cx(0,2)
main_circ.rx(-0.675000, 3)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.cx(3,0)
main_circ.cx(1,0)
main_circ.cx(0,2)
main_circ.cx(3,2)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.append(subcirc1,[3,0,2,1])
main_circ.rx(param_3, 3)
main_circ.y(2)
bindings = {param_2: 0.189000, param_3: -0.986000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "720")
