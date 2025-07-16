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
subcirc0.u(0,0,-0.883000, qreg_0[1])
subcirc0.x(qreg_0[0])
subcirc0.u(0.677000,0.029000,0.008000, qreg_0[1])
subcirc0.u(-0.257000,0.607000,0.948000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.629000,-0.465000,0.701000, qreg_0[2])
subcirc1.u(0.169000,0.367000,-0.236000, qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.u(0,0,-0.403000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.u(0,0,0.867000, qreg_0[2])
subcirc2.x(qreg_0[3])
subcirc2.x(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[3])
subcirc3.h(qreg_0[0])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.append(subcirc1,[0,qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[3],qreg_0[2],qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[3],0,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.u(-0.974000,param_2,-0.080000, qreg_0[0])
main_circ.append(subcirc3,[qreg_0[3],qreg_0[2],0,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc3,[qreg_0[1],0,qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[3],0,qreg_0[0],qreg_0[2]])
main_circ.x(qreg_0[2])
main_circ.h(0)
main_circ.u(param_1,-0.495000,param_0, qreg_0[0])
main_circ.u(0.784000,param_1,param_1, qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.x(0)
main_circ.h(0)
main_circ.u(param_2,0,0.475000, 0)
bindings = {param_0: 0.420000, param_1: 0.715000, param_2: 0.051000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
