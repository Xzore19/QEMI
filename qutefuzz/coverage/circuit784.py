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
subcirc0.h(qreg_0[3])
subcirc0.h(qreg_0[0])
subcirc0.cx(qreg_0[3],qreg_0[2])
subcirc0.u(0,0,0.362000, qreg_0[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_4 = Parameter("param_4")

main_circ.z(qreg_1[0])
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_2[0],0])
main_circ.h(qreg_2[0])
main_circ.z(0)
main_circ.append(subcirc0,[1,qreg_3[0],0,qreg_1[0]])
main_circ.z(0)
main_circ.h(qreg_3[0])
main_circ.cx(qreg_2[0],1)
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],0,1])
main_circ.z(1)
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_1[0],1])
main_circ.h(qreg_0[0])
main_circ.u(param_1,param_0,-0.578000, 0)
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.h(qreg_3[0])
main_circ.u(param_0,0,param_1, qreg_0[0])
main_circ.h(qreg_2[0])
main_circ.cx(1,0)
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(0,qreg_3[0])
main_circ.cx(0,qreg_1[0])
main_circ.cx(1,qreg_0[0])
main_circ.h(0)
main_circ.h(qreg_0[0])
main_circ.h(0)
main_circ.cx(1,qreg_0[0])
main_circ.cx(0,qreg_2[0])
main_circ.z(qreg_3[0])
main_circ.cx(0,qreg_1[0])
main_circ.h(qreg_1[0])
bindings = {param_0: -0.468000, param_1: -0.186000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "784")
