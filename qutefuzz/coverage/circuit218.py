from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(-0.772000,-0.426000,-0.773000, qreg_0[0])
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_1[1])
subcirc0.u(0.849000,-0.690000,-0.730000, qreg_0[0])
subcirc0.rx(-0.554000, qreg_0[0])
subcirc0.rx(-0.057000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_1[0])
subcirc1.rx(-0.663000, qreg_2[0])
subcirc1.u(-0.274000,-0.086000,-0.675000, qreg_1[0])
subcirc1.u(-0.663000,-0.737000,0.808000, qreg_1[0])
subcirc1.u(pi/2,0.800000,-0.049000, qreg_2[0])
subcirc1.u(pi/2,-0.235000,-0.776000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,0.569000,0.890000, qreg_0[1])
subcirc2.rx(0.385000, qreg_0[1])
subcirc2.u(-0.573000,0.818000,-0.672000, qreg_0[2])
subcirc2.rx(-0.240000, qreg_0[3])
subcirc2.u(pi/2,-0.631000,0.507000, qreg_0[0])
subcirc2.u(0.701000,-0.554000,0.289000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(0.461000,0.406000,-0.373000, qreg_1[0])
subcirc3.u(-0.834000,0.330000,0.280000, qreg_1[0])
subcirc3.rx(0.330000, qreg_1[0])
subcirc3.rx(-0.461000, qreg_1[1])
subcirc3.u(pi/2,-0.593000,0.769000, qreg_1[2])
subcirc3.u(0.219000,0.544000,0.638000, qreg_1[1])

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

main_circ.u(param_0,param_2,0.147000, 2)
main_circ.h(3)
main_circ.rx(param_0, 0)
main_circ.rx(param_2, 1)
main_circ.append(subcirc1,[qreg_0[0],0,3,1])
main_circ.rx(param_1, qreg_0[0])
main_circ.u(param_2,-0.044000,0.389000, qreg_0[0])
main_circ.h(1)
main_circ.h(1)
main_circ.h(0)
main_circ.rx(param_0, 2)
main_circ.append(subcirc1,[1,qreg_0[0],0,2])
main_circ.u(param_0,0.047000,param_0, qreg_0[0])
main_circ.append(subcirc1,[2,qreg_0[0],3,1])
main_circ.h(3)
main_circ.u(param_1,0.820000,param_2, 2)
main_circ.u(param_2,param_2,param_2, 2)
main_circ.u(param_0,0.007000,param_1, 3)
main_circ.rx(0.158000, 0)
main_circ.u(0.945000,param_2,0.267000, 0)
main_circ.rx(-0.601000, qreg_0[0])
main_circ.u(pi/2,0.907000,param_0, qreg_0[0])
main_circ.u(param_1,-0.850000,0.576000, 3)
main_circ.append(subcirc3,[qreg_0[0],3,2,0])
main_circ.u(pi/2,0.456000,param_1, 1)
main_circ.rx(-0.855000, 2)
main_circ.append(subcirc3,[3,qreg_0[0],0,1])
bindings = {param_0: -0.164000, param_1: 0.569000, param_2: 0.982000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
