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
subcirc0.u(-0.687000,-0.788000,0.490000, qreg_0[1])
subcirc0.u(pi/2,0.420000,0.620000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_0[1])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.588000,0.162000, qreg_1[0])
subcirc1.cz(qreg_1[0],qreg_3[0])
subcirc1.cz(qreg_1[0],qreg_3[0])
subcirc1.cy(qreg_1[1],qreg_1[0])
subcirc1.cz(qreg_0[0],qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,-0.527000,-0.215000, qreg_0[0])
subcirc2.u(-0.433000,0.496000,0.055000, qreg_0[0])
subcirc2.u(-0.085000,-0.745000,0.313000, qreg_0[3])
subcirc2.u(pi/2,-0.403000,-0.483000, qreg_0[0])
subcirc2.u(pi/2,0.691000,-0.497000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.cz(qreg_1[2],qreg_1[0])
subcirc3.cz(qreg_1[0],qreg_0[0])
subcirc3.u(0.361000,0.731000,-0.149000, qreg_1[1])
subcirc3.u(pi/2,0.711000,-0.480000, qreg_0[0])
subcirc3.u(pi/2,0.617000,-0.287000, qreg_1[1])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(1)
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

main_circ.u(param_3,param_3,param_3, qreg_0[3])
main_circ.append(subcirc1,[qreg_0[3],0,qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.u(param_1,-0.864000,0.043000, 0)
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],0])
main_circ.u(0.797000,param_2,0.820000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],0,qreg_0[2],qreg_0[0]])
main_circ.u(0.745000,param_2,param_3, qreg_0[3])
main_circ.u(pi/2,param_0,0.855000, qreg_0[3])
main_circ.u(param_3,-0.272000,param_2, 0)
main_circ.u(0.020000,param_1,param_3, 0)
main_circ.append(subcirc2,[qreg_0[1],0,qreg_0[0],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_0[3]])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3],0])
main_circ.u(pi/2,-0.208000,0.717000, qreg_0[0])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.u(-0.391000,param_1,param_0, qreg_0[2])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],qreg_0[1],0,qreg_0[2]])
main_circ.cy(qreg_0[1],0)
main_circ.u(pi/2,param_1,param_2, 0)
main_circ.u(param_3,param_0,param_2, qreg_0[1])
main_circ.cy(qreg_0[3],0)
main_circ.u(param_2,param_1,-0.197000, qreg_0[2])
main_circ.u(param_3,0.157000,param_2, qreg_0[2])
bindings = {param_0: 0.968000, param_1: -0.986000, param_2: 0.174000, param_3: -0.481000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
