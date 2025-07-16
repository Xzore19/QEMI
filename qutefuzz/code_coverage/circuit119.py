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
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.u(-0.343000,0.861000,-0.955000, qreg_3[0])
subcirc0.u(0.147000,0.799000,-0.723000, qreg_0[0])
subcirc0.u(-0.979000,-0.766000,-0.033000, qreg_0[2])
subcirc0.rz(-0.184000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.u(-0.176000,0.688000,-0.591000, qreg_0[1])
subcirc1.u(0.320000,-0.502000,-0.560000, qreg_0[3])
subcirc1.u(-0.508000,-0.609000,-0.633000, qreg_0[0])
subcirc1.rz(-0.888000, qreg_0[3])
subcirc1.u(0.260000,-0.809000,0.871000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.y(qreg_1[2])
subcirc2.cy(qreg_1[2],qreg_1[0])
subcirc2.u(0.845000,0.830000,0.555000, qreg_1[1])
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_1[2])
subcirc2.u(-0.694000,0.427000,-0.592000, qreg_1[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(0)
main_circ.append(subcirc2,[0,1,qreg_0[1],qreg_0[2]])
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.rz(param_0, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.y(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[2],0,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[3],0,1,qreg_0[0]])
main_circ.y(qreg_0[2])
main_circ.y(qreg_0[0])
main_circ.u(param_1,param_1,param_0, qreg_0[1])
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[3],1,qreg_0[0]])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_0[2])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.cy(qreg_0[3],0)
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.u(0.751000,0.808000,param_1, qreg_0[3])
bindings = {param_0: 0.360000, param_1: 0.118000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "119")
