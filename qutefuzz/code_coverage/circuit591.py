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
subcirc0.u(pi/2,0.904000,0.504000, qreg_2[0])
subcirc0.rz(-0.900000, qreg_2[1])
subcirc0.rz(-0.978000, qreg_0[1])
subcirc0.u(pi/2,0.960000,0.656000, qreg_2[0])
subcirc0.u(pi/2,0.275000,0.936000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.650000,0.773000, qreg_2[0])
subcirc1.rz(-0.127000, qreg_3[0])
subcirc1.z(qreg_2[0])
subcirc1.z(qreg_0[1])
subcirc1.rz(0.260000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,0.896000,0.372000, qreg_0[0])
subcirc2.u(pi/2,-0.688000,0.069000, qreg_1[0])
subcirc2.u(0,0,-0.801000, qreg_2[0])
subcirc2.u(0,0,-0.749000, qreg_0[0])
subcirc2.rz(0.418000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.u(0,0,0.281000, qreg_1[2])
subcirc3.z(qreg_1[1])
subcirc3.u(0,0,-0.142000, qreg_1[2])
subcirc3.z(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rz(-0.663000, qreg_0[0])
subcirc4.u(pi/2,0.963000,-0.515000, qreg_0[0])
subcirc4.u(pi/2,0.284000,0.745000, qreg_0[0])
subcirc4.rz(-0.035000, qreg_0[3])
subcirc4.u(0,0,-0.919000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rz(param_0, 2)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.append(subcirc2,[0,1,3,2])
main_circ.u(0,param_0,-0.433000, 2)
main_circ.append(subcirc0,[3,2,1,0])
main_circ.rz(0.055000, 2)
main_circ.u(param_0,-0.648000,param_1, 3)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.append(subcirc0,[2,1,0,3])
main_circ.z(3)
main_circ.rz(param_1, 0)
main_circ.u(pi/2,-0.989000,param_0, 0)
main_circ.rz(0.360000, 2)
main_circ.z(0)
main_circ.z(1)
main_circ.rz(0.382000, 0)
main_circ.z(2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.u(0,0,param_1, 3)
main_circ.u(param_1,0,param_1, 2)
main_circ.u(0,0,param_1, 1)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.rz(-0.362000, 3)
main_circ.z(1)
main_circ.u(param_1,param_0,0.192000, 3)
main_circ.append(subcirc2,[3,2,0,1])
bindings = {param_0: 0.267000, param_1: 0.694000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "591")
