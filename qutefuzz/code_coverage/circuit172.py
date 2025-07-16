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
subcirc0.y(qreg_0[0])
subcirc0.rx(-0.927000, qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.rx(0.011000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.168000, qreg_0[2])
subcirc1.rx(-0.153000, qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.rx(-0.370000, qreg_0[1])

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

main_circ.x(1)
main_circ.rx(0.421000, 1)
main_circ.rz(param_1, 0)
main_circ.rz(param_0, 3)
main_circ.y(2)
main_circ.y(0)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.rx(0.212000, 1)
main_circ.rx(0.283000, 1)
main_circ.y(0)
main_circ.rz(0.493000, 2)
main_circ.y(2)
main_circ.x(2)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.rx(0.219000, 1)
main_circ.rz(param_1, 0)
main_circ.rx(-0.658000, 1)
main_circ.x(3)
main_circ.rz(0.850000, 1)
main_circ.x(2)
main_circ.x(3)
main_circ.append(subcirc1,[0,1,qreg_0[0],3])
main_circ.append(subcirc1,[2,3,1,qreg_0[0]])
main_circ.rz(0.432000, qreg_0[0])
main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_1, 1)
main_circ.y(1)
main_circ.x(qreg_0[0])
main_circ.x(0)
main_circ.append(subcirc1,[2,qreg_0[0],0,3])
main_circ.y(1)
main_circ.rx(-0.510000, 3)
bindings = {param_0: -0.679000, param_1: -0.623000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "172")
