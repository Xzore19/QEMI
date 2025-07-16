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
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_2[0])
subcirc0.ry(0.644000, qreg_2[0])
subcirc0.rx(-0.863000, qreg_2[0])
subcirc0.rx(-0.155000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.771000, qreg_0[3])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.ry(-0.320000, qreg_0[0])
subcirc1.ry(0.410000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.ry(-0.815000, qreg_1[1])
subcirc2.rx(0.374000, qreg_1[2])
subcirc2.cx(qreg_1[2],qreg_1[1])
subcirc2.rx(-0.409000, qreg_1[1])
subcirc2.rx(-0.012000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.916000, qreg_0[1])
subcirc3.u(0,0,0.159000, qreg_0[1])
subcirc3.u(0,0,0.601000, qreg_2[0])
subcirc3.u(0,0,0.588000, qreg_0[0])
subcirc3.cx(qreg_0[0],qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(-0.193000, qreg_3[0])
subcirc4.ry(0.347000, qreg_3[0])
subcirc4.rx(-0.716000, qreg_0[2])
subcirc4.ry(-0.068000, qreg_3[0])
subcirc4.cx(qreg_0[2],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_0,param_2,param_0, qreg_0[0])
main_circ.append(subcirc1,[0,2,1,3])
main_circ.cx(qreg_0[0],2)
main_circ.append(subcirc4,[0,qreg_0[0],2,1])
main_circ.append(subcirc2,[1,qreg_0[0],2,3,0])
main_circ.ry(-0.039000, 2)
main_circ.append(subcirc2,[1,0,qreg_0[0],3,2])
main_circ.ry(-0.177000, 3)
main_circ.append(subcirc4,[1,qreg_0[0],3,0])
main_circ.append(subcirc2,[qreg_0[0],3,1,0,2])
main_circ.cx(1,qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(1,qreg_0[0])
main_circ.cx(1,0)
main_circ.append(subcirc3,[qreg_0[0],0,1,3])
bindings = {param_0: -0.555000, param_2: 0.649000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1413")
