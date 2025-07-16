from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(-0.272000, qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[1])
subcirc0.rz(-0.834000, qreg_0[1])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.rx(0.221000, qreg_0[0])

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

main_circ.rx(param_0, 2)
main_circ.u(0,param_0,param_0, 2)
main_circ.u(param_0,0,param_0, qreg_0[0])
main_circ.cz(3,0)
main_circ.u(0,param_0,-0.986000, 1)
main_circ.u(0,param_0,param_0, 2)
main_circ.append(subcirc0,[2,qreg_0[0],3,0])
main_circ.append(subcirc0,[1,3,qreg_0[0],2])
main_circ.append(subcirc0,[3,0,1,qreg_0[0]])
main_circ.rx(param_0, 2)
main_circ.rz(0.968000, 2)
main_circ.rx(0.953000, qreg_0[0])
main_circ.cz(3,1)
main_circ.u(param_0,0,param_0, 3)
main_circ.cz(0,qreg_0[0])
main_circ.u(param_0,0,-0.132000, 0)
main_circ.cz(2,qreg_0[0])
main_circ.u(0,param_0,0.348000, 0)
main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_0, 3)
main_circ.append(subcirc0,[2,0,qreg_0[0],1])
main_circ.cz(3,0)
main_circ.cz(3,0)
main_circ.rz(-0.335000, 2)
main_circ.u(param_0,0,0.569000, 3)
main_circ.rz(-0.130000, 2)
main_circ.cz(3,1)
main_circ.u(0,0,-0.816000, 1)
main_circ.rx(param_0, 3)
main_circ.cz(1,2)
main_circ.u(param_0,param_0,param_0, 1)
main_circ.cz(3,1)
main_circ.u(param_0,param_0,-0.048000, 0)
bindings = {param_0: -0.447000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1090")
