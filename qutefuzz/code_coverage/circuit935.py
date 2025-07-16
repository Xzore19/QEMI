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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(-0.863000, qreg_0[0])
subcirc0.u(0,0,0.076000, qreg_2[0])
subcirc0.rx(0.445000, qreg_2[1])
subcirc0.u(0,0,-0.340000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_7 = Parameter("param_7")

main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(param_3,0.833000,0.232000, 1)
main_circ.u(param_4,0,-0.331000, 2)
main_circ.rx(param_3, 2)
main_circ.u(0,param_1,param_1, 0)
main_circ.u(param_2,0.581000,param_2, 3)
main_circ.u(param_2,param_2,param_6, 2)
main_circ.rx(param_5, 2)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.u(pi/2,param_6,param_4, 1)
main_circ.u(0,param_3,param_2, 3)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.ry(param_0, 1)
main_circ.rx(0.214000, 2)
main_circ.ry(-0.825000, 3)
main_circ.u(pi/2,-0.489000,0.634000, 0)
main_circ.u(pi/2,param_0,-0.937000, 1)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.ry(param_2, 1)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.u(param_6,param_6,-0.414000, 3)
main_circ.rx(param_2, 0)
main_circ.rx(0.321000, 1)
main_circ.u(param_6,0.133000,0.135000, 0)
main_circ.rx(0.230000, 2)
main_circ.u(0,0,param_2, 1)
main_circ.append(subcirc0,[0,1,3,2])
main_circ.u(pi/2,-0.275000,-0.150000, 0)
main_circ.u(param_1,0,0.085000, 2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.rx(0.556000, 0)
main_circ.u(param_1,param_6,param_4, 1)
bindings = {param_0: -0.119000, param_1: 0.196000, param_2: -0.266000, param_3: 0.327000, param_4: -0.376000, param_5: -0.994000, param_6: 0.412000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "935")
