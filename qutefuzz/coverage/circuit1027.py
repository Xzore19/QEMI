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
subcirc0.u(pi/2,-0.680000,-0.655000, qreg_3[0])
subcirc0.u(pi/2,-0.586000,0.922000, qreg_0[0])
subcirc0.u(pi/2,-0.746000,-0.225000, qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.cy(qreg_1[1],qreg_3[0])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1.y(qreg_0[0])
subcirc1.u(pi/2,0.872000,-0.029000, qreg_3[0])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[1,qreg_0[0],qreg_1[0],3,0,2])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],3,0])
main_circ.cy(2,1)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.ry(-0.340000, 3)
main_circ.u(pi/2,-0.695000,param_0, 1)
main_circ.append(subcirc1,[0,2,qreg_1[0],1,3,qreg_0[0]])
main_circ.y(1)
main_circ.append(subcirc0,[2,1,0,3])
main_circ.y(1)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.append(subcirc0,[qreg_0[0],3,0,1])
main_circ.cy(qreg_1[0],3)
main_circ.cy(2,qreg_1[0])
main_circ.cy(3,qreg_0[0])
main_circ.cy(3,1)
main_circ.cy(3,qreg_1[0])
main_circ.cy(0,1)
main_circ.cy(2,qreg_0[0])
main_circ.cy(3,qreg_0[0])
main_circ.y(3)
main_circ.ry(0.315000, qreg_1[0])
main_circ.u(pi/2,0.789000,-0.600000, 3)
main_circ.y(qreg_0[0])
main_circ.y(1)
main_circ.cy(1,0)
main_circ.cy(1,0)
main_circ.cy(0,3)
bindings = {param_0: 0.482000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1027")
