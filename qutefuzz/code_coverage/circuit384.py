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
subcirc0.h(qreg_2[1])
subcirc0.rz(-0.891000, qreg_2[1])
subcirc0.u(pi/2,-0.461000,0.523000, qreg_2[1])
subcirc0.u(pi/2,0.222000,-0.993000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.898000,0.766000, qreg_0[2])
subcirc1.h(qreg_0[3])
subcirc1.h(qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.h(2)
main_circ.rz(0.838000, 3)
main_circ.rz(param_0, 1)
main_circ.rz(-0.298000, 1)
main_circ.y(3)
main_circ.h(3)
main_circ.rz(param_0, 2)
main_circ.h(1)
main_circ.rz(param_0, 0)
main_circ.u(pi/2,0.890000,-0.158000, 2)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.rz(0.410000, 3)
main_circ.y(0)
main_circ.h(2)
main_circ.h(1)
main_circ.h(0)
main_circ.y(3)
main_circ.rz(0.368000, 1)
main_circ.rz(param_0, 3)
main_circ.y(1)
main_circ.y(1)
main_circ.rz(param_0, 2)
main_circ.rz(param_0, 0)
main_circ.y(1)
main_circ.u(pi/2,param_0,param_0, 0)
main_circ.h(2)
main_circ.u(param_0,0.188000,-0.704000, 0)
main_circ.rz(param_0, 0)
main_circ.rz(param_0, 0)
main_circ.u(param_0,0.725000,param_0, 1)
main_circ.u(pi/2,-0.212000,param_0, 2)
main_circ.h(3)
main_circ.u(param_0,-0.759000,param_0, 1)
main_circ.rz(param_0, 0)
main_circ.y(0)
main_circ.u(param_0,0.700000,0.593000, 3)
main_circ.y(3)
main_circ.y(2)
main_circ.h(2)
main_circ.h(0)
main_circ.u(pi/2,param_0,param_0, 3)
main_circ.u(param_0,param_0,param_0, 2)
main_circ.u(param_0,param_0,param_0, 3)
main_circ.y(3)
main_circ.rz(0.389000, 0)
bindings = {param_0: 0.521000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "384")
