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
subcirc0.z(qreg_0[0])
subcirc0.u(0,0,0.218000, qreg_0[0])
subcirc0.u(0,0,-0.252000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.rx(-0.198000, qreg_0[0])
main_circ.z(qreg_2[0])
main_circ.u(0,0,param_0, qreg_2[0])
main_circ.rx(param_0, qreg_2[0])
main_circ.append(subcirc0,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.u(param_0,param_0,-0.970000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_0[0],qreg_2[0]])
main_circ.rx(param_0, qreg_2[1])
main_circ.cy(qreg_2[0],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.u(param_0,0,param_0, qreg_2[0])
main_circ.rx(-0.730000, qreg_2[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_0[0],qreg_2[0]])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_2[1])
main_circ.cy(qreg_2[0],qreg_2[1])
main_circ.cy(qreg_2[1],qreg_0[1])
main_circ.z(qreg_2[1])
main_circ.z(qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.z(qreg_2[0])
bindings = {param_0: -0.541000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1844")
