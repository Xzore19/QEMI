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
subcirc0.cx(qreg_1[2],qreg_1[0])
subcirc0.cz(qreg_1[2],qreg_0[0])
subcirc0.rx(0.300000, qreg_0[0])
subcirc0.cx(qreg_1[1],qreg_1[0])
subcirc0.rx(0.565000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1.u(0,0,-0.738000, qreg_0[2])
subcirc1.u(0,0,-0.293000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.u(0,0,0.422000, qreg_0[2])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.u(0,0,-0.817000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rx(-0.480000, qreg_0[0])
subcirc3.rx(-0.091000, qreg_0[0])
subcirc3.u(0,0,0.909000, qreg_0[0])
subcirc3.u(0,0,0.670000, qreg_2[1])
subcirc3.u(0,0,-0.693000, qreg_2[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rx(0.670000, 0)
main_circ.cz(3,1)
main_circ.cx(2,3)
main_circ.cx(0,1)
main_circ.rx(param_2, 3)
main_circ.rx(param_1, 0)
main_circ.rx(0.831000, 3)
main_circ.u(0,0,param_1, 3)
main_circ.rx(0.541000, 1)
main_circ.cz(0,3)
main_circ.cz(3,0)
main_circ.rx(0.704000, 3)
main_circ.cz(1,2)
main_circ.u(param_1,param_1,-0.504000, 2)
main_circ.rx(param_1, 0)
main_circ.cz(3,0)
main_circ.cx(1,2)
main_circ.rx(-0.253000, 3)
main_circ.rx(param_1, 1)
main_circ.rx(-0.537000, 1)
main_circ.rx(-0.803000, 1)
main_circ.cx(0,3)
main_circ.rx(0.540000, 1)
main_circ.cx(3,1)
main_circ.u(param_0,0,0.306000, 1)
main_circ.cx(3,0)
main_circ.cz(1,0)
main_circ.cz(2,3)
main_circ.u(param_1,0,0.857000, 1)
main_circ.u(param_1,param_2,0.314000, 3)
main_circ.cx(1,0)
main_circ.rx(param_1, 0)
main_circ.rx(0.610000, 0)
main_circ.u(0,0,0.374000, 0)
main_circ.u(param_2,param_0,param_1, 1)
main_circ.rx(0.778000, 0)
main_circ.rx(param_0, 1)
main_circ.cx(2,0)
main_circ.rx(0.904000, 3)
main_circ.cz(1,3)
main_circ.cz(3,1)
main_circ.rx(0.096000, 3)
main_circ.u(0,0,-0.323000, 0)
main_circ.rx(-0.889000, 1)
main_circ.rx(-0.521000, 0)
main_circ.u(param_1,param_1,-0.449000, 0)
bindings = {param_0: 0.101000, param_1: 0.728000, param_2: 0.916000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1857")
