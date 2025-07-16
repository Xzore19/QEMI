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
subcirc0.u(-0.218000,-0.677000,-0.940000, qreg_2[0])
subcirc0.u(0.895000,-0.609000,0.836000, qreg_2[1])
subcirc0.u(-0.899000,-0.839000,-0.781000, qreg_1[0])
subcirc0.cx(qreg_2[0],qreg_1[0])
subcirc0.y(qreg_0[0])
subcirc0.y(qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.cz(0,1)
main_circ.cz(0,2)
main_circ.y(3)
main_circ.u(0.134000,-0.616000,param_0, 2)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cz(3,1)
main_circ.cx(0,1)
main_circ.cx(0,1)
main_circ.u(param_1,0.262000,0.860000, 0)
main_circ.cx(1,2)
main_circ.cx(0,1)
main_circ.append(subcirc0,[2,0,3,1])
main_circ.cz(1,2)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.cx(0,3)
main_circ.u(-0.910000,-0.925000,param_1, 2)
main_circ.y(0)
main_circ.cz(3,2)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.y(3)
main_circ.cx(3,0)
main_circ.cx(3,2)
main_circ.cz(1,3)
main_circ.cz(1,0)
main_circ.u(param_1,param_0,-0.648000, 1)
bindings = {param_0: 0.401000, param_1: -0.741000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
