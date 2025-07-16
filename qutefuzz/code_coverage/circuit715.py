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
subcirc0.rz(-0.290000, qreg_2[0])
subcirc0.x(qreg_2[0])
subcirc0.cx(qreg_0[1],qreg_2[1])
subcirc0.rz(0.753000, qreg_2[0])
subcirc0.h(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[3])
subcirc1.h(qreg_0[0])
subcirc1.x(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_3[0])
subcirc2.h(qreg_0[2])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.x(qreg_0[1])
subcirc3.x(qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3.h(qreg_0[3])
subcirc3.x(qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cx(qreg_2[0],qreg_0[0])
subcirc4.x(qreg_0[1])
subcirc4.x(qreg_2[1])
subcirc4.h(qreg_2[1])
subcirc4.x(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

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
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[qreg_0[0],1,3,0])
main_circ.append(subcirc0,[0,2,qreg_0[0],3])
main_circ.rz(param_0, 3)
main_circ.append(subcirc3,[qreg_0[0],1,3,0])
main_circ.append(subcirc0,[3,2,qreg_0[0],1])
main_circ.x(2)
main_circ.rz(-0.058000, 3)
main_circ.append(subcirc0,[0,qreg_0[0],1,2])
main_circ.cx(3,qreg_0[0])
main_circ.cx(1,0)
main_circ.rz(0.884000, 0)
main_circ.h(3)
main_circ.h(qreg_0[0])
main_circ.rz(-0.808000, qreg_0[0])
main_circ.h(2)
main_circ.cx(2,0)
main_circ.cx(qreg_0[0],3)
main_circ.cx(2,3)
main_circ.cx(0,3)
main_circ.cx(2,3)
main_circ.cx(2,3)
main_circ.cx(qreg_0[0],2)
main_circ.cx(3,1)
main_circ.cx(2,qreg_0[0])
main_circ.rz(0.097000, 1)
main_circ.append(subcirc3,[0,qreg_0[0],1,2])
bindings = {param_0: 0.287000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "715")
