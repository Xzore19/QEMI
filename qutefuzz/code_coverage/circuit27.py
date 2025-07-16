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
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.u(0,0,0.472000, qreg_0[1])
subcirc0.u(0,0,0.153000, qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_3[0])
subcirc0.ry(0.478000, qreg_0[0])
subcirc0.ry(0.991000, qreg_0[1])

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

main_circ.ry(-0.485000, 2)
main_circ.cz(3,0)
main_circ.cz(1,3)
main_circ.cz(3,1)
main_circ.ry(param_1, 1)
main_circ.h(qreg_0[0])
main_circ.cz(1,3)
main_circ.u(0,0,-0.944000, 2)
main_circ.cz(2,0)
main_circ.cz(0,2)
main_circ.cz(3,1)
main_circ.ry(param_0, 2)
main_circ.cz(qreg_0[0],0)
main_circ.u(0,0,-0.783000, 3)
main_circ.h(3)
main_circ.ry(0.275000, 0)
main_circ.append(subcirc0,[3,2,1,qreg_0[0]])
main_circ.h(2)
main_circ.cz(qreg_0[0],0)
main_circ.cz(0,qreg_0[0])
main_circ.cz(2,0)
main_circ.cz(0,qreg_0[0])
main_circ.u(param_1,param_0,param_1, qreg_0[0])
main_circ.u(param_1,0,param_1, 3)
main_circ.cz(1,0)
main_circ.u(0,param_0,param_1, 0)
main_circ.append(subcirc0,[qreg_0[0],1,3,2])
main_circ.ry(param_1, 3)
main_circ.ry(param_1, 2)
main_circ.append(subcirc0,[0,2,qreg_0[0],1])
main_circ.u(0,0,0.288000, 1)
main_circ.append(subcirc0,[qreg_0[0],1,3,0])
main_circ.cz(1,0)
bindings = {param_0: 0.681000, param_1: -0.857000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "27")
