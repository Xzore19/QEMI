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
subcirc0.u(0.067000,-0.841000,-0.428000, qreg_0[3])
subcirc0.rx(-0.133000, qreg_0[0])
subcirc0.rx(0.498000, qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.cx(qreg_0[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_3[0])
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.227000, qreg_0[2])
subcirc2.rx(-0.679000, qreg_0[0])
subcirc2.h(qreg_0[2])
subcirc2.rx(-0.267000, qreg_0[1])
subcirc2.u(0.225000,-0.467000,0.457000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(-0.924000,-0.853000,param_2, 3)
main_circ.h(0)
main_circ.append(subcirc2,[0,1,qreg_0[0],3])
main_circ.append(subcirc0,[0,2,1,qreg_0[1]])
main_circ.cx(qreg_0[0],2)
main_circ.h(3)
main_circ.append(subcirc0,[2,0,qreg_0[1],1])
main_circ.rx(param_3, qreg_0[0])
main_circ.h(2)
main_circ.h(2)
main_circ.rx(-0.556000, qreg_0[0])
main_circ.u(param_2,param_4,-0.710000, 0)
main_circ.rx(-0.231000, qreg_0[0])
main_circ.rx(-0.406000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],2,3,qreg_0[0]])
main_circ.cx(2,qreg_0[1])
main_circ.cx(1,3)
main_circ.u(param_2,param_2,param_4, 0)
main_circ.append(subcirc2,[2,0,qreg_0[0],1])
main_circ.cx(qreg_0[0],1)
main_circ.cx(1,qreg_0[0])
main_circ.cx(2,1)
main_circ.cx(2,1)
main_circ.cx(qreg_0[1],0)
main_circ.u(0.171000,param_3,param_4, qreg_0[0])
main_circ.cx(1,0)
main_circ.h(0)
main_circ.cx(2,qreg_0[0])
main_circ.h(qreg_0[1])
bindings = {param_2: 0.496000, param_3: -0.010000, param_4: -0.274000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "415")
