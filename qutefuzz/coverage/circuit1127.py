from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0.267000,0.181000,0.123000, qreg_3[0])
subcirc0.u(0,0,0.635000, qreg_0[1])
subcirc0.u(0,0,0.527000, qreg_0[0])
subcirc0.ry(0.900000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.020000, qreg_2[0])
subcirc1.ry(0.693000, qreg_0[1])
subcirc1.ry(0.037000, qreg_2[1])
subcirc1.ry(0.002000, qreg_2[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.u(param_0,-0.979000,param_0, qreg_0[2])
main_circ.u(param_0,param_0,0.270000, qreg_0[1])
main_circ.rx(0.118000, qreg_0[0])
main_circ.ry(param_0, qreg_0[0])
main_circ.ry(-0.198000, qreg_0[2])
main_circ.rx(0.070000, qreg_0[1])
main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.u(param_0,0.753000,param_0, qreg_0[0])
main_circ.u(-0.359000,param_0,param_0, qreg_3[0])
main_circ.ry(param_0, 0)
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],0,qreg_0[2]])
main_circ.u(param_0,-0.656000,-0.102000, qreg_0[2])
main_circ.rx(0.859000, 0)
main_circ.u(-0.102000,param_0,param_0, qreg_3[0])
main_circ.u(0.686000,0.789000,0.535000, qreg_0[1])
main_circ.ry(-0.342000, qreg_0[1])
main_circ.u(-0.676000,0.406000,0.004000, qreg_0[0])
main_circ.u(param_0,param_0,-0.807000, 0)
main_circ.rx(-0.306000, qreg_0[0])
main_circ.ry(0.879000, qreg_0[0])
main_circ.u(param_0,0.608000,param_0, qreg_0[1])
main_circ.ry(param_0, qreg_3[0])
main_circ.u(param_0,-0.407000,0.338000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],0])
main_circ.rx(-0.374000, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],0])
main_circ.u(-0.124000,param_0,param_0, qreg_0[1])
main_circ.rx(-0.082000, qreg_0[2])
main_circ.u(0,param_0,-0.686000, 0)
main_circ.rx(-0.252000, qreg_0[0])
main_circ.rx(param_0, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[1],qreg_0[0]])
main_circ.rx(-0.836000, qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.rx(param_0, qreg_3[0])
main_circ.u(0,0,0.208000, qreg_0[1])
main_circ.u(0,0,param_0, qreg_0[1])
main_circ.u(param_0,param_0,0.921000, 0)
main_circ.ry(0.958000, qreg_3[0])
main_circ.rx(param_0, qreg_3[0])
bindings = {param_0: -0.179000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1127")
