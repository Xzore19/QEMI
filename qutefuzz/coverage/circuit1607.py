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
subcirc0.u(0,0,-0.948000, qreg_0[1])
subcirc0.u(0,0,-0.121000, qreg_0[3])
subcirc0.u(0,0,-0.492000, qreg_0[3])
subcirc0.u(pi/2,-0.891000,0.889000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.u(pi/2,0.218000,0.648000, qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],0,qreg_0[1],qreg_0[0]])
main_circ.h(0)
main_circ.u(pi/2,-0.877000,param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],0])
main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[2],qreg_3[0]])
main_circ.u(pi/2,-0.701000,0.627000, 0)
main_circ.u(0,param_0,0.194000, qreg_3[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],0,qreg_3[0],qreg_0[1]])
main_circ.u(pi/2,-0.919000,0.113000, qreg_0[2])
main_circ.h(qreg_0[2])
main_circ.rx(param_0, 0)
main_circ.rx(-0.870000, qreg_0[0])
main_circ.u(pi/2,0.537000,0.005000, 0)
main_circ.u(0,param_0,param_0, qreg_0[2])
main_circ.u(0,param_0,param_0, qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.u(0,param_0,0.288000, qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.u(0,param_0,param_0, 0)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.u(0,param_0,param_0, qreg_3[0])
main_circ.h(qreg_0[1])
main_circ.h(0)
main_circ.u(param_0,0,param_0, qreg_0[2])
main_circ.u(pi/2,param_0,param_0, 0)
main_circ.h(qreg_0[1])
main_circ.rx(param_0, qreg_3[0])
main_circ.rx(0.116000, 0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[2],0,qreg_0[0]])
main_circ.u(param_0,-0.445000,-0.630000, 0)
main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.h(qreg_0[1])
main_circ.h(0)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.u(param_0,-0.661000,param_0, qreg_0[2])
main_circ.rx(param_0, qreg_0[0])
main_circ.u(0,0,0.944000, qreg_0[2])
bindings = {param_0: -0.631000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
