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
subcirc0.u(-0.707000,-0.258000,-0.174000, qreg_0[2])
subcirc0.ry(-0.661000, qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_0[2])
subcirc0.u(0.217000,0.780000,-0.999000, qreg_3[0])
subcirc0.ry(0.481000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.321000, qreg_0[3])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.x(qreg_0[3])
subcirc1.ry(-0.332000, qreg_0[2])
subcirc1.x(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.ry(-0.060000, 2)
main_circ.x(1)
main_circ.cz(2,3)
main_circ.u(0.819000,-0.040000,-0.109000, 1)
main_circ.cz(0,1)
main_circ.cz(2,1)
main_circ.cz(2,0)
main_circ.ry(param_0, 1)
main_circ.ry(0.099000, 1)
main_circ.ry(param_1, 1)
main_circ.ry(0.763000, 0)
main_circ.ry(param_1, 3)
main_circ.cz(1,0)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.cz(2,0)
main_circ.ry(param_0, 0)
main_circ.append(subcirc1,[3,1,0,2])
main_circ.cz(0,2)
main_circ.cz(2,1)
main_circ.ry(param_0, 3)
main_circ.ry(-0.494000, 0)
main_circ.u(0.161000,param_0,param_1, 0)
main_circ.ry(param_1, 1)
main_circ.append(subcirc1,[2,0,3,1])
main_circ.cz(1,2)
main_circ.cz(1,2)
main_circ.x(1)
main_circ.ry(0.769000, 3)
main_circ.ry(param_0, 2)
main_circ.x(0)
main_circ.cz(1,2)
main_circ.ry(0.685000, 2)
main_circ.u(param_1,-0.382000,param_0, 3)
bindings = {param_0: -0.918000, param_1: 0.221000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "883")
