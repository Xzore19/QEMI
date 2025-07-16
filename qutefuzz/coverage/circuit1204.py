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
subcirc0.u(-0.793000,-0.589000,0.622000, qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_3[0],qreg_1[1])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_1[1])
subcirc1.u(-0.137000,0.613000,0.218000, qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_1[1])
subcirc1.u(0.919000,0.485000,-0.485000, qreg_1[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_1[2],qreg_0[0])
subcirc2.cz(qreg_1[1],qreg_1[2])
subcirc2.cx(qreg_1[2],qreg_1[0])
subcirc2.cx(qreg_1[1],qreg_1[2])
subcirc2.cy(qreg_1[1],qreg_1[0])
subcirc2.cz(qreg_1[0],qreg_1[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[0],qreg_0[1])
subcirc3.cz(qreg_0[1],qreg_3[0])
subcirc3.u(0.458000,0.607000,-0.192000, qreg_3[0])
subcirc3.u(0.414000,-0.063000,0.007000, qreg_0[0])
subcirc3.u(-0.850000,0.396000,0.334000, qreg_0[2])
subcirc3.cz(qreg_0[0],qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(param_0,-0.334000,-0.264000, qreg_0[2])
main_circ.cz(qreg_3[0],qreg_0[1])
main_circ.u(-0.044000,param_0,0.870000, qreg_3[0])
main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.u(-0.580000,0.661000,param_0, qreg_0[1])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.append(subcirc3,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.u(param_0,param_0,0.449000, qreg_3[0])
main_circ.cz(qreg_0[2],qreg_3[0])
main_circ.cy(qreg_0[1],qreg_3[0])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc3,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.u(-0.044000,-0.428000,param_0, qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.u(param_0,-0.672000,param_0, qreg_0[2])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cx(qreg_0[1],qreg_0[2])
bindings = {param_0: -0.809000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1204")
