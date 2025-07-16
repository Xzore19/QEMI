from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(-0.267000,-0.319000,-0.379000, qreg_2[0])
subcirc0.u(0,0,-0.497000, qreg_0[0])
subcirc0.u(0,0,-0.790000, qreg_2[0])
subcirc0.u(0,0,-0.850000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.154000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.729000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0.657000,0.623000,0.728000, qreg_1[1])
subcirc2.u(0.224000,0.750000,-0.200000, qreg_1[1])
subcirc2.u(-0.276000,-0.304000,-0.960000, qreg_1[0])
subcirc2.u(0,0,0.686000, qreg_1[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.u(0.801000,-0.785000,0.395000, qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.u(0,0,0.260000, qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.u(-0.440000,0.418000,0.157000, qreg_0[1])
subcirc4.z(qreg_0[0])
subcirc4.z(qreg_2[0])
subcirc4.u(0,0,-0.904000, qreg_0[1])
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

main_circ.append(subcirc1,[1,0,2,3])
main_circ.u(-0.642000,-0.207000,param_3, 2)
main_circ.append(subcirc0,[1,3,0,2])
main_circ.append(subcirc3,[0,3,1,2])
main_circ.z(3)
main_circ.append(subcirc1,[2,3,0,1])
main_circ.u(0,param_3,0.492000, 0)
main_circ.u(param_2,0,param_3, 0)
main_circ.append(subcirc1,[0,1,2,3])
main_circ.append(subcirc3,[1,3,0,2])
main_circ.z(1)
main_circ.append(subcirc2,[1,3,0,2])
main_circ.x(3)
main_circ.x(0)
main_circ.append(subcirc1,[3,1,0,2])
main_circ.append(subcirc3,[3,1,2,0])
main_circ.x(2)
main_circ.append(subcirc2,[2,1,0,3])
bindings = {param_2: -0.428000, param_3: -0.233000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "153")
