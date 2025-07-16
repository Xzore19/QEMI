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
subcirc0.u(0,0,0.741000, qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0.u(-0.986000,0.981000,-0.929000, qreg_0[3])
subcirc0.z(qreg_0[3])
subcirc0.ry(0.859000, qreg_0[0])

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

main_circ.append(subcirc0,[0,3,1,2])
main_circ.append(subcirc0,[1,3,2,0])
main_circ.u(param_1,0,param_2, 2)
main_circ.append(subcirc0,[0,3,2,1])
main_circ.append(subcirc0,[3,0,2,1])
main_circ.ry(-0.424000, 1)
main_circ.ry(-0.434000, 2)
main_circ.u(param_0,-0.276000,-0.886000, 3)
main_circ.u(0.849000,param_3,param_1, 3)
main_circ.ry(0.281000, 1)
main_circ.u(0,param_1,param_3, 3)
main_circ.u(0.185000,-0.757000,-0.399000, 2)
main_circ.u(0,0,param_3, 0)
main_circ.u(param_0,param_0,param_1, 2)
main_circ.append(subcirc0,[1,2,0,3])
main_circ.append(subcirc0,[1,2,0,3])
main_circ.u(0,param_2,param_1, 1)
main_circ.u(0,0,0.810000, 3)
main_circ.u(0,param_3,-0.948000, 3)
main_circ.u(-0.328000,0.974000,param_2, 3)
main_circ.ry(-0.053000, 0)
main_circ.u(param_2,param_3,-0.427000, 3)
main_circ.ry(param_0, 1)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.u(0,param_0,0.564000, 3)
main_circ.z(1)
main_circ.u(-0.097000,-0.248000,param_2, 1)
bindings = {param_0: -0.893000, param_1: -0.790000, param_2: -0.679000, param_3: -0.604000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "477")
