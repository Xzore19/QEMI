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
subcirc0.u(pi/2,0.521000,-0.591000, qreg_0[0])
subcirc0.u(0.520000,-0.959000,0.231000, qreg_0[2])
subcirc0.u(pi/2,-0.652000,-0.004000, qreg_0[1])
subcirc0.u(-0.713000,-0.363000,-0.540000, qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.488000,-0.504000, qreg_3[0])
subcirc1.rx(-0.686000, qreg_0[2])
subcirc1.rx(-0.898000, qreg_0[2])
subcirc1.rx(-0.882000, qreg_0[2])
subcirc1.u(pi/2,0.235000,-0.317000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0.544000,-0.662000,-0.018000, qreg_2[1])
subcirc2.u(pi/2,-0.799000,-0.156000, qreg_1[0])
subcirc2.u(0.345000,0.932000,-0.082000, qreg_2[0])
subcirc2.cy(qreg_0[0],qreg_2[0])
subcirc2.u(-0.431000,-0.283000,-0.170000, qreg_2[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cy(qreg_3[0],qreg_0[1])
subcirc3.u(pi/2,0.158000,0.483000, qreg_0[0])
subcirc3.u(0.433000,0.404000,-0.794000, qreg_3[0])
subcirc3.rx(0.044000, qreg_3[0])
subcirc3.u(pi/2,-0.712000,-0.682000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_0[2],qreg_0[3])
main_circ.u(param_3,-0.847000,-0.445000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.rx(0.744000, qreg_0[1])
main_circ.rx(param_1, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
main_circ.u(param_3,param_1,0.357000, qreg_0[1])
main_circ.rx(param_1, qreg_0[2])
main_circ.rx(0.547000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.rx(-0.147000, qreg_0[3])
main_circ.u(-0.964000,-0.940000,param_0, qreg_0[2])
main_circ.u(-0.811000,-0.349000,-0.551000, qreg_0[3])
bindings = {param_0: -0.364000, param_1: -0.573000, param_3: 0.182000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "230")
