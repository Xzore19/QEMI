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
subcirc0.u(0.517000,-0.271000,-0.571000, qreg_3[0])
subcirc0.u(-0.060000,0.372000,0.365000, qreg_3[0])
subcirc0.u(-0.304000,0.814000,0.684000, qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.u(-0.734000,-0.713000,-0.640000, qreg_0[1])
subcirc0.h(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.u(0.268000,0.304000,-0.493000, qreg_0[2])
subcirc1.u(-0.626000,0.381000,-0.331000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_0[3])
subcirc2.u(0.511000,0.900000,0.962000, qreg_0[1])
subcirc2.u(pi/2,-0.063000,0.327000, qreg_0[3])
subcirc2.h(qreg_0[3])
subcirc2.u(0.531000,-0.830000,0.284000, qreg_0[1])
subcirc2.u(pi/2,-0.940000,0.492000, qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cz(qreg_0[1],qreg_2[1])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_2[1])
subcirc3.u(-0.715000,-0.146000,0.891000, qreg_0[1])
subcirc3.h(qreg_2[1])
subcirc3.cz(qreg_0[0],qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.h(qreg_3[0])
subcirc4.u(-0.995000,0.795000,0.695000, qreg_0[0])
subcirc4.h(qreg_3[0])
subcirc4.u(0.841000,-0.220000,-0.063000, qreg_0[2])
subcirc4.cz(qreg_0[0],qreg_3[0])
subcirc4.h(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cz(1,qreg_2[1])
main_circ.append(subcirc1,[0,1,qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.h(qreg_0[1])
main_circ.h(0)
main_circ.u(param_0,param_0,-0.410000, 1)
main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],1,qreg_2[1],qreg_0[0],0])
main_circ.h(qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.append(subcirc0,[1,qreg_0[0],0,qreg_2[1]])
main_circ.u(param_2,-0.987000,param_0, qreg_2[1])
main_circ.h(qreg_2[0])
main_circ.append(subcirc0,[1,qreg_2[0],0,qreg_0[1]])
main_circ.u(pi/2,param_2,param_0, qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.cz(0,qreg_2[0])
main_circ.cz(qreg_2[1],qreg_2[0])
main_circ.cz(0,qreg_0[0])
main_circ.cz(0,qreg_2[0])
main_circ.cz(qreg_2[1],0)
main_circ.cz(qreg_2[0],0)
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.h(qreg_2[1])
main_circ.u(param_0,param_1,param_0, qreg_2[1])
main_circ.u(param_0,param_0,0.275000, 1)
main_circ.h(qreg_0[0])
main_circ.h(0)
main_circ.h(0)
bindings = {param_0: 0.674000, param_1: -0.645000, param_2: -0.662000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
