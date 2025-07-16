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
subcirc0.rx(0.577000, qreg_3[0])
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0.u(0,0,0.768000, qreg_2[0])
subcirc0.rx(-0.685000, qreg_0[0])
subcirc0.h(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.u(0,0,0.605000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rx(param_0, 3)
main_circ.cy(1,qreg_0[0])
main_circ.cy(1,3)
main_circ.u(0,0,-0.885000, 3)
main_circ.h(2)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.cy(0,qreg_0[0])
main_circ.cy(0,3)
main_circ.append(subcirc0,[qreg_0[0],0,2,1])
main_circ.append(subcirc0,[1,3,0,2])
main_circ.cy(0,3)
main_circ.rx(0.877000, 2)
main_circ.rx(-0.964000, 3)
main_circ.cy(2,1)
main_circ.rx(0.869000, 3)
main_circ.append(subcirc0,[1,0,qreg_0[0],2])
main_circ.cy(0,2)
main_circ.cy(2,1)
main_circ.u(0,param_2,0.048000, 1)
main_circ.append(subcirc1,[0,2,1,qreg_0[0]])
main_circ.h(0)
bindings = {param_0: -0.302000, param_2: 0.653000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1699")
