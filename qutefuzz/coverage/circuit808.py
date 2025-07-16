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
subcirc0.u(0,0,0.092000, qreg_0[2])
subcirc0.u(0,0,-0.732000, qreg_0[1])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.ry(0.322000, 1)
main_circ.append(subcirc0,[0,2,qreg_0[1],qreg_0[0],1])
main_circ.ry(0.188000, qreg_0[1])
main_circ.append(subcirc0,[3,0,1,qreg_0[0],2])
main_circ.ry(param_2, 1)
main_circ.z(0)
main_circ.u(0,0,param_3, qreg_0[0])
main_circ.z(0)
main_circ.ry(-0.280000, 1)
main_circ.u(0,param_1,param_4, qreg_0[0])
main_circ.u(param_3,param_3,param_0, 2)
main_circ.z(0)
main_circ.u(0,param_2,-0.595000, 3)
main_circ.ry(0.688000, 1)
main_circ.z(0)
main_circ.u(param_2,param_3,0.695000, 2)
main_circ.u(0,param_2,-0.460000, 2)
main_circ.z(1)
main_circ.u(0,param_3,-0.825000, 3)
main_circ.u(param_2,0,param_2, 3)
main_circ.cz(qreg_0[0],3)
main_circ.append(subcirc0,[3,qreg_0[0],0,qreg_0[1],1])
main_circ.cz(qreg_0[1],1)
main_circ.append(subcirc0,[0,qreg_0[1],3,qreg_0[0],2])
main_circ.u(param_0,0,param_3, 0)
main_circ.cz(2,qreg_0[1])
main_circ.append(subcirc0,[3,2,0,qreg_0[0],qreg_0[1]])
main_circ.cz(3,qreg_0[0])
main_circ.cz(3,2)
main_circ.cz(3,2)
main_circ.cz(2,0)
main_circ.cz(1,qreg_0[0])
main_circ.cz(0,2)
main_circ.cz(2,qreg_0[0])
main_circ.cz(2,1)
main_circ.cz(2,1)
main_circ.ry(-0.512000, 3)
main_circ.append(subcirc0,[0,3,2,qreg_0[1],1])
main_circ.u(0,0,-0.631000, qreg_0[1])
bindings = {param_0: 0.038000, param_1: -0.876000, param_2: -0.083000, param_3: -0.805000, param_4: 0.336000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "808")
