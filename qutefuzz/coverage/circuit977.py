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
subcirc0.u(0,0,0.503000, qreg_0[1])
subcirc0.rz(0.006000, qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.y(1)
main_circ.append(subcirc0,[2,0,3,qreg_0[0],1])
main_circ.u(param_1,0,-0.727000, 3)
main_circ.y(2)
main_circ.y(0)
main_circ.append(subcirc0,[0,1,2,3,qreg_0[0]])
main_circ.y(0)
main_circ.append(subcirc0,[1,2,3,qreg_0[0],0])
main_circ.rz(0.143000, qreg_0[0])
main_circ.u(0,param_0,0.187000, 3)
main_circ.u(param_3,0,param_2, 0)
main_circ.h(2)
main_circ.append(subcirc0,[1,0,3,2,qreg_0[0]])
main_circ.u(0,0,0.008000, 0)
main_circ.rz(param_1, 2)
main_circ.h(2)
main_circ.rz(-0.909000, 0)
main_circ.y(2)
main_circ.y(qreg_0[0])
main_circ.u(0,param_1,param_1, 2)
main_circ.rz(param_0, qreg_0[0])
main_circ.u(param_1,param_2,0.347000, 0)
main_circ.append(subcirc0,[qreg_0[0],2,0,3,1])
main_circ.h(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],2,3,1,0])
main_circ.h(3)
bindings = {param_0: -0.850000, param_1: 0.884000, param_2: -0.066000, param_3: -0.529000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "977")
