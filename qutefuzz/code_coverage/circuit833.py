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
subcirc0.u(-0.295000,0.324000,-0.448000, qreg_0[1])
subcirc0.rz(-0.487000, qreg_0[1])
subcirc0.rz(-0.616000, qreg_0[0])
subcirc0.u(pi/2,-0.092000,0.061000, qreg_0[1])
subcirc0.u(0.456000,-0.960000,-0.306000, qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(pi/2,param_0,param_0, qreg_3[0])
main_circ.rz(0.389000, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_3[0],qreg_0[0]])
main_circ.rz(param_0, qreg_2[0])
main_circ.rz(param_0, qreg_0[1])
main_circ.rz(0.986000, qreg_0[0])
main_circ.u(param_0,param_0,param_0, qreg_2[0])
main_circ.u(pi/2,param_0,0.584000, qreg_0[1])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.u(param_0,param_0,0.429000, qreg_0[1])
main_circ.u(param_0,0.130000,param_0, qreg_3[0])
main_circ.u(param_0,0.642000,0.212000, qreg_0[0])
main_circ.u(param_0,0,param_0, qreg_0[1])
main_circ.u(-0.046000,-0.644000,-0.996000, qreg_0[0])
main_circ.u(param_0,0.757000,0.062000, qreg_2[0])
main_circ.u(0,param_0,param_0, qreg_2[0])
main_circ.rz(param_0, qreg_3[0])
main_circ.u(-0.981000,0.356000,param_0, qreg_0[0])
main_circ.rz(-0.155000, qreg_0[1])
main_circ.u(pi/2,0.417000,-0.110000, qreg_3[0])
main_circ.u(param_0,0.907000,0.806000, qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.u(0,param_0,param_0, qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.u(param_0,param_0,-0.366000, qreg_0[1])
main_circ.rz(param_0, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_2[0]])
main_circ.u(0.448000,param_0,param_0, qreg_2[0])
main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.u(0,param_0,param_0, qreg_3[0])
bindings = {param_0: 0.773000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "833")
