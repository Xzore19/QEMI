from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.y(qreg_2[1])
subcirc0.u(pi/2,0.670000,0.822000, qreg_2[1])
subcirc0.cx(qreg_0[0],qreg_2[0])
subcirc0.y(qreg_2[1])
subcirc0.cx(qreg_0[0],qreg_2[1])
subcirc0.cx(qreg_2[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.rx(-0.958000, qreg_0[1])
subcirc1.y(qreg_2[0])
subcirc1.cx(qreg_2[1],qreg_2[0])
subcirc1.rx(0.969000, qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(1)
main_circ.append(subcirc0,[qreg_0[1],0,3,2])
main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.rx(param_0, qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.rx(0.584000, 3)
main_circ.append(subcirc0,[0,qreg_0[0],2,1])
main_circ.u(pi/2,param_0,-0.024000, 0)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[0,qreg_0[1],3,qreg_0[0]])
main_circ.cx(2,qreg_0[1])
main_circ.append(subcirc1,[3,qreg_0[0],qreg_0[1],1])
main_circ.cx(1,qreg_0[0])
main_circ.rx(param_0, 0)
main_circ.append(subcirc0,[qreg_0[1],2,1,qreg_0[0]])
main_circ.y(2)
main_circ.rx(param_0, 1)
main_circ.u(pi/2,param_0,param_0, 0)
bindings = {param_0: 0.854000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1886")
