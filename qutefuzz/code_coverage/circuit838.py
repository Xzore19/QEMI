from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(0,0,0.225000, qreg_1[2])
subcirc0.u(-0.872000,-0.245000,0.477000, qreg_0[0])
subcirc0.u(0,0,-0.761000, qreg_1[1])
subcirc0.y(qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.714000,0.713000,-0.703000, qreg_0[2])
subcirc1.u(-0.411000,0.439000,-0.964000, qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[1])
subcirc1.u(-0.093000,0.697000,-0.425000, qreg_0[1])

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

main_circ.cz(3,1)
main_circ.u(-0.977000,param_0,param_0, 2)
main_circ.append(subcirc1,[3,qreg_0[0],1,2])
main_circ.y(1)
main_circ.u(0,0,param_0, 2)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.u(0.986000,param_0,0.261000, 1)
main_circ.y(0)
main_circ.cz(1,2)
main_circ.u(0,param_0,-0.168000, 2)
main_circ.cz(2,3)
main_circ.y(qreg_0[0])
main_circ.cz(0,qreg_0[0])
main_circ.u(param_0,param_0,-0.565000, qreg_0[0])
main_circ.cz(0,1)
main_circ.y(3)
main_circ.cz(qreg_0[0],1)
main_circ.u(param_0,0,param_0, 3)
main_circ.append(subcirc1,[3,qreg_0[0],2,0])
main_circ.y(2)
main_circ.u(param_0,0,param_0, 0)
main_circ.append(subcirc1,[3,qreg_0[0],1,0])
main_circ.cz(1,qreg_0[0])
main_circ.cz(qreg_0[0],2)
main_circ.cz(1,0)
main_circ.y(0)
main_circ.u(param_0,0,param_0, qreg_0[0])
main_circ.append(subcirc1,[0,3,1,2])
bindings = {param_0: 0.072000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
