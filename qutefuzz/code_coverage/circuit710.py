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
subcirc0.u(-0.691000,0.253000,-0.034000, qreg_0[2])
subcirc0.rx(0.940000, qreg_0[0])
subcirc0.rx(-0.749000, qreg_0[3])
subcirc0.u(0.502000,-0.526000,0.705000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.163000, qreg_1[1])
subcirc1.u(0,0,-0.950000, qreg_1[1])
subcirc1.rx(0.419000, qreg_3[0])
subcirc1.u(0,0,-0.931000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.783000, qreg_0[3])
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2.rx(0.105000, qreg_0[1])
subcirc2.rx(0.972000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(-0.408000, qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_3[0])
subcirc3.u(-0.258000,-0.540000,0.927000, qreg_0[0])
subcirc3.cy(qreg_0[0],qreg_3[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rx(0.887000, qreg_2[0])
subcirc4.cy(qreg_3[0],qreg_0[0])
subcirc4.rx(0.077000, qreg_2[0])
subcirc4.u(0,0,-0.195000, qreg_0[0])

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

main_circ.u(param_0,param_0,param_0, 2)
main_circ.append(subcirc4,[2,1,3,0])
main_circ.rx(0.737000, 2)
main_circ.rx(param_1, 1)
main_circ.cy(2,1)
main_circ.u(-0.199000,-0.046000,0.212000, 1)
main_circ.u(param_1,param_0,0.951000, 2)
main_circ.rx(param_1, 0)
main_circ.u(0.868000,param_0,-0.541000, 2)
main_circ.u(0,0,0.859000, 0)
main_circ.append(subcirc2,[2,3,0,1])
main_circ.append(subcirc2,[3,1,2,0])
main_circ.append(subcirc2,[0,2,3,1])
main_circ.rx(param_1, 1)
main_circ.cy(2,1)
main_circ.append(subcirc4,[0,2,3,1])
main_circ.cy(3,0)
main_circ.cy(3,1)
main_circ.cy(0,1)
main_circ.cy(3,0)
main_circ.cy(2,3)
main_circ.append(subcirc4,[1,0,2,3])
main_circ.u(param_1,param_0,-0.792000, 2)
bindings = {param_0: 0.616000, param_1: -0.957000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "710")
