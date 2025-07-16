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
subcirc0.s(qreg_0[0])
subcirc0.u(0.342000,0.672000,0.386000, qreg_0[0])
subcirc0.ry(-0.627000, qreg_2[0])
subcirc0.s(qreg_2[0])
subcirc0.s(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.u(-0.905000,0.723000,0.989000, qreg_0[0])
subcirc1.ry(0.518000, qreg_0[0])
subcirc1.ry(0.474000, qreg_0[2])
subcirc1.u(pi/2,-0.197000,0.646000, qreg_0[0])

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
param_5 = Parameter("param_5")

main_circ.u(0.592000,param_5,param_5, 1)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.s(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],2,0,1])
main_circ.u(pi/2,param_3,0.400000, 1)
main_circ.ry(param_2, 1)
main_circ.u(param_4,param_4,0.500000, 0)
main_circ.u(-0.784000,0.786000,-0.194000, 1)
main_circ.u(param_0,param_2,-0.235000, 2)
main_circ.append(subcirc1,[1,qreg_0[0],3,2])
main_circ.ry(param_2, 3)
main_circ.append(subcirc0,[qreg_0[0],0,2,3])
main_circ.s(qreg_0[0])
main_circ.u(0.885000,param_4,0.710000, qreg_0[0])
main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
main_circ.append(subcirc1,[0,qreg_0[0],3,2])
main_circ.append(subcirc0,[0,2,qreg_0[0],3])
main_circ.ry(0.521000, qreg_0[0])
bindings = {param_0: 0.819000, param_2: -0.486000, param_3: 0.104000, param_4: -0.709000, param_5: 0.197000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1678")
