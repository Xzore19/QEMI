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
subcirc0.ry(0.414000, qreg_1[0])
subcirc0.rz(0.779000, qreg_1[0])
subcirc0.u(pi/2,-0.363000,0.298000, qreg_1[1])
subcirc0.ry(0.764000, qreg_0[0])
subcirc0.u(pi/2,-0.993000,-0.727000, qreg_3[0])
subcirc0.u(pi/2,0.253000,0.918000, qreg_1[1])

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

main_circ.ry(0.404000, 1)
main_circ.cy(qreg_0[0],2)
main_circ.cy(qreg_0[0],2)
main_circ.u(param_0,param_0,-0.297000, 3)
main_circ.append(subcirc0,[0,qreg_0[0],1,3])
main_circ.ry(0.953000, 0)
main_circ.u(pi/2,param_0,-0.802000, qreg_0[0])
main_circ.u(param_0,0.623000,param_0, 0)
main_circ.u(param_0,0.589000,param_0, 0)
main_circ.u(pi/2,0.073000,-0.596000, 1)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.cy(qreg_0[0],2)
main_circ.rz(param_0, 3)
main_circ.ry(0.085000, 0)
main_circ.append(subcirc0,[qreg_0[0],1,2,0])
main_circ.append(subcirc0,[0,1,qreg_0[0],3])
main_circ.cy(3,qreg_0[0])
main_circ.cy(qreg_0[0],3)
main_circ.cy(0,qreg_0[0])
main_circ.ry(-0.794000, 0)
main_circ.ry(param_0, 1)
main_circ.cy(3,2)
main_circ.rz(param_0, qreg_0[0])
main_circ.cy(3,qreg_0[0])
main_circ.cy(2,qreg_0[0])
main_circ.cy(2,0)
main_circ.cy(qreg_0[0],3)
main_circ.cy(1,2)
main_circ.cy(1,3)
main_circ.cy(qreg_0[0],3)
main_circ.cy(qreg_0[0],0)
main_circ.cy(3,2)
main_circ.u(pi/2,0.406000,-0.858000, 3)
main_circ.cy(2,0)
main_circ.u(pi/2,param_0,0.825000, qreg_0[0])
main_circ.rz(0.938000, 2)
main_circ.cy(qreg_0[0],3)
main_circ.rz(param_0, 0)
main_circ.rz(param_0, 2)
bindings = {param_0: -0.491000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
