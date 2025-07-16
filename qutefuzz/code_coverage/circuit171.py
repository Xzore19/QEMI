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
subcirc0.u(0.306000,0.011000,-0.542000, qreg_0[1])
subcirc0.u(0,0,0.300000, qreg_0[2])
subcirc0.u(0,0,-0.643000, qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.u(0.584000,0.031000,0.919000, qreg_0[1])
subcirc1.u(-0.114000,0.762000,0.531000, qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0,0,-0.323000, qreg_0[0])
subcirc2.u(0.196000,0.033000,0.769000, qreg_0[0])
subcirc2.u(0.306000,-0.053000,-0.716000, qreg_1[2])
subcirc2.u(-0.497000,-0.048000,-0.459000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(-0.197000,-0.764000,-0.118000, qreg_0[2])
subcirc3.x(qreg_0[3])
subcirc3.u(0,0,-0.211000, qreg_0[0])
subcirc3.u(-0.372000,-0.150000,0.832000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(param_0,0,0.959000, qreg_0[0])
main_circ.x(2)
main_circ.z(3)
main_circ.u(param_0,param_0,-0.047000, 2)
main_circ.u(0,0,param_0, qreg_1[0])
main_circ.x(0)
main_circ.append(subcirc2,[qreg_0[0],0,2,qreg_1[0]])
main_circ.u(-0.744000,-0.221000,-0.072000, qreg_0[0])
main_circ.x(3)
main_circ.u(param_0,param_0,-0.279000, qreg_1[0])
main_circ.z(1)
main_circ.append(subcirc2,[0,3,qreg_0[0],qreg_1[0]])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[0],1,3])
main_circ.u(param_0,param_0,param_0, 3)
main_circ.append(subcirc2,[qreg_0[0],3,2,0])
main_circ.x(qreg_0[0])
main_circ.append(subcirc2,[3,2,1,qreg_0[0]])
main_circ.u(0.351000,-0.312000,-0.121000, qreg_1[0])
main_circ.x(1)
main_circ.append(subcirc3,[3,1,qreg_1[0],2,qreg_0[0],0])
main_circ.u(0,0,param_0, 1)
main_circ.append(subcirc2,[0,3,qreg_0[0],2])
main_circ.u(0.503000,param_0,0.403000, 0)
main_circ.append(subcirc2,[qreg_1[0],3,qreg_0[0],2])
main_circ.x(0)
main_circ.x(qreg_1[0])
bindings = {param_0: 0.970000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "171")
