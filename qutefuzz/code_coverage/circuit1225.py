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
subcirc0.rx(-0.473000, qreg_0[1])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.u(-0.791000,0.987000,-0.261000, qreg_0[1])
subcirc0.rx(0.489000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.990000,0.073000,-0.820000, qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1.rx(-0.421000, qreg_3[0])
subcirc1.u(0.479000,-0.272000,0.333000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[2],qreg_0[1])
subcirc2.h(qreg_0[0])
subcirc2.u(-0.199000,-0.049000,0.031000, qreg_0[2])
subcirc2.rx(0.877000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.854000,0.979000,-0.162000, qreg_3[0])
subcirc3.rx(0.814000, qreg_2[0])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.u(-0.388000,0.033000,-0.991000, qreg_2[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cz(qreg_0[1],qreg_2[1])
subcirc4.rx(0.466000, qreg_0[1])
subcirc4.rx(-0.518000, qreg_2[0])
subcirc4.rx(0.778000, qreg_2[1])
subcirc4 = subcirc4.to_gate().control(3)

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

main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],2,3,0,1,qreg_0[0]])
main_circ.append(subcirc1,[1,3,qreg_0[0],qreg_0[1],0,2])
main_circ.u(param_1,-0.573000,-0.544000, 0)
main_circ.h(qreg_0[0])
main_circ.h(1)
main_circ.rx(-0.132000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[1],3,0,2,qreg_0[0],1])
main_circ.rx(param_0, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],2,qreg_0[1],0,3,1])
main_circ.append(subcirc3,[qreg_0[0],3,1,2])
main_circ.u(param_1,0.542000,0.749000, qreg_0[0])
main_circ.append(subcirc1,[2,1,0,qreg_0[0],qreg_0[1],3])
main_circ.u(param_1,0.325000,-0.982000, 0)
main_circ.append(subcirc2,[0,3,2,qreg_0[1],1,qreg_0[0]])
main_circ.cz(0,3)
main_circ.append(subcirc0,[1,3,qreg_0[1],qreg_0[0],0])
main_circ.cz(qreg_0[0],2)
main_circ.cz(qreg_0[1],2)
main_circ.cz(qreg_0[1],0)
main_circ.cz(3,qreg_0[1])
main_circ.cz(1,3)
main_circ.cz(qreg_0[0],0)
main_circ.cz(0,3)
main_circ.cz(0,1)
main_circ.cz(qreg_0[0],1)
main_circ.cz(0,qreg_0[0])
main_circ.cz(3,2)
main_circ.cz(1,3)
main_circ.cz(0,2)
main_circ.append(subcirc1,[2,qreg_0[0],1,3,qreg_0[1],0])
main_circ.rx(param_1, 0)
main_circ.rx(param_1, 0)
bindings = {param_0: 0.581000, param_1: -0.145000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1225")
