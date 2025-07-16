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
subcirc0.h(qreg_0[0])
subcirc0.u(0,0,0.519000, qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.cx(0,3)
main_circ.u(0,0,param_0, 0)
main_circ.h(0)
main_circ.u(param_0,0,param_0, 2)
main_circ.cx(2,3)
main_circ.cx(1,0)
main_circ.u(param_1,param_1,-0.960000, 0)
main_circ.cx(0,1)
main_circ.cx(0,3)
main_circ.cx(2,0)
main_circ.h(3)
main_circ.h(0)
main_circ.cx(2,3)
main_circ.cx(1,0)
main_circ.cx(3,0)
main_circ.h(1)
main_circ.u(pi/2,0.067000,param_1, 3)
main_circ.h(1)
main_circ.u(pi/2,param_0,-0.678000, 2)
main_circ.h(2)
main_circ.h(0)
main_circ.h(3)
main_circ.u(param_1,param_0,param_0, 1)
main_circ.h(0)
main_circ.u(0,0,-0.977000, 0)
main_circ.u(param_0,param_0,0.877000, 3)
main_circ.u(pi/2,param_1,param_0, 2)
main_circ.cx(0,3)
main_circ.u(pi/2,param_1,param_1, 0)
main_circ.h(0)
main_circ.cx(3,1)
main_circ.cx(0,2)
main_circ.h(2)
main_circ.u(pi/2,0.988000,param_0, 0)
main_circ.u(param_0,param_1,-0.576000, 1)
main_circ.u(param_0,param_0,param_1, 1)
main_circ.u(0,param_0,param_1, 1)
main_circ.cx(1,3)
main_circ.u(param_0,0,-0.608000, 2)
main_circ.u(pi/2,-0.053000,-0.853000, 3)
main_circ.u(pi/2,param_1,param_1, 0)
main_circ.u(param_0,0,-0.325000, 1)
bindings = {param_0: 0.204000, param_1: 0.863000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1141")
