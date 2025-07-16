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
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[3])
subcirc0.u(pi/2,-0.171000,0.810000, qreg_0[3])
subcirc0.u(pi/2,-0.369000,0.544000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_2,param_0,param_1, 1)
main_circ.cy(0,3)
main_circ.u(param_1,0.695000,0.834000, 2)
main_circ.cy(2,0)
main_circ.cy(0,1)
main_circ.append(subcirc0,[3,qreg_0[0],2,1,0])
main_circ.append(subcirc0,[3,1,qreg_0[0],0,2])
main_circ.z(0)
main_circ.u(pi/2,-0.346000,param_0, 1)
main_circ.cy(3,0)
main_circ.cy(1,2)
main_circ.u(param_0,0.238000,0.961000, 3)
main_circ.append(subcirc0,[0,qreg_0[0],3,1,2])
main_circ.append(subcirc0,[1,3,2,0,qreg_0[0]])
main_circ.u(-0.107000,-0.798000,0.097000, qreg_0[0])
main_circ.cy(2,qreg_0[0])
main_circ.cy(1,qreg_0[0])
main_circ.cy(0,1)
main_circ.u(pi/2,param_0,0.232000, 0)
main_circ.cy(3,2)
main_circ.cy(0,3)
main_circ.cy(2,3)
main_circ.u(param_1,0.684000,param_2, qreg_0[0])
main_circ.cy(0,1)
main_circ.cy(1,2)
main_circ.append(subcirc0,[1,3,qreg_0[0],2,0])
main_circ.cy(1,qreg_0[0])
main_circ.cy(1,0)
main_circ.cy(0,1)
main_circ.cy(3,2)
main_circ.append(subcirc0,[0,2,1,qreg_0[0],3])
main_circ.z(0)
main_circ.u(param_2,param_0,param_0, 1)
main_circ.cy(qreg_0[0],2)
main_circ.cy(0,3)
bindings = {param_0: -0.033000, param_1: 0.464000, param_2: -0.927000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
