from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_3[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.h(qreg_2[0])
subcirc0.u(0.502000,-0.199000,-0.433000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[1],qreg_0[2])
subcirc1.u(-0.005000,-0.062000,-0.922000, qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_0[1])
subcirc1.u(-0.911000,0.674000,0.218000, qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_2[0])
subcirc2.cz(qreg_0[1],qreg_2[0])
subcirc2.u(-0.634000,-0.331000,0.346000, qreg_3[0])
subcirc2.z(qreg_0[0])
subcirc2.h(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3.cz(qreg_3[0],qreg_1[1])
subcirc3.h(qreg_1[0])
subcirc3.cz(qreg_3[0],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.h(qreg_0[1])
main_circ.h(qreg_0[2])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2],0])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.u(param_0,param_0,param_5, qreg_0[2])
main_circ.cz(0,qreg_0[0])
main_circ.u(0.311000,-0.866000,param_5, qreg_0[2])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.u(0.754000,param_0,-0.424000, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[3],qreg_0[1],qreg_0[2],0])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],0,qreg_0[3]])
main_circ.z(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[3],0,qreg_0[0],qreg_0[1]])
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[0],0)
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.h(qreg_0[3])
main_circ.h(0)
main_circ.z(qreg_0[3])
main_circ.u(param_6,-0.387000,param_1, qreg_0[2])
main_circ.u(-0.584000,0.332000,-0.143000, qreg_0[0])
bindings = {param_0: -0.981000, param_1: 0.993000, param_5: 0.712000, param_6: -0.545000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "334")
