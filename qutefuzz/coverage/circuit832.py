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
subcirc0.u(-0.697000,0.778000,-0.997000, qreg_0[0])
subcirc0.u(0.962000,0.459000,0.714000, qreg_1[0])
subcirc0.u(0.466000,0.838000,-0.364000, qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.739000,-0.877000,0.876000, qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.u(0.721000,0.133000,0.281000, qreg_0[0])
subcirc1.x(qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.u(0,0,-0.065000, qreg_0[2])
subcirc2.u(0,0,-0.112000, qreg_0[2])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.x(qreg_2[0])
subcirc3.u(0,0,-0.935000, qreg_3[0])
subcirc3.u(0,0,-0.030000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.099000,0.470000,-0.327000, qreg_0[0])
subcirc4.u(0,0,0.624000, qreg_0[0])
subcirc4.u(0.986000,0.260000,0.658000, qreg_0[1])
subcirc4.u(0,0,-0.316000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[1,2,qreg_0[0],0,3])
main_circ.u(param_3,param_1,param_2, 0)
main_circ.y(qreg_0[0])
main_circ.u(0,0,0.465000, qreg_0[0])
main_circ.append(subcirc0,[1,0,3,qreg_0[0],2])
main_circ.append(subcirc0,[2,1,qreg_0[0],3,0])
main_circ.x(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.u(0,0,0.229000, 3)
main_circ.append(subcirc1,[qreg_0[0],2,1,3,0])
main_circ.append(subcirc1,[qreg_0[0],0,2,1,3])
main_circ.u(param_1,param_5,param_4, 3)
main_circ.u(param_3,param_3,param_2, 2)
main_circ.u(0.287000,param_0,param_5, 1)
main_circ.u(param_3,param_5,param_3, 3)
main_circ.y(2)
main_circ.append(subcirc1,[1,qreg_0[0],2,3,0])
main_circ.u(param_3,-0.486000,param_2, 0)
main_circ.u(-0.960000,param_4,param_1, 0)
main_circ.append(subcirc0,[1,qreg_0[0],3,2,0])
main_circ.u(param_4,param_5,param_4, 2)
main_circ.u(-0.538000,0.064000,-0.807000, 2)
main_circ.x(0)
main_circ.append(subcirc1,[0,qreg_0[0],3,2,1])
main_circ.u(0,param_1,param_1, 2)
main_circ.u(0,param_5,param_5, qreg_0[0])
main_circ.append(subcirc1,[2,1,0,qreg_0[0],3])
main_circ.y(0)
main_circ.y(1)
bindings = {param_0: 0.616000, param_1: 0.305000, param_2: 0.296000, param_3: -0.488000, param_4: 0.480000, param_5: 0.870000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "832")
