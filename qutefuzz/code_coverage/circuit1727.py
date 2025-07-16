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
subcirc0.u(-0.364000,0.294000,0.582000, qreg_0[1])
subcirc0.u(pi/2,-0.283000,0.811000, qreg_0[1])
subcirc0.u(pi/2,0.987000,0.816000, qreg_0[0])
subcirc0.u(pi/2,-0.038000,0.946000, qreg_0[0])
subcirc0.u(0,0,-0.726000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.414000,-0.022000, qreg_0[2])
subcirc1.u(pi/2,0.748000,0.796000, qreg_3[0])
subcirc1.u(pi/2,-0.461000,0.147000, qreg_0[2])
subcirc1.u(pi/2,-0.901000,0.309000, qreg_0[2])
subcirc1.u(pi/2,0.383000,0.291000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.166000, qreg_0[0])
subcirc2.u(pi/2,-0.188000,0.203000, qreg_0[1])
subcirc2.u(-0.048000,0.369000,0.002000, qreg_0[1])
subcirc2.u(pi/2,0.093000,0.837000, qreg_0[0])
subcirc2.ry(-0.091000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.u(param_0,param_0,-0.875000, qreg_0[0])
main_circ.u(param_1,param_0,param_1, 2)
main_circ.ry(-0.186000, 2)
main_circ.u(pi/2,param_1,param_0, 0)
main_circ.u(param_1,-0.608000,param_1, qreg_0[1])
main_circ.append(subcirc1,[2,0,qreg_0[1],1])
main_circ.append(subcirc2,[1,qreg_0[0],3,0,qreg_0[1]])
main_circ.u(param_1,0.741000,param_1, 2)
main_circ.append(subcirc1,[1,0,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],2,1,0])
main_circ.append(subcirc0,[qreg_0[1],3,1,2])
main_circ.u(0,0,param_1, qreg_0[1])
main_circ.ry(param_0, 3)
main_circ.ry(param_1, qreg_0[1])
main_circ.u(-0.331000,param_1,param_0, qreg_0[1])
main_circ.append(subcirc0,[1,qreg_0[0],2,qreg_0[1]])
main_circ.u(-0.003000,param_0,param_1, 1)
main_circ.u(0.616000,param_1,-0.145000, 0)
main_circ.ry(-0.261000, 1)
main_circ.u(0,param_1,param_1, 3)
main_circ.append(subcirc0,[1,2,qreg_0[0],3])
main_circ.u(pi/2,0.191000,param_1, 0)
main_circ.u(0,0,-0.710000, 0)
main_circ.u(param_1,0,param_0, 2)
main_circ.u(param_0,-0.051000,-0.957000, 1)
main_circ.u(param_0,param_1,param_1, qreg_0[0])
main_circ.u(pi/2,param_0,-0.786000, 3)
main_circ.ry(param_1, qreg_0[0])
bindings = {param_0: -0.891000, param_1: 0.377000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1727")
