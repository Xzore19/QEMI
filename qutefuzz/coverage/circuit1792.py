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
subcirc0.z(qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,-0.323000,0.631000, qreg_0[3])
subcirc1.ry(0.134000, qreg_0[2])
subcirc1.z(qreg_0[2])
subcirc1.u(pi/2,-0.200000,0.592000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

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

main_circ.cz(qreg_0[0],0)
main_circ.z(0)
main_circ.ry(param_0, 0)
main_circ.cz(3,qreg_0[0])
main_circ.ry(-0.774000, 3)
main_circ.append(subcirc0,[1,3,0,qreg_0[0]])
main_circ.ry(param_0, 2)
main_circ.ry(param_0, 0)
main_circ.cz(2,3)
main_circ.u(pi/2,-0.654000,0.230000, 3)
main_circ.z(1)
main_circ.ry(-0.597000, 1)
main_circ.u(pi/2,-0.507000,-0.224000, 0)
main_circ.cz(qreg_0[0],0)
main_circ.ry(param_0, 0)
main_circ.cz(1,0)
main_circ.cz(qreg_0[0],0)
main_circ.z(qreg_0[0])
main_circ.z(3)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.ry(0.523000, qreg_0[0])
main_circ.cz(0,1)
main_circ.append(subcirc0,[0,1,3,qreg_0[0]])
main_circ.z(qreg_0[0])
main_circ.cz(1,2)
main_circ.cz(qreg_0[0],1)
main_circ.cz(1,3)
main_circ.u(pi/2,0.465000,0.350000, qreg_0[0])
main_circ.ry(0.430000, 1)
main_circ.append(subcirc0,[qreg_0[0],2,1,0])
main_circ.u(param_0,-0.733000,0.522000, 2)
main_circ.u(param_0,0.694000,0.534000, 3)
main_circ.ry(param_0, 0)
bindings = {param_0: 0.958000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
