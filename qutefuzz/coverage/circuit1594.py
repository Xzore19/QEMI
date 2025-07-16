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
subcirc0.u(-0.133000,-0.519000,-0.513000, qreg_1[2])
subcirc0.cy(qreg_1[1],qreg_1[2])
subcirc0.cy(qreg_1[2],qreg_1[1])
subcirc0.cy(qreg_1[2],qreg_1[1])
subcirc0.u(0.329000,-0.003000,0.495000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rz(-0.631000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_2[0])
subcirc1.z(qreg_2[0])
subcirc1.u(-0.483000,-0.740000,0.310000, qreg_0[0])
subcirc1.cy(qreg_2[0],qreg_0[1])

main_circ = QuantumCircuit(1)
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

main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.u(param_0,-0.732000,param_0, qreg_3[0])
main_circ.z(qreg_3[0])
main_circ.u(param_0,param_0,param_0, 0)
main_circ.z(qreg_0[0])
main_circ.z(0)
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_3[0],qreg_0[1]])
main_circ.z(qreg_2[0])
main_circ.z(0)
main_circ.u(param_0,0.552000,-0.810000, qreg_0[1])
main_circ.u(0.382000,-0.819000,param_0, qreg_3[0])
main_circ.rz(param_0, 0)
main_circ.u(-0.599000,param_0,0.664000, qreg_3[0])
main_circ.u(param_0,param_0,-0.316000, qreg_3[0])
main_circ.u(param_0,param_0,-0.244000, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_3[0]])
main_circ.z(0)
main_circ.u(param_0,0.313000,param_0, qreg_2[0])
main_circ.cy(qreg_0[0],0)
main_circ.z(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.cy(0,qreg_3[0])
main_circ.cy(0,qreg_0[1])
main_circ.cy(0,qreg_0[1])
main_circ.cy(qreg_0[1],qreg_3[0])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.rz(param_0, qreg_3[0])
main_circ.u(param_0,0.784000,param_0, qreg_2[0])
main_circ.rz(-0.508000, 0)
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.z(0)
bindings = {param_0: -0.527000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
