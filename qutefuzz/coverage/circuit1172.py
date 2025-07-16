from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.rz(0.180000, qreg_0[0])
subcirc0.u(0,0,-0.733000, qreg_0[0])
subcirc0.rz(-0.856000, qreg_1[1])
subcirc0.u(-0.842000,-0.833000,0.896000, qreg_1[2])
subcirc0.u(0,0,0.759000, qreg_1[1])
subcirc0.u(0.487000,0.576000,0.519000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rz(param_0, qreg_0[0])
main_circ.u(0.866000,-0.921000,param_0, 3)
main_circ.rz(param_0, 0)
main_circ.append(subcirc0,[2,3,1,qreg_0[1]])
main_circ.u(0.752000,param_0,-0.202000, 2)
main_circ.rz(0.409000, 1)
main_circ.x(3)
main_circ.u(0,0,-0.348000, qreg_0[0])
main_circ.x(0)
main_circ.u(param_0,0,0.450000, 0)
main_circ.rz(-0.003000, qreg_0[1])
main_circ.u(param_0,param_0,param_0, 2)
main_circ.u(-0.963000,-0.479000,0.620000, 3)
main_circ.x(0)
main_circ.rz(param_0, 3)
main_circ.append(subcirc0,[3,qreg_0[0],2,qreg_0[1]])
main_circ.u(-0.557000,0.462000,-0.204000, 2)
main_circ.u(param_0,param_0,-0.721000, 3)
main_circ.u(param_0,param_0,-0.155000, 0)
main_circ.rz(param_0, qreg_0[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.u(-0.279000,param_0,param_0, 3)
main_circ.rz(param_0, 1)
main_circ.rz(param_0, 2)
main_circ.u(param_0,param_0,0.989000, qreg_0[1])
main_circ.x(2)
main_circ.rz(0.760000, 1)
main_circ.append(subcirc0,[2,3,qreg_0[1],0])
main_circ.u(0.496000,param_0,param_0, 0)
main_circ.u(0,param_0,param_0, 3)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.u(-0.900000,param_0,param_0, qreg_0[1])
main_circ.rz(param_0, qreg_0[0])
main_circ.rz(-0.811000, qreg_0[1])
main_circ.u(0.105000,param_0,0.081000, 0)
bindings = {param_0: 0.224000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1172")
