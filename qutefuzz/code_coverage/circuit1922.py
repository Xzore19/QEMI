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
subcirc0.rz(-0.412000, qreg_0[0])
subcirc0.u(-0.187000,-0.400000,-0.857000, qreg_0[3])
subcirc0.u(-0.752000,0.481000,-0.536000, qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(-0.954000,param_0,0.199000, 2)
main_circ.ry(-0.314000, 0)
main_circ.rz(param_0, 2)
main_circ.s(0)
main_circ.u(param_0,param_0,0.388000, 1)
main_circ.ry(0.739000, 1)
main_circ.ry(0.603000, 2)
main_circ.rz(-0.675000, 3)
main_circ.rz(param_0, 1)
main_circ.rz(param_0, 3)
main_circ.rz(param_0, 1)
main_circ.rz(0.537000, 2)
main_circ.u(param_0,-0.299000,-0.838000, 3)
main_circ.ry(param_0, 2)
main_circ.rz(-0.663000, 3)
main_circ.s(2)
main_circ.ry(param_0, 1)
main_circ.s(0)
main_circ.u(0.155000,-0.131000,param_0, 1)
main_circ.ry(-0.980000, 2)
main_circ.s(2)
main_circ.ry(0.896000, 0)
main_circ.s(3)
main_circ.rz(param_0, 3)
main_circ.u(-0.140000,0.181000,0.457000, 0)
main_circ.rz(param_0, 0)
main_circ.rz(param_0, 1)
main_circ.u(0.996000,param_0,0.646000, 0)
main_circ.ry(0.041000, 0)
main_circ.ry(-0.446000, 0)
main_circ.s(0)
main_circ.u(param_0,param_0,param_0, 1)
main_circ.rz(-0.725000, 0)
main_circ.rz(param_0, 2)
main_circ.ry(param_0, 0)
main_circ.rz(param_0, 1)
main_circ.s(3)
main_circ.s(2)
main_circ.u(param_0,-0.411000,-0.286000, 0)
main_circ.u(0.014000,param_0,param_0, 0)
main_circ.s(1)
main_circ.u(param_0,param_0,0.781000, 1)
main_circ.rz(0.328000, 3)
main_circ.s(0)
main_circ.ry(-0.673000, 2)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.rz(0.099000, 2)
main_circ.rz(-0.789000, 1)
bindings = {param_0: -0.467000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1922")
