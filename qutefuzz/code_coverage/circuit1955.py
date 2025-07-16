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
subcirc0.u(0,0,-0.872000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.u(0,0,0.126000, qreg_0[1])
subcirc0.rz(0.430000, qreg_3[0])
subcirc0.u(0,0,-0.284000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_0[1])
subcirc1.rz(-0.409000, qreg_2[0])
subcirc1.rz(0.214000, qreg_2[0])
subcirc1.u(0,0,-0.970000, qreg_0[1])
subcirc1.rz(0.273000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(-0.258000,-0.908000,-0.565000, qreg_2[1])
subcirc2.x(qreg_0[1])
subcirc2.rz(0.848000, qreg_0[0])
subcirc2.x(qreg_0[1])
subcirc2.u(0,0,0.886000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.u(0.599000,0.340000,-0.109000, qreg_0[3])
subcirc3.u(-0.307000,0.094000,-0.324000, qreg_0[3])
subcirc3.u(0,0,0.662000, qreg_0[2])
subcirc3.u(-0.181000,-0.096000,0.753000, qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.x(qreg_0[2])
subcirc4.x(qreg_0[3])
subcirc4.u(0,0,0.674000, qreg_0[1])
subcirc4.x(qreg_0[1])
subcirc4.u(0.620000,0.117000,-0.897000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc3,[0,3,2,qreg_0[0]])
main_circ.rz(0.315000, qreg_0[0])
main_circ.u(0.240000,param_0,0.158000, qreg_0[0])
main_circ.u(0.580000,param_0,param_1, qreg_0[0])
main_circ.rz(-0.023000, qreg_0[0])
main_circ.append(subcirc4,[qreg_0[0],2,1,0])
main_circ.u(0.366000,0.155000,-0.276000, 1)
main_circ.u(0.180000,param_2,-0.224000, 2)
main_circ.append(subcirc4,[1,qreg_0[0],2,0])
main_circ.append(subcirc4,[qreg_0[0],3,1,0])
main_circ.append(subcirc4,[1,0,2,3])
main_circ.append(subcirc0,[3,0,1,qreg_0[0]])
main_circ.u(0,0,0.280000, 0)
main_circ.x(2)
main_circ.x(3)
main_circ.append(subcirc3,[3,qreg_0[0],1,0])
main_circ.u(param_2,-0.655000,param_0, 1)
main_circ.u(param_2,param_1,-0.343000, 3)
main_circ.u(param_0,param_2,param_2, 1)
main_circ.u(0,0,param_2, qreg_0[0])
bindings = {param_0: 0.284000, param_1: 0.726000, param_2: 0.949000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1955")
