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
subcirc0.u(pi/2,0.640000,0.826000, qreg_0[2])
subcirc0.u(pi/2,-0.377000,-0.921000, qreg_0[2])
subcirc0.u(0,0,0.350000, qreg_0[0])
subcirc0.u(0,0,-0.014000, qreg_3[0])
subcirc0.ry(-0.124000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(0,0,param_0, 1)
main_circ.ry(0.892000, 2)
main_circ.h(3)
main_circ.u(param_1,0,0.700000, 2)
main_circ.h(3)
main_circ.u(param_1,0,param_0, 2)
main_circ.h(3)
main_circ.h(1)
main_circ.u(0,param_1,0.275000, 1)
main_circ.h(2)
main_circ.h(3)
main_circ.u(pi/2,param_0,-0.059000, 1)
main_circ.ry(param_1, 2)
main_circ.u(param_1,param_0,0.709000, 1)
main_circ.ry(0.139000, 0)
main_circ.u(param_1,0.700000,-0.351000, 0)
main_circ.u(param_0,param_0,param_0, 1)
main_circ.u(param_0,param_0,param_1, 0)
main_circ.h(1)
main_circ.ry(0.702000, 2)
main_circ.u(param_0,param_0,param_1, 2)
main_circ.u(param_1,-0.312000,param_1, 3)
main_circ.u(pi/2,-0.085000,param_1, 2)
main_circ.u(param_1,-0.186000,-0.947000, 3)
main_circ.u(0,param_1,0.824000, 2)
main_circ.u(param_0,param_1,param_1, 0)
main_circ.u(pi/2,param_1,0.844000, 2)
main_circ.u(pi/2,param_0,param_1, 1)
main_circ.u(param_0,param_1,param_0, 2)
main_circ.h(3)
main_circ.h(1)
main_circ.u(param_1,0,-0.043000, 1)
main_circ.u(param_1,param_1,param_0, 1)
main_circ.u(param_0,param_1,param_0, 3)
main_circ.h(2)
main_circ.u(0,param_1,param_1, 3)
main_circ.ry(0.666000, 2)
main_circ.ry(param_1, 3)
main_circ.ry(param_0, 1)
main_circ.u(param_0,0,0.299000, 3)
main_circ.h(3)
main_circ.u(0,0,-0.536000, 3)
bindings = {param_0: -0.874000, param_1: -0.196000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1869")
