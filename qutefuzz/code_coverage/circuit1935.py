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
subcirc0.rx(-0.211000, qreg_0[1])
subcirc0.ry(0.231000, qreg_0[2])
subcirc0.rx(-0.516000, qreg_0[1])
subcirc0.u(0,0,0.114000, qreg_0[3])
subcirc0.ry(0.588000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.z(0)
main_circ.z(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_0[1],qreg_3[0]])
main_circ.rx(param_1, qreg_0[0])
main_circ.u(0,0,param_2, qreg_0[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0],0])
main_circ.rx(param_3, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],0,qreg_3[0]])
main_circ.rx(-0.235000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],0,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0],0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],0,qreg_0[0],qreg_3[0]])
main_circ.u(0,0,-0.129000, qreg_3[0])
main_circ.z(qreg_0[2])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.rx(param_1, 0)
main_circ.u(param_3,0,-0.388000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],0,qreg_3[0]])
main_circ.ry(param_0, qreg_0[2])
main_circ.rx(param_3, qreg_0[0])
main_circ.u(param_3,0,param_2, qreg_0[0])
main_circ.ry(param_1, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],0,qreg_3[0],qreg_0[2]])
bindings = {param_0: -1.000000, param_1: 0.660000, param_2: 0.968000, param_3: 0.058000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1935")
