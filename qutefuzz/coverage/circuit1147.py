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
subcirc0.u(0,0,0.012000, qreg_0[0])
subcirc0.u(0,0,0.371000, qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0,0,-0.315000, qreg_1[2])
subcirc1.y(qreg_1[2])
subcirc1.u(0,0,0.093000, qreg_1[2])
subcirc1.h(qreg_1[1])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.h(0)
main_circ.append(subcirc1,[2,1,qreg_0[0],0])
main_circ.append(subcirc1,[qreg_0[0],0,3,2])
main_circ.y(0)
main_circ.cx(0,2)
main_circ.h(2)
main_circ.u(0,param_2,param_3, qreg_0[0])
main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
main_circ.append(subcirc1,[1,qreg_0[0],3,2])
main_circ.cx(3,2)
main_circ.y(qreg_0[0])
main_circ.u(param_3,0,param_0, 2)
main_circ.y(3)
main_circ.y(1)
main_circ.y(1)
main_circ.cx(2,1)
main_circ.append(subcirc1,[2,qreg_0[0],1,0])
main_circ.cx(0,2)
main_circ.append(subcirc1,[qreg_0[0],0,3,2])
main_circ.cx(qreg_0[0],0)
main_circ.cx(0,qreg_0[0])
main_circ.cx(0,3)
main_circ.cx(2,3)
main_circ.cx(1,0)
main_circ.cx(qreg_0[0],0)
main_circ.cx(1,3)
main_circ.cx(qreg_0[0],0)
main_circ.cx(3,qreg_0[0])
main_circ.cx(3,qreg_0[0])
main_circ.h(qreg_0[0])
bindings = {param_0: -0.527000, param_2: 0.905000, param_3: 0.506000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1147")
