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
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.cy(qreg_2[0],qreg_3[0])
subcirc0.u(pi/2,0.211000,0.314000, qreg_2[0])
subcirc0.u(pi/2,-0.941000,-0.339000, qreg_2[0])
subcirc0.u(pi/2,0.193000,0.447000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(pi/2,0.611000,-0.808000, 1)
main_circ.cy(qreg_0[0],0)
main_circ.u(pi/2,param_3,0.918000, 1)
main_circ.u(pi/2,param_2,0.954000, 1)
main_circ.append(subcirc0,[1,qreg_0[0],0,2,3])
main_circ.cy(1,3)
main_circ.append(subcirc0,[qreg_0[0],3,2,0,1])
main_circ.z(qreg_0[0])
main_circ.u(pi/2,param_0,-0.310000, 2)
main_circ.u(param_2,param_4,param_5, qreg_0[0])
main_circ.cy(0,2)
main_circ.append(subcirc0,[qreg_0[0],3,1,0,2])
main_circ.cy(1,qreg_0[0])
main_circ.append(subcirc0,[0,2,1,qreg_0[0],3])
main_circ.z(2)
main_circ.append(subcirc0,[0,2,qreg_0[0],3,1])
main_circ.append(subcirc0,[qreg_0[0],3,1,0,2])
main_circ.append(subcirc0,[2,3,0,qreg_0[0],1])
main_circ.y(0)
bindings = {param_0: -0.112000, param_2: -0.850000, param_3: -0.643000, param_4: 0.288000, param_5: -0.348000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1733")
